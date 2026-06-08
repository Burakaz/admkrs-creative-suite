#!/usr/bin/env node
/**
 * ADMKRS Creative Briefing — DOCX builder
 * ----------------------------------------
 * Renders a briefing JSON spec into a .docx that matches the ADMKRS house style
 * (black table headers + white text, light-grey zebra rows, lavender "Locked"
 * callout, cream "Strategic anchor" callout, B4 Querformat (Landscape) / 1 cm Ränder).
 *
 * Usage:
 *   node build_briefing.js <input.json> [output.docx]
 *
 * The JSON schema is documented in references/document-format.md and there are
 * two complete reference inputs in examples/. Inline markup inside any text
 * field:  <b>bold</b>  <i>italic</i>  (literal "*" and "—" stay literal),
 * and "\n" starts a new line inside a cell / paragraph.
 */

const fs = require("fs");
const path = require("path");
const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell,
  AlignmentType, BorderStyle, WidthType, ShadingType, VerticalAlign,
  HeadingLevel, LevelFormat, PageOrientation
} = require("docx");

/* ----------------------------------------------------------------------- *
 * DESIGN TOKENS  — derived 1:1 from the two reference Google Docs
 * ----------------------------------------------------------------------- */
const T = {
  font: "Arial",
  ink: "111111",          // near-black body / headings
  headerFill: "0A0A0A",   // table header row/column fill (reads as black)
  headerText: "FFFFFF",
  body: "1A1A1A",         // table body text
  dek: "5F5F5F",          // sub-title / dek line
  eyebrow: "6B6B6B",      // kicker above title
  label: "8A8A8A",        // italic family label under a concept header
  border: "D9D9D9",       // table grid lines
  zebra: "F4F4F4",        // alternate row shade
  shadeCol: "F1F1F1",     // hooks letter-column shade
  lockedFill: "ECEAF6",   // lavender  "Gesperrt / Locked" callout
  lockedBar: "B9AEDB",    // lavender accent bar
  anchorFill: "FFF7DE",   // cream  "Strategic anchor" callout
  anchorBar: "E8B923",    // gold accent bar
};

// sizes are half-points (docx unit): 1pt = 2
const SZ = {
  title: 52, eyebrow: 18, dek: 21, h1: 33, h2: 26, h3: 22,
  label: 18, body: 18, header: 18, callout: 19, p: 21, outro: 20,
};

/* ADMKRS-Dokumentstandard: B4 QUERFORMAT (ISO B4 250×353 mm), 1 cm Ränder.
   Landscape-Trick (docx-js): kurze Kante als width, lange als height + orientation LANDSCAPE;
   docx-js swapt sie im XML. Inhaltsbreite spannt die LANGE Kante minus Ränder. (1 mm = 56.6929 DXA) */
const SHORT_EDGE = 14173;   // 250 mm  → width  (wird für Landscape getauscht)
const LONG_EDGE  = 20013;   // 353 mm  → height
const MARGIN = 567;         // 1 cm
const CONTENT_W = LONG_EDGE - 2 * MARGIN;   // 18879 DXA — Inhalt über die lange Kante

/* ----------------------------------------------------------------------- *
 * Inline + paragraph helpers
 * ----------------------------------------------------------------------- */
function mkRun(text, o = {}) {
  return new TextRun({
    text,
    font: T.font,
    size: o.size || SZ.body,
    color: o.color || T.body,
    bold: !!o.bold,
    italics: !!o.italics,
    allCaps: !!o.allCaps,
    characterSpacing: o.spacing || 0,
  });
}

// Parse <b>/<i> tags into runs. Literal "*"/"—" are untouched.
function inlineRuns(text, base = {}) {
  const runs = [];
  let bold = 0, ital = 0, buf = "";
  const flush = () => {
    if (buf) runs.push(mkRun(buf, { ...base, bold: bold > 0 || base.bold, italics: ital > 0 || base.italics }));
    buf = "";
  };
  const s = String(text);
  for (let i = 0; i < s.length;) {
    if (s.startsWith("<b>", i)) { flush(); bold++; i += 3; }
    else if (s.startsWith("</b>", i)) { flush(); bold = Math.max(0, bold - 1); i += 4; }
    else if (s.startsWith("<i>", i)) { flush(); ital++; i += 3; }
    else if (s.startsWith("</i>", i)) { flush(); ital = Math.max(0, ital - 1); i += 4; }
    else { buf += s[i]; i++; }
  }
  flush();
  return runs.length ? runs : [mkRun("", base)];
}

// One text field -> array of Paragraphs (split on "\n"); supports a bold lead-in.
function textParagraphs(text, base = {}, pOpts = {}) {
  const lines = String(text == null ? "" : text).split("\n");
  return lines.map((ln, idx) =>
    new Paragraph({
      children: inlineRuns(ln, base),
      spacing: { after: idx === lines.length - 1 ? (pOpts.afterLast ?? 0) : (pOpts.between ?? 20), line: 252 },
      alignment: pOpts.align || AlignmentType.LEFT,
    })
  );
}

/* ----------------------------------------------------------------------- *
 * Table helpers
 * ----------------------------------------------------------------------- */
function noBorder() { return { style: BorderStyle.NONE, size: 0, color: "FFFFFF" }; }
function gridBorder() { return { style: BorderStyle.SINGLE, size: 4, color: T.border }; }
function allGrid() {
  return { top: gridBorder(), bottom: gridBorder(), left: gridBorder(), right: gridBorder(),
           insideHorizontal: gridBorder(), insideVertical: gridBorder() };
}

function cell(content, o = {}) {
  const base = { size: o.size || SZ.body, color: o.color || T.body, bold: o.bold, italics: o.italics };
  const paras = textParagraphs(content, base, { between: 18, afterLast: 0, align: o.align });
  return new TableCell({
    width: { size: o.width, type: WidthType.DXA },
    shading: o.fill ? { fill: o.fill, type: ShadingType.CLEAR, color: "auto" } : undefined,
    margins: { top: 60, bottom: 60, left: 110, right: 110 },
    verticalAlign: o.vAlign || VerticalAlign.CENTER,
    borders: o.borders,
    columnSpan: o.colSpan,
    children: paras.length ? paras : [new Paragraph({ children: [mkRun("")] })],
  });
}

// scale relative weights to the content width
function scaleWidths(weights, total = CONTENT_W) {
  const sum = weights.reduce((a, b) => a + b, 0);
  const out = weights.map(w => Math.round((w / sum) * total));
  out[out.length - 1] = total - out.slice(0, -1).reduce((a, b) => a + b, 0);
  return out;
}

/* ----------------------------------------------------------------------- *
 * Block renderers
 * ----------------------------------------------------------------------- */

// Generic data table with a black header row. style: "plain" | "zebra"
function tableHeaderRow(block) {
  const widths = scaleWidths(block.widths || block.header.map(() => 1));
  const colAligns = block.colAligns || [];
  const rows = [];

  // header
  rows.push(new TableRow({
    tableHeader: true,
    children: block.header.map((h, i) => cell(h, {
      width: widths[i], fill: T.headerFill, color: T.headerText, bold: true, size: SZ.header,
      align: colAligns[i] === "center" ? AlignmentType.CENTER : AlignmentType.LEFT,
      borders: { top: noBorder(), bottom: noBorder(), left: noBorder(), right: noBorder(),
                 insideVertical: noBorder() },
    })),
  }));

  // body
  block.rows.forEach((r, ri) => {
    const zebra = block.style === "zebra" && ri % 2 === 1;
    rows.push(new TableRow({
      children: r.map((c, i) => cell(c, {
        width: widths[i],
        fill: zebra ? T.zebra : undefined,
        size: SZ.body,
        italics: block.colItalics && block.colItalics[i],
        align: colAligns[i] === "center" ? AlignmentType.CENTER : AlignmentType.LEFT,
        vAlign: VerticalAlign.TOP,
      })),
    }));
  });

  return new Table({
    width: { size: CONTENT_W, type: WidthType.DXA },
    columnWidths: widths,
    borders: allGrid(),
    rows,
  });
}

// Key/value table: left column is a black "header" column, right column is body.
function tableKeyValue(block) {
  const widths = scaleWidths(block.widths || [1, 3.2]);
  const rows = block.rows.map(([k, v]) => new TableRow({
    children: [
      cell(k, { width: widths[0], fill: T.headerFill, color: T.headerText, bold: true, size: SZ.header,
                vAlign: VerticalAlign.CENTER }),
      cell(v, { width: widths[1], size: SZ.body, vAlign: VerticalAlign.CENTER }),
    ],
  }));
  return new Table({ width: { size: CONTENT_W, type: WidthType.DXA }, columnWidths: widths, borders: allGrid(), rows });
}

// Hooks table: shaded centered letter column + hook text.
function tableHooks(block) {
  const widths = scaleWidths(block.widths || [0.7, 9]);
  const rows = block.rows.map(([letter, hook]) => new TableRow({
    children: [
      cell(letter, { width: widths[0], fill: T.shadeCol, bold: true, align: AlignmentType.CENTER, size: SZ.body }),
      cell(hook, { width: widths[1], size: SZ.body }),
    ],
  }));
  return new Table({ width: { size: CONTENT_W, type: WidthType.DXA }, columnWidths: widths, borders: allGrid(), rows });
}

// Full-width single-cell callout (locked = lavender, anchor = cream + gold bar).
function callout(block) {
  const isAnchor = block.variant === "anchor";
  const fill = isAnchor ? T.anchorFill : T.lockedFill;
  const barColor = isAnchor ? T.anchorBar : T.lockedBar;
  const borders = {
    top: noBorder(), bottom: noBorder(), right: noBorder(),
    left: { style: BorderStyle.SINGLE, size: isAnchor ? 24 : 18, color: barColor },
  };
  const runs = [];
  if (block.lead) runs.push(mkRun(block.lead + "  ", { bold: true, italics: false, size: SZ.callout, color: T.ink }));
  inlineRuns(block.text, { italics: true, size: SZ.callout, color: "3C3C3C" }).forEach(r => runs.push(r));
  const para = new Paragraph({ children: runs, spacing: { line: 264 } });
  const c = new TableCell({
    width: { size: CONTENT_W, type: WidthType.DXA },
    shading: { fill, type: ShadingType.CLEAR, color: "auto" },
    margins: { top: 110, bottom: 110, left: 160, right: 140 },
    borders,
    children: [para],
  });
  return new Table({
    width: { size: CONTENT_W, type: WidthType.DXA },
    columnWidths: [CONTENT_W],
    borders: { top: noBorder(), bottom: noBorder(), left: noBorder(), right: noBorder() },
    rows: [new TableRow({ children: [c] })],
  });
}

function heading(text, level) {
  const map = {
    h1: { size: SZ.h1, before: 320, after: 140 },
    h2: { size: SZ.h2, before: 300, after: 80 },
    h3: { size: SZ.h3, before: 220, after: 70 },
  }[level];
  return new Paragraph({
    children: inlineRuns(text, { bold: true, size: map.size, color: T.ink }),
    spacing: { before: map.before, after: map.after },
    keepNext: true,
  });
}

/* ----------------------------------------------------------------------- *
 * Document assembly
 * ----------------------------------------------------------------------- */
function buildBody(spec) {
  const out = [];
  const h = spec.header || {};
  if (h.eyebrow) out.push(new Paragraph({
    children: inlineRuns(h.eyebrow, { bold: true, size: SZ.eyebrow, color: T.eyebrow, allCaps: true, spacing: 30 }),
    spacing: { after: 40 },
  }));
  if (h.title) out.push(new Paragraph({
    children: inlineRuns(h.title, { bold: true, size: SZ.title, color: T.ink }),
    spacing: { after: 60 }, keepNext: true,
  }));
  if (h.dek) out.push(new Paragraph({
    children: inlineRuns(h.dek, { bold: true, size: SZ.dek, color: T.dek }),
    spacing: { after: 120 },
  }));

  (spec.blocks || []).forEach(b => {
    switch (b.type) {
      case "h1": case "h2": case "h3": out.push(heading(b.text, b.type)); break;
      case "label": out.push(new Paragraph({
        children: inlineRuns(b.text, { italics: true, size: SZ.label, color: T.label }),
        spacing: { after: 90 },
      })); break;
      case "p": out.push(...textParagraphs(b.text, { size: SZ.p, color: T.ink },
        { between: 30, afterLast: 60 })); break;
      case "lede": out.push(new Paragraph({
        children: inlineRuns(b.text, { bold: true, size: SZ.p, color: T.ink }), spacing: { after: 40 },
      })); break;
      case "table":
        if (b.layout === "keyvalue") out.push(tableKeyValue(b));
        else if (b.layout === "hooks") out.push(tableHooks(b));
        else out.push(tableHeaderRow(b));
        out.push(new Paragraph({ children: [mkRun("")], spacing: { after: 60 } }));
        break;
      case "callout": out.push(callout(b));
        out.push(new Paragraph({ children: [mkRun("")], spacing: { after: 60 } })); break;
      case "outro": out.push(new Paragraph({
        children: [mkRun((b.lead || "Outro.") + "  ", { bold: true, size: SZ.outro, color: T.ink }),
                   ...inlineRuns(b.text, { size: SZ.outro, color: T.body })],
        spacing: { before: 60, after: 120 },
      })); break;
      case "spacer": out.push(new Paragraph({ children: [mkRun("")], spacing: { after: b.size || 120 } })); break;
      case "divider": out.push(new Paragraph({
        border: { bottom: { style: BorderStyle.SINGLE, size: 6, color: T.border, space: 1 } },
        spacing: { before: 120, after: 120 }, children: [mkRun("")],
      })); break;
      default: break;
    }
  });
  return out;
}

function build(spec) {
  return new Document({
    creator: "ADMKRS", title: spec.filename || "Creative Briefing",
    styles: { default: { document: { run: { font: T.font, size: SZ.body, color: T.body } } } },
    sections: [{
      properties: { page: {
        size: { width: SHORT_EDGE, height: LONG_EDGE, orientation: PageOrientation.LANDSCAPE },
        margin: { top: MARGIN, right: MARGIN, bottom: MARGIN, left: MARGIN } } },
      children: buildBody(spec),
    }],
  });
}

/* ----------------------------------------------------------------------- *
 * CLI
 * ----------------------------------------------------------------------- */
function main() {
  const input = process.argv[2];
  if (!input) { console.error("Usage: node build_briefing.js <input.json> [output.docx]"); process.exit(1); }
  const spec = JSON.parse(fs.readFileSync(input, "utf8"));
  const outPath = process.argv[3] ||
    path.join(path.dirname(input), (spec.filename || "briefing").replace(/\.docx$/, "") + ".docx");
  Packer.toBuffer(build(spec)).then(buf => {
    fs.writeFileSync(outPath, buf);
    console.log("Wrote " + outPath);
  });
}
main();
