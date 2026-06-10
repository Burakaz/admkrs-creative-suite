# Dokument-Format — JSON-Schema, Builder & Design-Tokens

Das Briefing wird aus einer **JSON-Spec** gerendert. Der Builder (`assets/build_briefing.js`, Node + `docx`) erzeugt das .docx im exakten ADMKRS-Stil. Inhalt füllen, Builder laufen lassen, fertig — die Optik ist fest verdrahtet, du kümmerst dich nur um den Inhalt.

**Vorgehen:** Nimm die passende Vorlage aus `examples/` (`example_statics_briefing.json` oder `example_motion_briefing.json`), kopiere die Struktur, ersetze den Inhalt. Nicht von Null bauen.

---

## Builder ausführen

```bash
cd <skill>/assets && npm install docx        # einmalig pro Umgebung
node <skill>/assets/build_briefing.js <input.json> <OUTPUT.docx>
# Output-Name = Dateiname-Konvention YYMMDD_BRAND_Product_Type_LANG (Sprache am Ende: DE/EN/NL/FR/AT):
# node assets/build_briefing.js briefing.json 260608_NOVA_ProteinCoffee_Statics_DE.docx
```

Wird `OUTPUT.docx` weggelassen, nimmt der Builder das Feld `filename` aus der JSON. Danach das .docx dem User mit `present_files` zeigen.

**Best Practice (Cowork mit verbundener Drive):** Das fertige .docx in **Google Drive** im Ordner des jeweiligen Kunden unter **„Briefings"** ablegen (Dateiname nach Konvention `YYMMDD_BRAND_Product_Type_LANG`) — statt es nur lokal liegen zu lassen. **Nicht** ungefragt in Slack/ClickUp posten; Speichern/Verschieben in der Kunden-Drive ist ok.

Optionaler Render-Check (Optik verifizieren): docx → PDF → JPEG via LibreOffice (`skills/docx/scripts/office/soffice.py --convert-to pdf`, dann `pdftoppm -jpeg`).

---

## Inline-Markup (in jedem Textfeld erlaubt)

- `<b>fett</b>` — Bold. `<i>kursiv</i>` — Italic. Verschachtelbar: `<b><i>…</i></b>`.
- `\n` — neue Zeile innerhalb einer Zelle, eines Absatzes **oder Callouts**.
- **Zeile für Zeile, nie als Block (Pflicht):** Jede Aufzählung, jeder eigenständige Gedanke, jede einzelne Anweisung kommt auf eine **eigene Zeile** (`\n`). Niemals mehrere nummerierte/aufgezählte Punkte in einen Fließtext-Block packen — ein „1) … 2) … 3) …"-Absatz ist falsch, je Punkt eine `\n`-Zeile ist richtig. Gilt für Zellen **und** Callouts.
- Literale `*`, `·`, „Anführungszeichen" bleiben unverändert (kollidieren **nicht** mit dem Markup — Sternchen-Disclaimer wie `*pro 30g Pulver` einfach so schreiben). **Kein langer Gedankenstrich „—"** in produzierter Copy (ADMKRS-Hausregel) — stattdessen Punkt/Komma, notfalls das kurze „–".

---

## Top-Level-Struktur

```json
{
  "filename": "260605_NOVA_Coffee_Whey_Statics_DE",
  "header": {
    "eyebrow": "Motion Concepts V5",          // optional, wird GROSS gesetzt (Kicker über dem Titel)
    "title": "NOVA · Protein Coffee — Statics",  // großer Titel
    "dek": "Creative Upgrade  ·  5 Statics  ·  Stand 05.06.2026"  // optional Untertitel-Zeile
  },
  "blocks": [ /* Reihenfolge = Dokument-Reihenfolge */ ]
}
```

---

## Block-Typen

| `type` | Zweck | Felder |
| --- | --- | --- |
| `h1` | Sektions-Überschrift („Strategie-Layer", „Briefing", „Overview", „B-Block …") | `text` |
| `h2` | Konzept-Überschrift („BM-01 · Sweet Without the Sugar — Crunch") | `text` |
| `h3` | Unter-Überschrift („3 Hooks · for scroll-stop testing", „Storyboard · Time-coded") | `text` |
| `label` | kleine kursive graue Zeile unter h2 (Family-Label, z. B. „Crunch") | `text` |
| `lede` | fetter Intro-Satz | `text` |
| `p` | normaler Absatz (Intro-/Erklärtext), `\n` für Zeilen | `text` |
| `callout` | farbiger Hinweis-Block, **mehrzeilig** (jede `\n`-Zeile = eigener Absatz) | `variant` (`"locked"`=lavendel \| `"anchor"`=creme+Gold \| `"todo"`=warm/„Vor Produktion klären"), `lead`, `text` |
| `table` | Tabelle (siehe Layouts) | `layout`, `style`, `widths`, `header`, `rows`, `colAligns`, `colItalics` |
| `outro` | fette Lead-In-Zeile + Text (Motion/Video-Outro) | `lead`, `text` |
| `spacer` | vertikaler Abstand | `size` (optional) |
| `divider` | dünne Trennlinie | — |

### Tabellen-Layouts (`table.layout`)

- **`headerrow`** — schwarze Kopfzeile + Datenzeilen. Für Briefing-Tabelle, Overview, Storyboard.
  - `header`: `["Spalte1", …]`
  - `rows`: `[ ["Zelle1", …], … ]` (Zellenanzahl = Spaltenanzahl)
  - `widths`: relative Gewichte je Spalte, z. B. `[1, 1.6, 1.7]` (werden auf die Seitenbreite skaliert)
  - `style`: `"plain"` (alle Zeilen weiß) oder `"zebra"` (jede 2. Zeile leicht grau)
  - `colAligns` (optional): `["center","left",…]` je Spalte
  - `colItalics` (optional): `[false,…,true]` — z. B. Voice-Over-Spalte kursiv
- **`keyvalue`** — linke Spalte = schwarze Label-Spalte, rechts Wert. Für Motion/Video-Property-Table.
  - `rows`: `[ ["Format","…"], ["Specific Offer","…"], … ]`
  - `widths` (optional): default `[1, 3.2]`
- **`hooks`** — schmale, grau hinterlegte Buchstaben-Spalte (A/B/C) + Hook-Text.
  - `rows`: `[ ["A","…"], ["B","<b>…</b>"], ["C","<b>…</b>"] ]`
  - `widths` (optional): default `[0.7, 9]`

**Spaltenbreiten-Tipp:** Die erste Spalte (Index/Static-Nr. + Kurzlabel) so breit wählen, dass das längste Label nicht mitten im Wort umbricht — bei langen Labels wie „Comparison“ Gewicht ~1,2 statt 1,0. Kurze Labels („Iced Coffee“) brauchen weniger. Lieber das Label kurz halten *und* die Spalte passend dimensionieren.

---

## Skelett je Briefing-Typ

**Statics / Carousel (Designer-Dokument — schlank, build-fertig):**
```
header (title, dek)
callout todo    "Vor Produktion klären (blockiert sonst alles): …"   ← offene Punkte gebündelt, ganz oben
table keyvalue  "Auf einen Blick"  [Ziel | Zielgruppe | Formate | Deadline | Wichtige Infos]   ← Pflicht
callout anchor  "Strategischer Anker. …"   ← die EINE strategische Idee, 1–2 Zeilen (keine Hebel-Tabelle)
callout locked  "Gesperrt 1:1: …"
p  "<b>Fett = landet auf dem Creative.</b> Alles andere ist Anweisung/Kontext."   ← Lese-Konvention, direkt über der Tabelle
h1 "Briefing"
table headerrow/plain  [# | Dateiname | Produkt | Creative Format | Hook | Subline | USPs / Badge | Disclaimer | Visual-Direction]
```

**„Auf einen Blick" (Pflicht-Block in jedem Designer-Briefing):**
- **Ziel** — was das Set erreichen soll (z. B. „Prospecting cold · CVR-Fokus", „Retargeting · Offer-Push").
- **Zielgruppe** — 1 Zeile, konkret (wer ist die Person, nicht Demografie-Salat).
- **Formate** — **Meta-Standard: 4:5 (1080×1350) und 9:16 (1080×1920). Kein 1:1 mehr für Meta-Briefings.** Sonderformate (andere Plattformen) immer **extra mit Plattform + Format + Pixeln** angeben (z. B. „Pinterest: 2:3 · 1000×1500").
- **Deadline** — Datum; fehlt es: `[Platzhalter: Deadline]` + ab in den todo-Callout.
- **Wichtige Infos** — zeilenweise, nur was die Produktion wirklich braucht.

**Bold-Konvention (Pflicht):** **Alles, was fett (`<b>`) geschrieben ist, landet als Text auf dem Creative.** Hook, Subline, USPs/Badge, Disclaimer-Wortlaut → fett. Anweisungen, Kontext, Visual-Direction → nicht fett. Die Konvention steht als `p`-Zeile direkt über der Briefing-Tabelle im Dokument.

**Briefing-Tabelle — Spalten (Statics):**

| Spalte | Inhalt |
| --- | --- |
| `#` | Creative-Nummer (1, 2, 3 …) |
| `Dateiname` | nach Naming-Convention des Kunden, sonst ADMKRS-Stil |
| `Produkt` | kurze Produktbezeichnung (z. B. „Schokoriegel", „Protein Butter Cups") |
| `Creative Format` | der Ad-Style aus der Style-Bibliothek (`creative-formats.md`): z. B. Vorher/Nachher, Product Features, USP Ad, 3 Reasons Why, Us vs Them, Review, Lifestyle, Organic Screen, Native Ad, Problem/Solution, Product-Hero … |
| `Hook` | die Headline — **fett** (landet auf dem Creative) |
| `Subline` | die Klammer-Auflösung zum Hook — **fett** |
| `USPs / Badge` | **optional** — nur wenn hier Text aufs Creative kommt UND relevant; **fett**, zeilenweise |
| `Disclaimer` | **optional** — klein aufs Creative, nur falls vorhanden & wichtig; **fett** |
| `Visual-Direction` | **frei halten:** Inspos, Stimmung, Referenzen — **keine Formatangaben** (stehen oben), **keine Farben**, keine Pixel-Vorgaben. Designer kreativ arbeiten lassen. Ausnahme: es gibt eine klare Kunden-Vorgabe, dann steht sie hier. |

- **Optionale Spalten (`USPs / Badge`, `Disclaimer`) nur aufnehmen, wenn mindestens ein Creative im Set sie braucht** — sonst Spalte ganz weglassen (kein „–"-Friedhof).
- Jede Zelle **zeilenweise** (`\n`), keine Prosa-Blöcke.
- **Keine `Strategie-Layer`-Tabelle** mehr im Designer-Dokument — die Hebel-/Warum-Analyse bleibt im Strategie-Pass (Chat), im Dokument steht nur der Anker.
- Carousel: letzte Tabelle = `[Card | Visual | On-Card Text | Zweck]`, Card 1 = Standalone-Hook, letzte Card = CTA.

**Motion / Video (pro Konzept ein Block-Set):**
```
header (eyebrow, title, dek)
lede + p   (kurzer Intro)
callout todo   "Vor Produktion klären (blockiert sonst alles): …"   ← offene Punkte gebündelt, ganz oben
table keyvalue  "Auf einen Blick"  [Ziel | Zielgruppe | Formate | Deadline | Wichtige Infos]   ← Pflicht (Formate: 4:5 + 9:16 Meta-Standard, kein 1:1; Sonderformate mit Plattform + Pixel)
h1 "Overview"
table headerrow/zebra  [# | Title | Family | Offer | Length]
h1 "B-Block — …"   p (italic Intro)
  h2 "BM-01 · …"
  label "Family"
  table keyvalue  [Format, Specific Offer, Target Audience, Voice-Over Direction, Music / Sound]
  callout anchor  "Strategic anchor. …"
  h3 "3 Hooks · for scroll-stop testing"
  table hooks  [A,B,C]
  h3 "VO-Script (Spine) · am Stück"        ← VO-FIRST: führt, kommt VOR dem Storyboard
  p  "<das komplette gesprochene VO als ein zusammenhängender Take, \n je Beat eine Zeile>"
  h3 "Storyboard · Time-coded"   (Video: "Script · Time-coded")
  table headerrow/zebra  [Time | Visual | On-Screen Text | Voice-Over]
  outro "Outro. …"
  … (nächstes Konzept)
```

> **VO-First (Pflicht-Vorgehen).** Pro Motion-/Video-Konzept ist das **„VO-Script (Spine)"** das **führende Element**: ein `h3` „VO-Script (Spine)" + ein `p`-Block mit dem **kompletten gesprochenen VO am Stück** (je Beat eine Zeile via `\n`) — **vor** dem time-coded Storyboard. Schreib das VO zuerst und durchgehend, sodass es sich als **ein** natürlicher Take liest; **dann** mappt das Storyboard `Time · Visual · On-Screen-Text` **auf die VO-Beats** (die Voice-Over-Spalte im Storyboard wiederholt die Beats des Spine, zerlegt nach Zeit).
>
> **Redefluss, kein Stakkato:** Der Spine liest sich von oben nach unten als zusammenhängender, natürlich gesprochener Monolog (Bindeglieder, „du"-Ansprache, Hook 0–2 s → Spannung → Auflösung → CTA). Jede Zeile knüpft an die vorige an. On-Screen-Text darf knapp/Schlagwort sein, das gesprochene VO nie. Schreibregeln: `creative-formats.md` §5b · Vorher/Nachher: `copywriting-frameworks.md` §4b. *(Kein Builder-Eingriff nötig — `h3`+`p` sind Standard-Blöcke.)*

---

## Struktur-Regeln — zeilenweise, Designer-tauglich, finale Briefings

Ein Briefing ist eine Bau-Anweisung, kein Strategie-Essay. Es muss so klar sein, dass ein Designer oder Editor es **ohne Rückfrage** umsetzen kann.

- **Zeile für Zeile, kein Block.** Aufzählungen, mehrere Anweisungen, mehrere Fakten: je Punkt eine `\n`-Zeile — in Zellen wie in Callouts. Ein dichter Absatz mit „1) … 2) … 3) …" ist ein Fehler.
- **Nur was beim Bauen hilft.** In Motion-/Static-Designer-Dokumenten kommt rein, was Bild, Text, Layout, Specs, VO oder Schnitt betrifft. Strategie steckt im **einen** `anchor`-Callout (1–2 Zeilen), nicht in einer Hebel-/Analyse-Tabelle. Audience-Psychografik, Awareness-Theorie, Test-Hypothesen-Prosa gehören nicht ins Designer-Dokument (UGC-Briefing ist die Ausnahme: dual-purpose für Creator **und** Kunde).
- **„Auf einen Blick" ist Pflicht.** Jedes Designer-Briefing trägt oben Ziel · Zielgruppe · Formate · Deadline · Wichtige Infos als keyvalue-Tabelle.
- **Format-Regel (Meta):** Standard ist **4:5 + 9:16. Kein 1:1 mehr in Meta-Briefings.** Sonderformate für andere Plattformen immer extra mit **Plattform + Format + Pixeln**. Formatangaben stehen NUR im „Auf einen Blick", nie in den Visual-Direction-Zellen.
- **Bold-Konvention:** **fett = landet auf dem Creative.** Hook/Subline/USPs/Disclaimer-Wortlaut fett, alles andere nicht. Konvention als `p`-Zeile über der Tabelle ausweisen.
- **Visual-Direction frei halten.** Inspos, Stimmung, Referenzen — keine Formatangaben, keine Farben, keine Pixel-Maße. Designer sollen kreativ arbeiten. Nur bei klarer Kunden-Vorgabe wird sie hier festgeschrieben.
- **Final entscheiden, nicht abwägen.** Build-Zellen enthalten Entscheidungen, keine offenen Fragen und kein „evtl./oder vielleicht". Beispiel: „Initiale im Kreis, kein KI-Gesicht" statt „KI-Frau geblurrt, könnte fake wirken".
- **Ein konkreter Fakt statt Floskel.** Keine generischen Badges doppeln („Geschmack, der für sich spricht" 3× im Set). Je Slide/Static **ein** konkreter, freigegebener Fakt („1,5 g Zucker pro Riegel", „max. 84 kcal pro Tüte"). Info statt Floskel = weniger salesy.
- **Offene Punkte gebündelt nach oben (`todo`-Callout).** Alle Blocker/Rückfragen in **einen** `todo`-Callout ganz oben („Vor Produktion klären (blockiert sonst alles):"), nummeriert, zeilenweise — nicht verstreut in die Build-Zellen. Schließt immer mit: „Keine neuen Zahlen erfinden – fehlende Werte als Platzhalter an ADMKRS zurück."
- **Platzhalter statt Erfindung.** Fehlt ein Wert, schreib `[Platzhalter: …]` und nimm ihn in den `todo`-Callout auf — niemals raten oder Zahlen erfinden.

---

## Design-Tokens (fest verdrahtet — nur zur Orientierung)

Aus den Referenzdokumenten 1:1 übernommen. **Nicht** im Inhalt überschreiben — der Builder setzt sie.

| Element | Wert |
| --- | --- |
| Font | Arial |
| Tabellen-Header-Fill | `#0A0A0A` (schwarz), Text `#FFFFFF` |
| Body-Text | `#1A1A1A`, ~9 pt in Tabellen |
| Zebra-Zeile | `#F4F4F4` |
| Hooks-Buchstaben-Spalte | `#F1F1F1` |
| Gitterlinien | `#D9D9D9` |
| Locked-Callout (lavendel) | Fill `#ECEAF6`, Balken `#B9AEDB` |
| Anchor-Callout (creme) | Fill `#FFF7DE`, Goldbalken `#E8B923` |
| Dek / Eyebrow / Label-Grau | `#5F5F5F` / `#6B6B6B` / `#8A8A8A` |
| Seite | **B4 Querformat** (ISO B4, 250×353 mm, Landscape), **1 cm Ränder** — ADMKRS-Standard für *alle* erzeugten Dokumente |

---

## Locked-Facts im Dokument

- **Gesperrt 1:1** (Locked-Callout) immer im Strategie-Layer: hält fest, was unverändert bleibt (Zahlen, Health Claims, Sternchentexte, Review-Wortlaut, Dateinamen).
- **[Ergänzung]** markiert jeden *neuen* Fakt/Vorschlag, der noch Freigabe braucht (z. B. eine zusätzliche Zahl, ein neues Offer). Im Text als `<b>[Ergänzung]</b>` oder `<i>[Ergänzung]</i>` setzen.
- Disclaimer/Sternchen exakt übernehmen (`*pro 30g Pulver`).
