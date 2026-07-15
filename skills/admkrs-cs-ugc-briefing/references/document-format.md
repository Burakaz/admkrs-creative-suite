# Dokument-Format - UGC-Briefing JSON, Builder & Skelett

Das UGC-Briefing wird aus einer **JSON-Spec** gerendert. Builder: `assets/build_briefing.js` (Node + `docx`) - **identische Engine wie `admkrs-cs-creative-briefing`**, gleicher ADMKRS-Stil, gleiches **B4 Querformat / 1 cm Ränder**. Inhalt füllen, Builder laufen lassen, fertig.

**Vorgehen:** Nimm `examples/example_ugc_briefing.json` als Muster - Struktur kopieren, Inhalt ersetzen. Nicht von Null bauen.

---

## Builder ausführen

```bash
cd <skill>/assets && npm install docx        # einmalig pro Umgebung
node <skill>/assets/build_briefing.js <input.json> <YYMMDD_BRAND_Product_UGC_LANG.docx>
```

Wird der Output-Name weggelassen, nimmt der Builder das Feld `filename` aus der JSON (Konvention `YYMMDD_BRAND_Product_UGC_LANG`, Sprache am Ende: DE/EN/NL/FR/AT). Danach das .docx mit `present_files` zeigen. **Best Practice (Cowork mit verbundener Drive):** das fertige .docx in **Google Drive** im Kunden-Ordner unter **„Briefings"** ablegen (Name nach Konvention) - **nicht** ungefragt in Slack/ClickUp posten; Speichern in der Kunden-Drive ist ok. Optionaler Render-Check: docx → PDF → JPEG via LibreOffice (`skills/docx/scripts/office/soffice.py --convert-to pdf`, dann `pdftoppm -jpeg`).

**Seite:** B4 Querformat (ISO B4, 250×353 mm, Landscape), 1 cm Ränder - ADMKRS-Standard für *alle* erzeugten Dokumente (fest im Builder).

---

## Inline-Markup (in jedem Textfeld)
`<b>fett</b>` · `<i>kursiv</i>` · `\n` neue Zeile in Zelle, Absatz **oder Callout**. Literale `*` und „Anführungszeichen" bleiben unverändert (Sternchen-Disclaimer wie `*pro Portion` einfach so schreiben). **Kein langer Gedankenstrich „—"** in produzierter Copy (Hausregel) - Punkt/Komma, notfalls „–". **Kein „·" als Trenner** im Dokument-Inhalt (dek, Überschriften h1/h2/h3, Zellen, Absätze): der Mittelpunkt macht Probleme beim Übernehmen in andere Programme; in Überschriften den Doppelpunkt nutzen („Konzept 1: …", „3 Hooks: zum Scroll-Stop-Test"), sonst Kommas oder `\n`-Zeilen.

**Zeile für Zeile, nie als Block (Pflicht):** Aufzählungen, mehrere Anweisungen, mehrere Fakten - je Punkt eine `\n`-Zeile, in Zellen wie in Callouts. Ein „1) … 2) … 3) …"-Fließtext-Block ist falsch.

**Bold-Semantik (UGC):** Die Haus-Regel „Bold = landet auf dem Creative" heißt hier: `<b>` markiert, was **wörtlich übernommen bzw. wörtlich eingeblendet** wird - gesperrte Claims/Zahlen/Codes (z. B. `Code <b>TRYNOVA</b>`, die „Werbung"-Einblendung), die 1:1-Spalte in „Darf & darf nicht" und die On-Screen-Text-Spalte im Script. Gesprochene Hooks und VO-Beats sind Beats, kein On-Creative-Text → **plain** (alle 3 Hooks eines Konzepts einheitlich unformatiert). Kein Bold zur bloßen Betonung.

---

## Top-Level

```json
{
  "filename": "260607_NOVA_ProteinCoffee_UGC_DE",
  "header": {
    "eyebrow": "UGC Creator Briefing",
    "title": "NOVA Protein Coffee - UGC",
    "dek": "3 Konzepte, 9 Hooks, drehfertige Scripts, Stand 07.06.2026"
  },
  "blocks": [ /* Reihenfolge = Dokument-Reihenfolge */ ]
}
```

## Block-Typen (wie admkrs-cs-creative-briefing)

`h1`/`h2`/`h3` (Überschriften) · `label` (graue Kursiv-Zeile unter h2) · `lede` (fetter Intro-Satz) · `p` (Absatz, `\n` für Zeilen) · `table` (`layout`: `headerrow` \| `keyvalue` \| `hooks`) · `spacer` · `divider`. - *Vom Builder weiterhin renderbar, aber im UGC-Briefing nicht mehr verwendet:* `callout` (todo/anchor/locked) und `outro` (CTA gehört als letzter Beat ins Script).

**Tabellen-Layouts:**
- `headerrow` - schwarze Kopfzeile + Zeilen. `header`, `rows`, `widths` (relative Gewichte), `style` `"plain"`/`"zebra"`, optional `colAligns`, `colItalics` (z. B. VO-Spalte kursiv).
- `keyvalue` - schwarze Label-Spalte links, Wert rechts. `rows`: `[["Format","…"], …]`, `widths` default `[1, 3.2]`.
- `hooks` - schmale graue Buchstaben-Spalte (A/B/C) + Hook-Text. `rows`: `[["A","…"], …]`, `widths` default `[0.7, 9]`.

**Spaltenbreiten-Tipp:** erste Spalte (Index/Zeit/Label) breit genug, dass das längste Label nicht mitten im Wort umbricht.

---

## UGC-Briefing-Skelett (Creator-First, Kunden-Layer als Anhang)

**Reihenfolge-Prinzip: Der Creator liest von vorne - also steht vorne, was er zum Drehen braucht.** Auftrag → Lieferung → Darf/Darf-nicht → Produkt & Ton → Konzepte mit Scripts → Scroll-Breaker → **Strategie-Anhang für den Kunden ganz hinten** (der Creator überspringt ihn, den Kunden stört er dort nicht). Kein todo-Callout, keine locked-Callouts - offene Punkte leben in ClickUp/Chat, gesperrte Texte stehen 1:1 in den Zellen, die Regeln stehen in „Darf & darf nicht". Details je Block: `brand-foundation.md`.

```
header (eyebrow "UGC Creator Briefing", title, dek)   ← dek mit Stand + "freigegeben"

h1 "Dein Auftrag"                  ← 4–5 Zeilen, mehr nicht
  table keyvalue  [Auftrag (1 Satz: "3 Videos à 20–30 s für TikTok/Reels") | Deadline | Produkt-Logistik (kommt per Post bis …) | Rückfragen (Kanal - Rolle, kein Name) | Offer/Code]

h1 "Lieferung & Specs"
  table keyvalue  [Stückzahl (explizit: 3 Konzepte × 3 Hook-Takes = 9 Files? oder 3?) | Ratio & Länge (9:16, …) | Roh oder geschnitten | Captions ja/nein | Dateiname | Upload-Ort (Link) | Kennzeichnung ("Werbung"-Disclosure - Pflicht)]

h1 "Darf & darf nicht"             ← MUSS vor den Scripts stehen
  table headerrow/plain  [Darf ich sagen | Darf ich NICHT sagen]   (Claims/Zahlen 1:1 sagbar vs. verboten - Heil-/Med-Claims etc.)
  p  (zeilenweise: Film-Dos/Don'ts, Aussprache des Markennamens, 2–3 Referenz-Links "so soll es aussehen" + 1 "so nicht")

h1 "Produkt & Ton"                 ← max. halbe Seite
  table keyvalue  [Produkt (1 Zeile) | 5 Facts, die du sagen darfst (zeilenweise, 1:1) | Ton (1 Zeile) | Was die Brand NICHT ist (1 Zeile) | Für wen du sprichst (2 Zeilen: Trigger-Moment + Einwand der Zielperson, ohne Strategie-Theorie - volle Persona bleibt im Anhang)]

h1 "Konzept 1: [Title]"            ← das Kernstück, pro Konzept ein Set
  p  "Idee: …"   (1 Satz - warum dieses Video; ersetzt den Anker-Callout)
  h3 "3 Hooks: zum Scroll-Stop-Test"
  table hooks  [A, B, C]
  h3 "Script: drehfertig"
  table headerrow/zebra  [Beat | Was du tust | On-Screen Text | Was du sagst]   (colItalics: [false,false,false,true])
       ← Beats (Hook/Problem/Demo/CTA) statt Sekunden-Korsett; Richtwert-Sekunden in der Beat-Zelle. Letzte Zeile = CTA-Beat (kein outro-Block).
  p  "<i>Regie-Notiz: …</i>"   (optional, 1 Zeile)
  … (Konzept 2, Konzept 3)

h1 "Scroll-Breaker: Bonus"         ← explizit gescoped
  p  "Optional - NICHT Teil der [N] Videos. Nur wenn Zeit & Lust:"  + max. 2 Ideen zeilenweise
  (Sind Scroll-Breaker Teil des Auftrags → stattdessen als reguläres Konzept briefen.)

h1 "Anhang: Strategie (für die Kunden-Präsentation)"   ← GANZ hinten; Creator kann hier aufhören zu lesen
  p  (Persona, Awareness, Funnel - zeilenweise)
  table headerrow/zebra  [Konzept | Angle | Framework | Awareness | Hypothese]
  (Auf Wunsch stattdessen als separates Kunden-Dokument aus derselben JSON - Creator-Doc bleibt dann ohne Anhang.)
```

**Script-Spalten:** `widths` ca. `[0.9, 3.4, 2.2, 3.0]`, `colAligns` `["center","left","left","left"]`, `colItalics` `[false,false,false,true]` (VO kursiv). Hook-Zeile: On-Screen = `<b>HOOK</b>`, VO = `"[ Hook, A / B / C ]"`.

---

## Struktur-Regeln - zeilenweise & final

- **Creator-Test für jeden Block:** Hilft das dem Creator beim Drehen? Nein → in den Anhang (Kunden-Strategie) oder ganz raus (interne Punkte). Das Dokument geht raus und wird auf dem **Handy** gelesen - kurze Blöcke, Beats statt Sekunden-Korsett.
- **Zeile für Zeile, kein Block.** Aufzählungen/mehrere Fakten je `\n`-Zeile. Ein „1) … 2) … 3) …"-Fließtext-Block ist falsch.
- **Keine offenen Punkte im Dokument.** Das Briefing geht erst raus, wenn geklärt (dek: „Stand …, freigegeben"); fehlt doch ein Wert: **beim Ersteller nachfragen, sonst die Zeile/Angabe weglassen** - kein `[Platzhalter: …]` im Dokument, der Creator füllt nie selbst. Offene Punkte trackt ADMKRS intern (ClickUp/Chat).
- **Scope glasklar.** Stückzahl explizit ausrechnen (Konzepte × Hook-Takes = Files); Scroll-Breaker explizit als „Bonus, nicht Teil des Scopes" labeln (oder als reguläres Konzept briefen).
- **Final entscheiden, ein konkreter Fakt statt Floskel**, nichts erfinden.
- **Rollen statt Namen:** keine Personennamen im Dokument - „Rückfragen an ADMKRS via [Kanal]", nie „[Name] fragen".

---

## Locked-Facts im Dokument
**Kein Locked-Callout mehr.** Sagbare Claims/Zahlen stehen 1:1 in „Darf & darf nicht" und in den Scripts - das ist die einzige Quelle. Verbotenes steht in der „Darf ich NICHT sagen"-Spalte. **[Ergänzung]**-Marker sind intern (Strategie-Pass/Kunden-Abstimmung) und erscheinen nicht im Creator-Dokument. Disclaimer/Sternchen exakt übernehmen.

---
<sub>**ADMKRS Creative Suite** · © ADMKRS GmbH, München · v1.13.0 · interner Gebrauch · erstellt von ADMKRS. Gleiche Builder-Engine & B4-Standard wie admkrs-cs-creative-briefing.</sub>
