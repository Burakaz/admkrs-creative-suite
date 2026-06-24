# Dokument-Format - Lokalisierungs-Briefing (verbindlich)

Gerendert über die **gemeinsame Builder-Engine** `../admkrs-cs-creative-briefing/assets/build_briefing.js` (Node + `docx`). **Keine neue Renderlogik**, gleicher Haus-Stil: B4 Querformat, 1 cm Ränder, schwarze Tabellen-Header, Arial, Zebra, Design-Tokens. Du füllst nur den Inhalt.

**Vorgehen:** Nimm `examples/localization_statics_example.json` bzw. `examples/localization_motion_example.json` als Muster, Struktur kopieren, Inhalt ersetzen. Nicht von Null bauen.

---

## Builder ausführen

```bash
cd <skill>/../admkrs-cs-creative-briefing/assets && npm install docx   # einmalig pro Umgebung
node ../admkrs-cs-creative-briefing/assets/build_briefing.js <input.json> <YYMMDD_BRAND_Product_Type_LANG.docx>
```

Wird der Output-Name weggelassen, nimmt der Builder das Feld `filename` aus der JSON. **Dateiname-Konvention:** `YYMMDD_BRAND_Product_Type_LANG` - die **Zielsprache** steht am Ende (`NL`, `FR`, `ES`, `IT` …). Danach das .docx mit `present_files` zeigen. **Best Practice (Cowork mit Drive):** das fertige .docx in der Kunden-Drive unter „Briefings" ablegen, nicht ungefragt in Slack/ClickUp posten.

Render-Check (Pflicht bei Lokalisierung): docx → PDF → JPEG (LibreOffice `--convert-to pdf`, dann `pdftoppm -jpeg`). **Sonderzeichen prüfen** (ä/ö/ü/é/è/ï/ç/„"/·/…) und Seiten-Fit.

---

## 1 - Sprache der Struktur (Kernregel)

**Alle** Labels, Header, Spaltennamen, Legende und Notizen sind **ENGLISCH** - internationale Teams arbeiten daran. Nur die **Copy-Zellen** tragen DE-Original und Zielsprache.

## 2 - Kopf (`header` + erste Blocks)

- `eyebrow`: `LOCALIZATION · ORIGINAL → TRANSLATION`
- `title`: `{Brand} · {Product} · DE → {LANG}`
- `dek`: `{scope, z. B. 3 Statics + 1 Motion Ad} · {Market} · {Date} · Draft`
- `p` **Glossary anchors:** eine Zeile mit den genutzten bindenden Mappings, z. B. `Glossary anchors: 97% weniger Zucker → 97% minder suiker · Disclaimer → official NL wording (below).`
- `p` **Legend (Englisch, Pflicht):**
  `<b>Bold = goes on the creative (final translated copy).</b> Left column = DE source (reference). Use all translated copy 1:1, do not re-translate, do not change numbers.`

## 3 - Statics / Carousel: Vergleichstabelle

`table` · `layout: "headerrow"` · `style: "plain"` · `widths: [1.25, 0.95, 2.5, 2.5]` · `colAligns: ["left","left","left","left"]`
- `header`: `["Asset", "Element", "Original (DE)", "Translation ({LANG})"]`
- Pro Asset Zeilen für `Hook`, `Subline`, `Badges`, `CTA` (nur, was existiert). **Asset-Name nur in der ersten Zeile der Gruppe**, danach leer (`""`).
- **Translation-Zellen `<b>fett</b>`** (= landet aufs Creative). Original-Spalte regular (Referenz).
- Disclaimer als Fußnote **unter** der Tabelle: `h3 "Disclaimer (all assets)"` + `p` mit `DE: …` und `{LANG}: <b>…</b> (official glossary wording)`.

## 4 - Motion / Video: NUR zwei Spalten (vereinfacht, wichtig)

`table` · `layout: "headerrow"` · `style: "zebra"` · `widths: [1, 1.4]` · `colItalics: [false, true]`
- `header`: `["On-Screen Text", "Voice-Over"]`
- **Eine Zeile pro Beat. KEINE Timecode-Spalte. KEINE getrennten Hook-/CTA-Zeilen.**
- **On-Screen-Box** = alles, was eingeblendet wird (Hook, Badges, Offer, CTA, Disclaimer), zusammen in **eine** Zelle, `<b>fett</b>`.
- **Voice-Over-Spalte** = der gesprochene Satz, **kursiv** (regelt `colItalics`).
- Inhalt in der **Zielsprache** (build-ready). DE-Quelle ist optional: nur auf Wunsch als kleine Referenz-Tabelle darüber. **Default ist die saubere 2-Spalten-Zielversion.**

## 5 - Adaptation & Compliance: Note am Ende

`callout` · `variant: "todo"` · `lead: "Adaptation & Compliance"`: zentrale kulturelle Adaptions-Entscheidungen, Markt-Compliance-Flags, Alternativen für riskante Zeilen, offene Glossar-Konflikte zur Klärung.

## 6 - Stil

Translation-Copy fett, Labels/Quelle regular, VO kursiv. Kompakt halten (Tabelle möglichst eine Seite). **Kein „—" in der Copy** (Hausregel).

---

## Inline-Markup & die Mehrzeilen-Bold-Regel (Pflicht)

`<b>fett</b>` · `<i>kursiv</i>` · `\n` = neue Zeile in der Zelle. Literale `*`, `·`, „Anführungszeichen" bleiben unverändert.

**Mehrzeilige On-Creative-Zellen: jede Zeile einzeln in `<b>…</b>` wickeln.** Der Builder trägt ein `<b>` **nicht** über `\n` hinweg, nur die erste Zeile bliebe fett. Also:
- ✗ `"<b>-15% · ALLEEN T/M ZONDAG\n97% minder suiker*\nLIMITED EDITION</b>"` (nur Zeile 1 wird fett)
- ✓ `"<b>-15% · ALLEEN T/M ZONDAG</b>\n<b>97% minder suiker*</b>\n<b>LIMITED EDITION</b>"`

Gilt für Badge-Stapel (Statics) und die On-Screen-Box (Motion), wann immer mehrere Zeilen aufs Creative gehen.

---

## Block-Typen (wie creative-briefing)

`h1`/`h2`/`h3` · `label` · `lede` · `p` (`\n` für Zeilen) · `table` (`headerrow` · `keyvalue` · `hooks`) · `callout` (`todo`/`anchor`/`locked`) · `spacer` · `divider`. Für die Lokalisierung gebraucht: `p`, `h3`, `table headerrow`, `callout todo`.

**Tabellen-Felder:** `header`, `rows` (Zellenzahl = Spaltenzahl), `widths` (relative Gewichte), `style` `"plain"`/`"zebra"`, optional `colAligns`, `colItalics`.

---

## Platzhalter & nichts erfinden

Fehlt ein Zielbegriff oder ein freigegebener Wert: **`[Placeholder: …]`** inline an der Stelle. Zahlen/Claims/Offers bleiben 1:1, nur die Sprache ändert sich. Offene Punkte intern (ClickUp/Chat) tracken, nicht im Dokument.

---
<sub>**ADMKRS Creative Suite** · © ADMKRS GmbH, München · v1.12.0 · interner Gebrauch · gleiche Builder-Engine & B4-Standard wie `admkrs-cs-creative-briefing`.</sub>
