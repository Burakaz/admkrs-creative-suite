# Dokument-Format - Lokalisierungs-Briefing (verbindlich)

Gerendert über die **gemeinsame Builder-Engine** `../admkrs-cs-creative-briefing/assets/build_briefing.js` (Node + `docx`). **Keine neue Renderlogik**, gleicher Haus-Stil: B4 Querformat, 1 cm Ränder, schwarze Tabellen-Header, Arial, Zebra, Design-Tokens. Du füllst nur den Inhalt.

**Vorgehen:** Nimm `examples/localization_statics_example.json` bzw. `examples/localization_motion_example.json` als Muster, Struktur kopieren, Inhalt ersetzen. Nicht von Null bauen.

---

## Builder ausführen

```bash
cd <skill>/../admkrs-cs-creative-briefing/assets && npm install docx   # einmalig pro Umgebung
node build_briefing.js <absoluter Pfad zu input.json> <YYMMDD_BRAND_Product_Type_LANG.docx>   # aus demselben assets/-Ordner heraus
```

Wird der Output-Name weggelassen, nimmt der Builder das Feld `filename` aus der JSON. **Dateiname-Konvention:** `YYMMDD_BRAND_Product_Type_LANG` - die **Zielsprache** steht am Ende (`NL`, `FR`, `ES`, `IT` …). Danach das .docx mit `present_files` zeigen. **Best Practice (Cowork mit Drive):** das fertige .docx in der Kunden-Drive unter „Briefings" ablegen, nicht ungefragt in Slack/ClickUp posten.

Render-Check (Pflicht bei Lokalisierung): docx → PDF → JPEG (LibreOffice `--convert-to pdf`, dann `pdftoppm -jpeg`). **Sonderzeichen prüfen** (ä/ö/ü/é/è/ï/ç/„"/·/…) und Seiten-Fit.

---

## 1 - Sprache der Struktur (Kernregel)

**Alle** Labels, Header, Spaltennamen und Notizen sind **ENGLISCH** - internationale Teams arbeiten daran. Nur die **Copy-Zellen** tragen DE-Original und Zielsprache.

## 2 - Kopf (`header` + erste Blocks)

- `eyebrow`: `LOCALIZATION: ORIGINAL → TRANSLATION`
- `title`: `{Brand} {Product}, DE → {LANG}` (Kommas statt „·", wie das Beispiel-JSON: „NOVA Sommermärchen-Bundle, DE → NL")
- `dek`: `{scope, z. B. 3 Statics + 1 Motion Ad}, {Market}, {Date}, Draft` (Kommas, kein „·"-Trenner)
- `p` **Glossary anchors:** eine Zeile mit den genutzten bindenden Mappings, z. B. `Glossary anchors: 97% weniger Zucker → 97% minder suiker, Disclaimer → official NL wording (below).`
- **Keine Legend-Zeile im Dokument** (Suite-Standard): weder Bold-Erklärung noch „use 1:1 / do not re-translate"-Anweisungen. Die Verbindlichkeit der Übersetzungen sichern **Glossar + Abnahme** (`admkrs-cs-creative-verifier`), nicht ein Hinweistext im Dokument.

## 3 - „At a glance" (Pflicht, direkt nach dem Kopf)

`table` · `layout: "keyvalue"` · `widths: [1, 4.2]` - englische Labels, **vor** der Vergleichs- bzw. Motion-Tabelle. Nur Zeilen mit echter Info: fehlt ein Wert, **im Intake beim Ersteller nachfragen**; bleibt er offen → Zeile weglassen und den Punkt intern (ClickUp/Chat) klären. Kein Platzhalter.

- **Scope** - Deliverables als explizite Zählung, z. B. `1 offer static, 2 formats = 2 assets` (Motion zusätzlich mit Länge: `length as DE master, 15 s`).
- **Source files** - Link zu den DE-Master-Design-Files (Figma/PSD, Packshots, Fonts; bei Motion das AE-/Schnitt-Projekt). Der häufigste Produktionsblocker jedes internationalen Teams: **im Intake aktiv erfragen.**
- **Formats** - `Meta standard: 4:5 (1080×1350) and 9:16 (1080×1920).` Oder `same as DE master`, wenn die lokalisierten Assets die Master-Formate 1:1 übernehmen.
- **Deadline** - Datum.
- **Delivery** - Lieferort (Ordner/Tool) + Export-Naming der lokalisierten Assets: Name des DE-Masters + Sprach-Suffix (`_NL`, `_FR` …).

## 4 - Statics / Carousel: Vergleichstabelle

`table` · `layout: "headerrow"` · `style: "plain"` · `widths: [1.25, 0.95, 2.5, 2.5]` · `colAligns: ["left","left","left","left"]`
- `header`: `["Asset", "Element", "Original (DE)", "Translation ({LANG})"]`
- Pro Asset Zeilen für `Hook`, `Subline`, `Badges`, `CTA` (nur, was existiert). **Asset-Name nur in der ersten Zeile der Gruppe**, danach leer (`""`).
- **Translation-Zellen `<b>fett</b>`** (= landet aufs Creative). Original-Spalte regular (Referenz).
- Disclaimer als Fußnote **unter** der Tabelle: `h3 "Disclaimer (all assets)"` + `p` mit `DE: …` und `{LANG}: <b>…</b> (official glossary wording)`.

## 5 - Motion / Video: NUR zwei Spalten (vereinfacht, wichtig)

`table` · `layout: "headerrow"` · `style: "zebra"` · `widths: [1, 1.4]` · `colItalics: [false, true]`
- `header`: `["On-Screen Text", "Voice-Over"]`
- **Eine Zeile pro Beat. KEINE Timecode-Spalte. KEINE getrennten Hook-/CTA-Zeilen.**
- **On-Screen-Box** = alles, was eingeblendet wird (Hook, Badges, Offer, CTA, Disclaimer), zusammen in **eine** Zelle, `<b>fett</b>`.
- **Voice-Over-Spalte** = der gesprochene Satz, **kursiv** (regelt `colItalics`).
- Inhalt in der **Zielsprache** (build-ready). DE-Quelle ist optional: nur auf Wunsch als kleine Referenz-Tabelle darüber. **Default ist die saubere 2-Spalten-Zielversion.**

## 6 - Adaptation & Compliance: Note am Ende

`callout` · `variant: "todo"` · `lead: "Adaptation & Compliance"` - **deklarierte Ausnahme** von der Suite-Regel „keine Callouts im Produktionsdokument": das internationale Team kennt den DE-Kontext nicht, die getroffenen Adaptions-Entscheidungen und Markt-Flags sind Bau-Wissen und haben in der Vergleichstabelle keinen Platz. Inhalt **ausschließlich build-relevant**:
- **getroffene** kulturelle Adaptions-Entscheidungen (z. B. Reframing „Sommermärchen" → „Oranjezomer"),
- Markt-Compliance-Flags als Bau-Anweisung (z. B. „oranje" nur als Farbe/Sommer-Vibe, keine KNVB-/Team-/Spieler-Referenzen).

**Nicht in den Callout, nicht ins Dokument:** offene Glossar-Konflikte, `[Addition]`-Vorschläge, Fragen „zur Klärung". Offene Punkte leben im internen Prozess (ClickUp/Chat). Ungeklärter Begriff: klären oder die betroffene Zeile/das Asset zurückhalten (analog Platzhalter-Regel). Was im Dokument steht, ist entschieden und freigegeben.

## 7 - Stil

Translation-Copy fett, Labels/Quelle regular, VO kursiv. Kompakt halten (Tabelle möglichst eine Seite). **Kein „—" in der Copy** (Hausregel).

---

## Inline-Markup & die Mehrzeilen-Bold-Regel (Pflicht)

`<b>fett</b>` · `<i>kursiv</i>` · `\n` = neue Zeile in der Zelle. Literale `*` und „Anführungszeichen" bleiben unverändert. **Kein „·" als Trenner** im Dokument-Inhalt (dek, Zellen, Absätze) - der Mittelpunkt macht Probleme beim Übernehmen in andere Programme; Kommas oder `\n`-Zeilen nutzen.

**Mehrzeilige On-Creative-Zellen: jede Zeile einzeln in `<b>…</b>` wickeln.** Der Builder trägt ein `<b>` **nicht** über `\n` hinweg, nur die erste Zeile bliebe fett. Also:
- ✗ `"<b>-15% ALLEEN T/M ZONDAG\n97% minder suiker*\nLIMITED EDITION</b>"` (nur Zeile 1 wird fett)
- ✓ `"<b>-15% ALLEEN T/M ZONDAG</b>\n<b>97% minder suiker*</b>\n<b>LIMITED EDITION</b>"`

Gilt für Badge-Stapel (Statics) und die On-Screen-Box (Motion), wann immer mehrere Zeilen aufs Creative gehen.

---

## Block-Typen (wie creative-briefing)

`h1`/`h2`/`h3` · `label` · `lede` · `p` (`\n` für Zeilen) · `table` (`headerrow` · `keyvalue` · `hooks`) · `callout` (`todo`/`anchor`/`locked`) · `spacer` · `divider`. Für die Lokalisierung gebraucht: `p`, `h3`, `table keyvalue` (At a glance), `table headerrow`, `callout todo`.

**Tabellen-Felder:** `header`, `rows` (Zellenzahl = Spaltenzahl), `widths` (relative Gewichte), `style` `"plain"`/`"zebra"`, optional `colAligns`, `colItalics`.

---

## Platzhalter & nichts erfinden

Fehlt ein freigegebener Wert: **beim Ersteller nachfragen**; bleibt er offen → Zeile/Asset weglassen bzw. das betroffene Konzept zurückhalten - **kein `[Placeholder: …]` im ausgelieferten Dokument.** Ungesicherte Zielbegriffe (kein Glossar-Match) **intern flaggen** (ClickUp/Chat) + Native-Review vor Abgabe empfehlen - nicht als offene Frage ins Dokument. Zahlen/Claims/Offers bleiben 1:1, nur die Sprache ändert sich. Offene Punkte intern (ClickUp/Chat) tracken.

---
<sub>**ADMKRS Creative Suite** · © ADMKRS GmbH, München · v1.13.0 · interner Gebrauch · gleiche Builder-Engine & B4-Standard wie `admkrs-cs-creative-briefing`.</sub>
