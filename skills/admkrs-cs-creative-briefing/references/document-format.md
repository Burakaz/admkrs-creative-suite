# Dokument-Format - JSON-Schema, Builder & Design-Tokens

Das Briefing wird aus einer **JSON-Spec** gerendert. Der Builder (`assets/build_briefing.js`, Node + `docx`) erzeugt das .docx im exakten ADMKRS-Stil. Inhalt füllen, Builder laufen lassen, fertig - die Optik ist fest verdrahtet, du kümmerst dich nur um den Inhalt.

**Vorgehen:** Nimm die passende Vorlage aus `examples/` (`example_statics_briefing.json` oder `example_motion_briefing.json`), kopiere die Struktur, ersetze den Inhalt. Nicht von Null bauen.

---

## Builder ausführen

```bash
cd <skill>/assets && npm install docx        # einmalig pro Umgebung
node <skill>/assets/build_briefing.js <input.json> <OUTPUT.docx>
# Output-Name = Dateiname-Konvention YYMMDD_BRAND_Product_Type_LANG (Sprache am Ende: DE/EN/NL/FR/AT):
# node <skill>/assets/build_briefing.js briefing.json 260608_NOVA_ProteinCoffee_Statics_DE.docx
```

Wird `OUTPUT.docx` weggelassen, nimmt der Builder das Feld `filename` aus der JSON. Danach das .docx dem User mit `present_files` zeigen.

**Best Practice (Cowork mit verbundener Drive):** Das fertige .docx in **Google Drive** im Ordner des jeweiligen Kunden unter **„Briefings"** ablegen (Dateiname nach Konvention `YYMMDD_BRAND_Product_Type_LANG`) - statt es nur lokal liegen zu lassen. **Nicht** ungefragt in Slack/ClickUp posten; Speichern/Verschieben in der Kunden-Drive ist ok.

Optionaler Render-Check (Optik verifizieren): docx → PDF → JPEG via LibreOffice (`skills/docx/scripts/office/soffice.py --convert-to pdf`, dann `pdftoppm -jpeg`).

---

## Inline-Markup (in jedem Textfeld erlaubt)

- `<b>fett</b>` - Bold. `<i>kursiv</i>` - Italic. Verschachtelbar: `<b><i>…</i></b>`.
- `\n` - neue Zeile innerhalb einer Zelle, eines Absatzes **oder Callouts**.
- **Zeile für Zeile, nie als Block (Pflicht):** Jede Aufzählung, jeder eigenständige Gedanke, jede einzelne Anweisung kommt auf eine **eigene Zeile** (`\n`). Niemals mehrere nummerierte/aufgezählte Punkte in einen Fließtext-Block packen - ein „1) … 2) … 3) …"-Absatz ist falsch, je Punkt eine `\n`-Zeile ist richtig. Gilt für Zellen **und** Callouts.
- Literale `*` und „Anführungszeichen" bleiben unverändert (kollidieren **nicht** mit dem Markup - Sternchen-Disclaimer wie `*pro 30g Pulver` einfach so schreiben). **Kein langer Gedankenstrich „—"** in produzierter Copy (ADMKRS-Hausregel) - stattdessen Punkt/Komma, notfalls das kurze „–". **Kein „·" als Trenner** im Dokument-Inhalt (dek, Überschriften h1/h2/h3, Zellen, Absätze): der Mittelpunkt macht Probleme beim Übernehmen in andere Programme; in Überschriften den Doppelpunkt nutzen („BM-01: …", „3 Hooks: for scroll-stop testing"), sonst Kommas oder `\n`-Zeilen.

---

## Top-Level-Struktur

```json
{
  "filename": "260605_NOVA_Coffee_Whey_Statics_DE",
  "header": {
    "eyebrow": "Motion Concepts V5",          // optional, wird GROSS gesetzt (Kicker über dem Titel)
    "title": "NOVA Protein Coffee - Statics",  // großer Titel
    "dek": "Creative Upgrade, 5 Statics, Stand 05.06.2026"  // optional Untertitel-Zeile
  },
  "blocks": [ /* Reihenfolge = Dokument-Reihenfolge */ ]
}
```

---

## Block-Typen

| `type` | Zweck | Felder |
| --- | --- | --- |
| `h1` | Sektions-Überschrift („Overview", „B-Block – Motion Concepts") - kein `h1 "Briefing"`, kein Strategie-Layer | `text` |
| `h2` | Konzept-Überschrift („BM-01: Sweet Without the Sugar - Crunch") | `text` |
| `h3` | Unter-Überschrift („3 Hooks: for scroll-stop testing", „Storyboard: Time-coded") | `text` |
| `label` | kleine kursive graue Zeile unter h2 (Family-Label, z. B. „Crunch") | `text` |
| `lede` | fetter Intro-Satz | `text` |
| `p` | normaler Absatz (Intro-/Erklärtext), `\n` für Zeilen | `text` |
| `callout` | farbiger Hinweis-Block, **mehrzeilig** - *im Designer-Briefing nicht mehr verwendet (ersatzlos gestrichen, wie die Legende); Builder kann ihn weiterhin rendern (Alt-Dokumente, Sonderfälle)* | `variant` (`"locked"`=lavendel \| `"anchor"`=creme+Gold \| `"todo"`=warm), `lead`, `text` |
| `table` | Tabelle (siehe Layouts) | `layout`, `style`, `widths`, `header`, `rows`, `colAligns`, `colItalics` |
| `outro` | fette Lead-In-Zeile + Text - *nicht mehr verwenden: End-Card gehört als letzte Zeile ins Storyboard* | `lead`, `text` |
| `spacer` | vertikaler Abstand | `size` (optional) |
| `divider` | dünne Trennlinie | - |

### Tabellen-Layouts (`table.layout`)

- **`headerrow`** - schwarze Kopfzeile + Datenzeilen. Für Briefing-Tabelle, Overview, Storyboard.
  - `header`: `["Spalte1", …]`
  - `rows`: `[ ["Zelle1", …], … ]` (Zellenanzahl = Spaltenanzahl)
  - `widths`: relative Gewichte je Spalte, z. B. `[1, 1.6, 1.7]` (werden auf die Seitenbreite skaliert)
  - `style`: `"plain"` (alle Zeilen weiß) oder `"zebra"` (jede 2. Zeile leicht grau)
  - `colAligns` (optional): `["center","left",…]` je Spalte
  - `colItalics` (optional): `[false,…,true]` - z. B. Voice-Over-Spalte kursiv
- **`keyvalue`** - linke Spalte = schwarze Label-Spalte, rechts Wert. Für Motion/Video-Property-Table.
  - `rows`: `[ ["Format","…"], ["Specific Offer","…"], … ]`
  - `widths` (optional): default `[1, 3.2]`
- **`hooks`** - schmale, grau hinterlegte Buchstaben-Spalte (A/B/C) + Hook-Text.
  - `rows`: `[ ["A","<b>…</b>"], ["B","<b>…</b>"], ["C","<b>…</b>"] ]` - **alle drei Hook-Texte fett** (jeder landet als On-Creative-Text); die „Visual 0–2 s"-Zeile darunter nie fett.
  - `widths` (optional): default `[0.7, 9]`

**Spaltenbreiten-Tipp:** Die `#`-Spalte ist **superschmal** (Gewicht ~0,3, nur die Ziffer, zentriert). Die Name-Spalte (`Static`/`Motion`/`Video`) so breit wählen, dass das längste Konzept-Label nicht mitten im Wort umbricht - bei langen Namen wie „Growth / Headcount" Gewicht ~1,1. Lieber den Namen kurz halten *und* die Spalte passend dimensionieren.

---

## Skelett je Briefing-Typ

**Leitfrage für jeden Block: „Braucht der Ausführer (Designer/Editor/Creator) das, um das Asset zu bauen?"** Wenn nein, fliegt er. Agentur-Kunde-Kommunikation (offene Fragen, Freigaben, Strategie-Begründung) lebt in ClickUp/Chat - **nicht im Produktionsdokument.**

**Statics / Carousel (Designer-Dokument - schlank, build-fertig):**
```
header (title, dek)        ← dek trägt Stand + Freigabe: "5 Statics, Stand 05.06., freigegeben"
table keyvalue  "Auf einen Blick"  [Ziel | Zielgruppe | Idee | Formate | Deadline | Assets | Abgabe | Wichtige Infos*]   ← nur Zeilen mit echter Info
table headerrow/plain  [# | Static | Dateiname | Produkt | Creative Format | Hook | Subline | USPs / Badge | CTA | Disclaimer | Visual-Direction]
(optional) h3 "Sternchentexte im Wortlaut" + p   ← nur falls ein Langtext nicht in die Zelle passt - UNTER der Tabelle
```
Mehr nicht. **Keine Callouts vor der Arbeit** (kein todo, kein anchor, kein locked), **keine Legende**, kein `h1 "Briefing"`, kein Intro-Absatz.

**„Auf einen Blick" (Pflicht-Block in jedem Designer-Briefing):**
- **Ziel** - 1 Zeile, was das Set erreichen soll (z. B. „Prospecting cold · CVR-Fokus").
- **Zielgruppe** - 1 Zeile, konkret (wer ist die Person, nicht Demografie-Salat).
- **Idee** - die EINE strategische Idee des Sets, 1–2 Zeilen (ersetzt den früheren Anker-Callout). Hilft dem Designer bei jeder Mikro-Entscheidung - mehr Strategie gehört nicht ins Dokument.
- **Formate** - im Dokument steht **nur**: „Meta-Standard: 4:5 (1080×1350) und 9:16 (1080×1920)." Hinweise wie „kein 1:1" oder „Sonderformate nur auf Ansage" gehören **nicht** ins Dokument. 1:1 nur aufnehmen, wenn der Kunde es explizit will; Sonderformate nur, wenn tatsächlich welche gebrieft sind (dann mit Plattform + Format + Pixeln, z. B. „Pinterest: 2:3, 1000×1500").
- **Deadline** - Datum. Unbekannt? **Beim Ersteller nachfragen**; bleibt sie offen → Zeile weglassen.
- **Assets** - Link/Ablageort zu Logo, Fonts, Brand-Farben, Packshots/Produktbildern, 1–2 Referenz-Creatives (Look-Anker). Die häufigste Rückfrage der Praxis - **im Intake aktiv erfragen**. Bleibt der Link trotz Rückfrage offen → Zeile weglassen und den Punkt intern (ClickUp/Chat) klären.
- **Abgabe** - wohin liefern (Ordner/Tool) + Dateiformat, wenn vom Standard abweichend.
- **Wichtige Infos** - *optional:* nur aufnehmen, wenn es etwas Konkretes gibt (z. B. „Produkt-Label muss lesbar sein"). Keine Resterampe, keine Selbstverständlichkeiten.

**Keine Legende im Dokument.** Die frühere 3-Zeilen-Legende (Fett-Regel, 1:1-Regel, Platzhalter-Regel) entfällt ersatzlos: die Bold-Konvention versteht der Designer ohne Erklärung, und eine „alle Texte 1:1 übernehmen"-Anweisung wollen wir nicht im Briefing - **gute Creatives dürfen Wordings challengen.** Gesperrte Claims, Zahlen und Disclaimer sichert der Autoren-Standard („nichts erfinden, gesperrte Texte 1:1 aus der Quelle") plus die Abnahme über `admkrs-cs-creative-verifier` - nicht ein Hinweistext im Dokument.

**Bold-Konvention (Pflicht, in beide Richtungen):** **Alles, was fett (`<b>`) ist, landet als Text auf dem Creative - und NUR das.** Hook, Subline, USPs/Badge, CTA, Disclaimer-Wortlaut → fett. **Nie fett:** `#`, Konzept-Name, Dateiname, Produkt, Creative Format, Visual-Direction, Anweisungen/Kontext. (Autoren-Konvention fürs Schreiben und die Abnahme - sie wird im Dokument **nicht** erklärt.)

**Final & ohne Ballast (Pflicht):** Build-Zellen enthalten **nur, was wirklich auf dem Creative landet** plus die Visual-Direction - keine Zusatz-Infos, Meta-Kommentare oder Erklärungen in den Zellen. **Offene Punkte stehen NICHT im Dokument** - sie leben im internen Prozess (ClickUp/Chat). **Keine `[Platzhalter: …]` im ausgelieferten Dokument:** fehlende Werte im Intake aktiv nachfragen; bleibt ein Wert offen, die Zeile/Angabe weglassen. Fehlt ein On-Creative-Pflichtwert (Disclaimer-Wortlaut, Offer-Preis), geht das betroffene Konzept nicht mit raus, bis er geklärt ist. Freigabe-Marker (`[CS-Freigabe]`, `[Ergänzung]`) haben im Designer-Dokument nichts verloren. **Kein Ads-Manager-CTA im Briefing:** Der Meta-CTA-Button („Jetzt einkaufen", „Mehr dazu" …) wird im Ads Manager eingestellt und gehört **nicht** in die Tabelle. Der **On-Creative-CTA** (gestaltetes Element, 2–4 Wörter) hat dagegen seine eigene Spalte - **Default leer**, nur wenn er mehr leistet als der Button (Offer-Pill, Code, Dringlichkeit).

**Rollen statt Namen (Pflicht):** Im Dokument stehen **keine Personennamen** - weder als Ansprechpartner noch in Anweisungen („X fragen"). Immer Rollen/Organisation: „zurück an ADMKRS", „CS klärt", „Freigabe durch den Kunden". (Personen-Namen in Review-Zitaten, die ALS Copy aufs Creative gehen, sind davon unberührt.)

**Text-Minimierung & Klarheit zuerst (Pflicht - ein Static ist kein Flyer):**
Ziel: **so wenig Text auf dem Creative wie möglich, ohne dass Verständnis verloren geht.** Klarheit (ein Blick, eine Aussage) schlägt Vollständigkeit. Ein starkes Static ist oft nur **ein Hook + das Produkt.** Jede weitere Zeile muss sich ihren Platz **verdienen**, indem sie einen **eigenen Job** macht, den keine andere Zeile schon erledigt. Die Spalten sind Optionen, keine auszufüllenden Pflichtfelder.
- **Hook** - immer. Der eine Gedanke (Tests: `copywriting.md` §1).
- **Subline** - **nur, wenn sie einen eigenen Job liefert** (Beweis, Trade-off, zweiter Halbsatz). Trägt der Hook allein, bleibt sie leer. Nie Füll-Sublines wie „Entdecke unsere Produkte".
- **USPs / Badge** - **nur bei echten Benefit-/Spec-Konzepten** (USP Ad, Feature-Callout, Listicle). Dann **max. 3 à 2–4 Wörter** und **nie wiederholen, was schon im Hook/Subline steht** (Zahl im Hook → nicht nochmal als USP). Weniger ist besser.
- **CTA (on-creative)** - **Default leer.** Die Handlung steuert meist der Meta-Button (Ads Manager). Ein gestaltetes CTA-Element nur, wenn es etwas tut, das der Button nicht kann (Offer-Pill, Code, Dringlichkeit).
- **Disclaimer** - **nur, wenn ein Claim/Preis ihn faktisch oder rechtlich braucht** (Sternchen-Auflösung). Dann **Wortlaut exakt**, klein als Fußzeile - **Länge ist hier ok**, es ist Kleingedrucktes, kein Headline-Text.
- **Subtraktions-Test (vor jeder Zeile):** „Versteht und überzeugt das Creative es OHNE diese Zeile genauso? Doppelt sie etwas, das schon woanders steht?" Ja → weg. Im Zweifel weglassen.

**Briefing-Tabelle - Spalten (Statics):**

| Spalte | Inhalt |
| --- | --- |
| `#` | **nur die Ziffer** (1, 2, 3 …) - Spalte **superschmal** (Gewicht ~0,3), zentriert, **nicht fett** (landet nicht auf dem Creative). |
| `Static` | der **Konzept-Name** (z. B. „WISMO", „Growth / Headcount", „Kalter Kaffee") - **nicht fett**. Header heißt je Briefing-Typ **`Static`**, **`Motion`** oder **`Video`**. |
| `Dateiname` | nach Naming-Convention des Kunden, sonst ADMKRS-Stil |
| `Produkt` | kurze Produktbezeichnung (z. B. „Schokoriegel", „Protein Butter Cups") |
| `Creative Format` | der Ad-Style aus der Style-Bibliothek (`creative-formats.md`): z. B. Vorher/Nachher, Product Features, USP Ad, 3 Reasons Why, Us vs Them, Review, Lifestyle, Organic Screen, Native Ad, Problem/Solution, Product-Hero … |
| `Hook` | die Headline - **fett** (landet auf dem Creative) |
| `Subline` | **optional** - die Auflösung/der Beweis zum Hook, **nur wenn sie einen eigenen Job macht** (sonst leer, `–`); **fett**. Keine Füll-Subline, kein Wiederholen des Hooks. |
| `USPs / Badge` | **optional** - nur wenn das Konzept sie wirklich braucht (USP Ad, Feature-Callout, Listicle …): **max. 3 Stichpunkte à 2–4 Wörter** ODER ein kurzer Satz; **fett**, zeilenweise. **Nie wiederholen, was schon im Hook/Subline steht.** Kein zweiter Info-Block, keine Klammer-Zusätze. |
| `CTA` | **optional · Default leer.** Gestaltetes CTA-Element **auf dem Creative** (Button/Pill/Zeile), **2–4 Wörter, fett** - nur wenn es mehr leistet als der Meta-Button (Offer-Pill, Code, Dringlichkeit). Die normale Handlung steuert der Ads-Manager-Button; den nie in die Tabelle. |
| `Disclaimer` | **optional** - nur wenn ein Claim/Preis ihn faktisch oder rechtlich braucht (Sternchen-Auflösung). Wortlaut exakt, klein als Fußzeile; **fett**. **Länge hier ok** (Kleingedrucktes). |
| `Visual-Direction` | **Default: leer (`–`).** Spalte bleibt im Schema, aber **nur füllen, wenn es einen expliziten konzeptionellen Grund gibt** (eine Idee, die ohne die visuelle Richtung nicht funktioniert, oder eine klare Kunden-Vorgabe). Sonst leer lassen - der Designer entscheidet die Optik. **Keine Detail-Beschreibung** (Arrangement, Stimmung, Props, „clean & premium"), **keine Formatangaben** (stehen oben), **keine Farben**, keine Pixel. Faustregel: ist das Creative auch ohne Visual-Direction klar gebrieft, bleibt die Zelle leer. |

- **Standard schlägt Vorlage (Pflicht):** Auch wenn ein **älteres Briefing fortgeschrieben** oder als Muster genutzt wird, gilt **immer das aktuelle Tabellen-Schema** - `#`-Spalte nur Ziffer (nicht fett), Konzept-Name in Spalte 2, Bold-Konvention beidseitig. Alte Strukturen beim Übernehmen **migrieren, nie kopieren**.
- **Kein Angle-/Framework-Label in der Designer-Tabelle:** „Pain", „Objection", „Social-Proof" & Co. sind Strategie-Notation - sie gehören **nicht** in die `#`- oder Name-Spalte (und in keine andere Zelle). Die Angle-Logik lebt im Strategie-Pass, im Dokument höchstens in der `Idee`-Zeile.
- **Optionale Spalten (`USPs / Badge`, `CTA`, `Disclaimer`) nur aufnehmen, wenn mindestens ein Creative im Set sie braucht** - sonst Spalte ganz weglassen (kein „–"-Friedhof).
- Jede Zelle **zeilenweise** (`\n`), keine Prosa-Blöcke.
- **Keine `Strategie-Layer`-Tabelle** mehr im Designer-Dokument - die Hebel-/Warum-Analyse bleibt im Strategie-Pass (Chat), im Dokument steht nur die `Idee`-Zeile.
- Carousel: letzte Tabelle = `[Card | Visual | On-Card Text | Zweck]`, Card 1 = Standalone-Hook, letzte Card = CTA.

**Motion / Video (pro Konzept ein Block-Set - schlank, kein Intro, keine Callouts):**
```
header (title, dek)        ← dek trägt Stand + Freigabe; KEIN lede/Intro-Absatz danach
table keyvalue  "Auf einen Blick"  [Ziel & Zielgruppe | Deliverables | Formate | Deadline | Assets | VO & Captions | Abgabe]   ← nur Zeilen mit echter Info
(optional, ab 3+ Konzepten) h1 "Overview" + table headerrow/zebra  [# | Title | Length | Exporte]
  h2 "BM-01: …"            ← ID + Titel (fürs File-Naming); KEIN Family-Label
  table keyvalue  [Idee, Length, Specific Offer, Voice-Over Direction, Music / Sound]
  h3 "3 Hooks: for scroll-stop testing"
  table hooks  [A,B,C]      ← je Hook 2 Zeilen in der Zelle: Hook-Text (fett) \n "Visual 0–2 s: …"
  h3 "VO-Script (Spine): Copy-Block für die VO-Produktion"
  p  "<das komplette gesprochene VO als ein zusammenhängender Take, \n je Beat eine Zeile>"
  h3 "Storyboard: Time-coded"   (Video: "Script: Time-coded")
  table headerrow/zebra  [Time | Visual | On-Screen Text | Voice-Over]   ← LETZTE Zeile = End-Card-Beat (CTA/Offer/Disclaimer), kein outro-Block
  … (nächstes Konzept)
```

**„Auf einen Blick" (Motion/Video) - Zeilen:**
- **Ziel & Zielgruppe** - zusammen 1–2 Zeilen (Kontext, der Mikro-Entscheidungen steuert - mehr nicht).
- **Deliverables** - **die explizite Export-Zählung:** „3 Konzepte × 3 Hook-Varianten × 2 Formate = 18 Exporte, 15–20 s". Verhindert das häufigste Missverständnis (sind A/B/C Optionen oder Deliverables?).
- **Formate** - im Dokument nur: „Meta-Standard: 4:5 (1080×1350) und 9:16 (1080×1920)." Kein-1:1-/Sonderformat-Hinweise nur bei explizitem Anlass (wie Statics).
- **Deadline** - Datum. Unbekannt nach Rückfrage → Zeile weglassen.
- **Assets** - Link zu Rohmaterial/Footage (Video!), Produktbildern, Logo, Fonts, Brand-Farben, 1–2 Referenz-Ads (Pacing-/Stil-Anker). **Im Intake aktiv erfragen**; bleibt der Link offen → Zeile weglassen, Punkt intern klären.
- **VO & Captions** - VO-Quelle (fertiges File / TTS + Stimme / Sprecher) und Captions ja/nein + Stil. Davon hängt das ganze Timing ab.
- **Abgabe** - Lieferort + Export-Spec (Auflösung, Codec, Naming), wenn vom Standard abweichend.

**Pro-Konzept-Tabelle (keyvalue):** **Idee** (1 Satz - warum dieses Konzept; ersetzt den Anker-Callout) · **Length** · **Specific Offer** (exakter Wortlaut/Preis/Code - Source of Truth gegen Tippfehler) · **VO-Direction** · **Music/Sound** (konkrete Referenz/Track-Link, nicht „upbeat"). **Kein** „Target Audience" pro Konzept (steht oben), **kein** „Format" pro Konzept (steht oben, nur bei Abweichung).

> **VO-First (Pflicht-Vorgehen).** Pro Motion-/Video-Konzept ist das **„VO-Script (Spine)"** das **führende Element**: ein `h3` „VO-Script (Spine)" + ein `p`-Block mit dem **kompletten gesprochenen VO am Stück** (je Beat eine Zeile via `\n`) - **vor** dem time-coded Storyboard. Schreib das VO zuerst und durchgehend, sodass es sich als **ein** natürlicher Take liest; **dann** mappt das Storyboard `Time · Visual · On-Screen-Text` **auf die VO-Beats**. Im Dokument ist der Spine der **Copy-Block für die VO-Produktion** (Sprecher/TTS) - er muss **wortidentisch** mit der Voice-Over-Spalte des Storyboards sein (eine Quelle, kein Drift; bei Revisionen beide gleichzeitig ändern).
>
> **Redefluss, kein Stakkato:** Der Spine liest sich von oben nach unten als zusammenhängender, natürlich gesprochener Monolog (Bindeglieder, „du"-Ansprache, Hook 0–2 s → Spannung → Auflösung → CTA). Jede Zeile knüpft an die vorige an. On-Screen-Text darf knapp/Schlagwort sein, das gesprochene VO nie - im VO sind Diskursmarker, Füllwörter und Überleitungen („also", „und das Beste:", „ehrlich") **erwünscht**, sie machen den Take menschlich (Sprechfluss-Doktrin: `../admkrs-cs-ugc-briefing/references/creator-script-craft.md` §5b; Kürze-Doktrin gilt für On-Screen, nicht fürs Gesprochene). Schreibregeln: `creative-formats.md` §5b · Vorher/Nachher: `copywriting-frameworks.md` §4b. *(Kein Builder-Eingriff nötig - `h3`+`p` sind Standard-Blöcke.)*
>
> **End-Card als Beat (Pflicht).** Die End-Card (CTA, Offer/Code, Sternchentext) steht als **letzte timecodierte Zeile in der Storyboard-Tabelle** - nie als `outro`-Prosa danach. Was nach dem Storyboard steht, liest kein Editor mehr; ein fehlender End-Card-Disclaimer fällt sonst erst beim Kunden auf.

---

## Struktur-Regeln - zeilenweise, Designer-tauglich, finale Briefings

Ein Briefing ist eine Bau-Anweisung, kein Strategie-Essay. Es muss so klar sein, dass ein Designer oder Editor es **ohne Rückfrage** umsetzen kann - und so schlank, dass nichts vor der eigentlichen Arbeit steht, was nicht zum Bauen gebraucht wird.

- **Ausführer-Test für jeden Block.** Vor dem Bauen jedes Blocks fragen: „Braucht der Designer/Editor/Creator das, um das Asset zu produzieren?" Nein → raus. Agentur-Kunde-Kommunikation (offene Fragen, Freigaben, Hypothesen) lebt in ClickUp/Chat, nicht im Dokument.
- **Zeile für Zeile, kein Block.** Aufzählungen, mehrere Anweisungen, mehrere Fakten: je Punkt eine `\n`-Zeile. Ein dichter Absatz mit „1) … 2) … 3) …" ist ein Fehler.
- **Nur was beim Bauen hilft.** Rein kommt, was Bild, Text, Layout, Specs, VO oder Schnitt betrifft. Strategie steckt in der **einen** `Idee`-Zeile (1–2 Zeilen in „Auf einen Blick" bzw. der Konzept-keyvalue) - kein Callout, keine Hebel-/Analyse-Tabelle, keine Awareness-Theorie. (UGC-Briefing: Kunden-Layer erlaubt, aber **hinten** als Anhang - Creator-Teil zuerst.)
- **„Auf einen Blick" ist Pflicht** - aber nur mit Zeilen, die echte Info tragen. Die **Assets-Quelle** (Logo/Fonts/Packshots/Footage/Referenzen-Link) ist der häufigste Produktionsblocker → **Pflicht-Rückfrage im Intake**; ohne Antwort Zeile weglassen statt Platzhalter.
- **Format-Regel (Meta):** Wir produzieren **4:5 + 9:16**, kein 1:1 (Autoren-Wissen; 1:1 nur auf expliziten Kundenwunsch). Im Dokument steht nur die Meta-Standard-Zeile; Kein-1:1-/Sonderformat-Hinweise nur bei echtem Anlass. Formatangaben stehen NUR im „Auf einen Blick", nie in den Visual-Direction-Zellen.
- **Keine Callouts, keine Legende:** todo-/locked-Callouts sind gestrichen, und auch die frühere 3-Zeilen-Legende entfällt - das Dokument enthält nur Inhalt, keine Meta-Anweisungen an den Leser.
- **Kein „·" als Trenner** im Dokument-Inhalt (dek, Überschriften, Zellen, Absätze) - schlecht in andere Programme übertragbar; in Überschriften Doppelpunkt, sonst Kommas oder `\n`-Zeilen nutzen.
- **Visual-Direction so weit wie möglich reduzieren - Default leer.** Die Spalte bleibt, aber **leer ist der Normalfall.** Nur füllen, wenn das Konzept es zwingend braucht (eine visuelle Idee, ohne die das Creative nicht funktioniert) oder eine klare Kunden-Vorgabe existiert. Dann knapp: keine Detail-Beschreibung, keine Stimmungswörter, keine Formate/Farben/Pixel. Designer kreativ arbeiten lassen - das Briefing entscheidet *was* gesagt wird (Hook/Subline/USPs), nicht *wie es aussieht*, außer das Aussehen IST das Konzept. *(Gilt für die Static-/Carousel-`Visual-Direction`-Spalte. Bei Motion/Video ist die Storyboard-`Visual`-Spalte keine ästhetische Richtung, sondern die funktionale Beat-Anweisung - sie bleibt, aber auch dort nur, was Animation/Schnitt wirklich braucht, nicht ausschmücken.)*
- **Final entscheiden, nicht abwägen.** Build-Zellen enthalten Entscheidungen, keine offenen Fragen und kein „evtl./oder vielleicht". Beispiel: „Initiale im Kreis, kein KI-Gesicht" statt „KI-Frau geblurrt, könnte fake wirken".
- **Ein konkreter Fakt statt Floskel.** Keine generischen Badges doppeln („Geschmack, der für sich spricht" 3× im Set). Je Slide/Static **ein** konkreter, freigegebener Fakt („1,5 g Zucker pro Riegel", „max. 84 kcal pro Tüte"). Info statt Floskel = weniger salesy.
- **Rückfragen statt Platzhalter.** Niemals raten oder Zahlen erfinden - aber auch **keine `[Platzhalter: …]` im ausgelieferten Dokument.** Fehlende Werte (Deadline, Assets, Abgabe, Offer-Details …) werden **im Intake aktiv beim Ersteller nachgefragt**; bleibt ein Wert offen, wird die Zeile/Angabe **weggelassen** und der Punkt intern (ClickUp/Chat) getrackt. Fehlt ein On-Creative-Pflichtwert (Disclaimer-Wortlaut, Offer-Preis), geht das betroffene Konzept nicht mit raus, bis er geklärt ist. Der Stand steht im `dek` („Stand 05.06., freigegeben").
- **Rollen statt Namen.** Keine Personennamen im Dokument - „zurück an ADMKRS", „CS klärt", nie „[Name] fragen". (Ausnahme: Namen, die als Copy aufs Creative gehen, z. B. Review-Zitate.)

---

## Design-Tokens (fest verdrahtet - nur zur Orientierung)

Aus den Referenzdokumenten 1:1 übernommen. **Nicht** im Inhalt überschreiben - der Builder setzt sie.

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
| Seite | **B4 Querformat** (ISO B4, 250×353 mm, Landscape), **1 cm Ränder** - ADMKRS-Standard für *alle* erzeugten Dokumente |

---

## Locked-Facts im Dokument

- **Kein separater Locked-Block, keine Legende.** Gesperrte Claims, Preise, Disclaimer stehen **fett in der Tabellenzelle** - das ist die einzige Quelle (kein Drift zwischen Callout und Tabelle). Ihre Verbindlichkeit wird **nicht im Dokument erklärt**, sondern über den Autoren-Standard (nichts erfinden, gesperrte Texte 1:1 aus der Quelle) und die Abnahme (`admkrs-cs-creative-verifier`, Briefing-Treue) gesichert. Wording-Verbesserungen durch den Designer sind bei freier Copy willkommen; gesperrte Claims/Zahlen/Disclaimer bleiben exakt.
- **Ausnahme Langtexte:** Sternchentexte/Disclaimer, die nicht in eine Zelle passen, kommen als `h3 "Sternchentexte im Wortlaut"` + `p` **unter** die Tabelle - nie davor.
- **[Ergänzung]/[CS-Freigabe]** sind interne Marker für den Strategie-Pass und die Kunden-Abstimmung - sie erscheinen **nicht** im Designer-Dokument. Was im Dokument steht, ist freigegeben; was nicht freigegeben ist, kommt **nicht ins Dokument** und wird intern getrackt.
- Disclaimer/Sternchen exakt übernehmen (`*pro 30g Pulver`).
