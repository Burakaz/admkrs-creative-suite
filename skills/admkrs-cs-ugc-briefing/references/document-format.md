# Dokument-Format — UGC-Briefing JSON, Builder & Skelett

Das UGC-Briefing wird aus einer **JSON-Spec** gerendert. Builder: `assets/build_briefing.js` (Node + `docx`) — **identische Engine wie `admkrs-cs-creative-briefing`**, gleicher ADMKRS-Stil, gleiches **B4 Querformat / 1 cm Ränder**. Inhalt füllen, Builder laufen lassen, fertig.

**Vorgehen:** Nimm `examples/example_ugc_briefing.json` als Muster — Struktur kopieren, Inhalt ersetzen. Nicht von Null bauen.

---

## Builder ausführen

```bash
cd <skill>/assets && npm install docx        # einmalig pro Umgebung
node <skill>/assets/build_briefing.js <input.json> <YYMMDD_BRAND_Product_UGC_LANG.docx>
```

Wird der Output-Name weggelassen, nimmt der Builder das Feld `filename` aus der JSON (Konvention `YYMMDD_BRAND_Product_UGC_LANG`, Sprache am Ende: DE/EN/NL/FR/AT). Danach das .docx mit `present_files` zeigen. **Best Practice (Cowork mit verbundener Drive):** das fertige .docx in **Google Drive** im Kunden-Ordner unter **„Briefings"** ablegen (Name nach Konvention) — **nicht** ungefragt in Slack/ClickUp posten; Speichern in der Kunden-Drive ist ok. Optionaler Render-Check: docx → PDF → JPEG via LibreOffice (`skills/docx/scripts/office/soffice.py --convert-to pdf`, dann `pdftoppm -jpeg`).

**Seite:** B4 Querformat (ISO B4, 250×353 mm, Landscape), 1 cm Ränder — ADMKRS-Standard für *alle* erzeugten Dokumente (fest im Builder).

---

## Inline-Markup (in jedem Textfeld)
`<b>fett</b>` · `<i>kursiv</i>` · `\n` neue Zeile in Zelle, Absatz **oder Callout**. Literale `*`, `·`, „Anführungszeichen" bleiben unverändert (Sternchen-Disclaimer wie `*pro Portion` einfach so schreiben). **Kein langer Gedankenstrich „—"** in produzierter Copy (Hausregel) — Punkt/Komma, notfalls „–".

**Zeile für Zeile, nie als Block (Pflicht):** Aufzählungen, mehrere Anweisungen, mehrere Fakten — je Punkt eine `\n`-Zeile, in Zellen wie in Callouts. Ein „1) … 2) … 3) …"-Fließtext-Block ist falsch.

---

## Top-Level

```json
{
  "filename": "260607_NOVA_ProteinCoffee_UGC_DE",
  "header": {
    "eyebrow": "UGC Creator Briefing",
    "title": "NOVA · Protein Coffee — UGC",
    "dek": "3 Konzepte · 9 Hooks · drehfertige Scripts · Stand 07.06.2026"
  },
  "blocks": [ /* Reihenfolge = Dokument-Reihenfolge */ ]
}
```

## Block-Typen (wie admkrs-cs-creative-briefing)

`h1`/`h2`/`h3` (Überschriften) · `label` (graue Kursiv-Zeile unter h2) · `lede` (fetter Intro-Satz) · `p` (Absatz, `\n` für Zeilen) · `callout` (**mehrzeilig**, jede `\n`-Zeile = eigener Absatz; `variant`: `"locked"`=lavendel \| `"anchor"`=creme+Gold \| `"todo"`=warm/„Vor Produktion klären"; Felder `lead`, `text`) · `table` (`layout`: `headerrow` \| `keyvalue` \| `hooks`) · `outro` (fette Lead-In + Text) · `spacer` · `divider`.

**Tabellen-Layouts:**
- `headerrow` — schwarze Kopfzeile + Zeilen. `header`, `rows`, `widths` (relative Gewichte), `style` `"plain"`/`"zebra"`, optional `colAligns`, `colItalics` (z. B. VO-Spalte kursiv).
- `keyvalue` — schwarze Label-Spalte links, Wert rechts. `rows`: `[["Format","…"], …]`, `widths` default `[1, 3.2]`.
- `hooks` — schmale graue Buchstaben-Spalte (A/B/C) + Hook-Text. `rows`: `[["A","…"], …]`, `widths` default `[0.7, 9]`.

**Spaltenbreiten-Tipp:** erste Spalte (Index/Zeit/Label) breit genug, dass das längste Label nicht mitten im Wort umbricht.

---

## UGC-Briefing-Skelett (Dual-Purpose)

Die Reihenfolge setzt **Brand-Foundation (Creator+Kunde) → Strategie (Kunde) → Standards (Creator) → Konzepte mit Scripts → Out-of-the-box-Layer → Test-/Delivery-Plan.** Details je Block: `brand-foundation.md`.

```
header (eyebrow "UGC Creator Briefing", title, dek)
lede  (1 Positionierungssatz)
callout todo  "Vor Produktion klären (blockiert sonst alles): …"   ← offene Punkte gebündelt, ganz oben (Zahlen, Casting, Rechte, Kennzeichnung, Deadline)

h1 "Brand auf einen Blick"
  table keyvalue  [Marke | Kategorie | Produkt | Was es ist | Ton | Was die Brand NICHT ist | Offer/Code]

h1 "Produkt-Facts & USPs"
  table headerrow/plain  [Fact | Warum es zählt / wie im Video nutzbar]
  callout locked  "Gesperrt 1:1: …"   (Zahlen, Claims, Disclaimer, Code)

h1 "Wen wir ansprechen"
  p  (konkrete Persona — Name, Alltag, Trigger, Einwand)
  table keyvalue  [Persona | Awareness | Trigger-Moment | Vorerfahrung | Einwand | Kauf-Ort]

h1 "Strategische Grundlage"        ← Client-Layer (das Warum)
  p  (Awareness · Funnel · Angle-Logik · Hypothese)
  table headerrow/zebra  [Konzept | Angle | Framework | Awareness | Hypothese]

h1 "Wie wir filmen — Standards"     ← Creator-Layer
  table keyvalue  [Ratio | Länge | Hooks | Rohmaterial | Captions | Licht | Ton | Setting | Edit | Dateiname]
  callout anchor  "Performance-Regeln. …"
  callout locked  "Kennzeichnung & Claims. …"   (→ admkrs-cs-ad-compliance-check)

h1 "Konzept 1 · [Title]"            ← pro Konzept ein Set (Creator+Kunde)
  label "[Angle / Family]"
  table keyvalue  [Format | Angle | Framework | Awareness | Zielperson | Setting | Sound]
  callout anchor  "Strategischer Anker. … + Hypothese."
  h3 "3 Hooks · zum Scroll-Stop-Test"
  table hooks  [A, B, C]
  h3 "Script · Time-coded (drehfertig)"
  table headerrow/zebra  [Zeit | Bild / Action | On-Screen Text | Gesprochen (VO)]   (colItalics: [false,false,false,true])
  p  "<i>Regie-Notiz: …</i>"
  outro "CTA / Outro. …"
  … (Konzept 2, Konzept 3)

h1 "Out-of-the-box-Layer · Scroll-Breaker"   ← der dedizierte „nicht-Standard"-Layer
  p  (Intro)
  table headerrow/zebra  [Idee | Format | Warum es teilt | Wofür]

h1 "Test- & Delivery-Plan"
  table headerrow/plain  [Was | Detail]   (Hook-Varianten, Rohmaterial, Deadline, Naming, Freigabe)
```

**Script-Spalten:** `widths` ca. `[0.9, 3.4, 2.2, 3.0]`, `colAligns` `["center","left","left","left"]`, `colItalics` `[false,false,false,true]` (VO kursiv). Hook-Zeile: On-Screen = `<b>HOOK</b>`, VO = `"[ Hook · A/B/C ]"`.

---

## Struktur-Regeln — zeilenweise & final

- **Zeile für Zeile, kein Block.** Aufzählungen/mehrere Fakten je `\n`-Zeile, in Zellen wie in Callouts.
- **Offene Punkte gebündelt nach oben** in **einen** `todo`-Callout („Vor Produktion klären …"), nummeriert, zeilenweise. Schließt mit: „Keine neuen Zahlen erfinden – fehlende Werte als Platzhalter an ADMKRS zurück." Nicht in die Build-Zellen verstreuen.
- **Final entscheiden, ein konkreter Fakt statt Floskel**, Platzhalter (`[Platzhalter: …]`) statt geraten. (UGC ist dual-purpose: Strategie-Layer für den Kunden bleibt — anders als bei den schlanken Motion-/Static-Designer-Dokumenten.)

---

## Locked-Facts im Dokument
**Gesperrt 1:1** (Locked-Callout) hält fest, was unverändert bleibt (Zahlen, Claims, Disclaimer, Code, Review-Wortlaut). **[Ergänzung]** markiert jeden neuen Fakt/Vorschlag, der Freigabe braucht — im Text als `<b>[Ergänzung]</b>`. Disclaimer/Sternchen exakt übernehmen.

---
<sub>**ADMKRS Creative Suite** · © ADMKRS GmbH, München · v1.5.0 · interner Gebrauch · erstellt von ADMKRS. Gleiche Builder-Engine & B4-Standard wie admkrs-cs-creative-briefing.</sub>
