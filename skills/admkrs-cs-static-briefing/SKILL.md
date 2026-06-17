---
name: admkrs-cs-static-briefing
description: >
  Erstellt ADMKRS Creative Briefings für STATIC- & CAROUSEL-Ads (Single-Image, Review,
  Comparison, Offer/Promo, Listicle, Native/Lo-fi) als formatiertes .docx im ADMKRS-Haus-Stil.
  Use this skill when the user wants a static ad, single-image ad, offer/sale static, comparison,
  review/testimonial static, carousel, or says "Static", "Statics", "Bild-Anzeige", "Offer-Static",
  "Carousel", "Sale-Anzeige" and wants the creative briefed. Format-spezifische Tür zur ADMKRS-
  Briefing-Methode — nutzt die gemeinsame Engine von admkrs-cs-creative-briefing.
---

# ADMKRS Static Briefing

Brieft **Static- & Carousel-Ads** im exakten ADMKRS-Stil. Das ist die **format-spezifische Tür** zur ADMKRS-Briefing-Methode — die volle Strategie-, Hook- und Copy-Engine sowie der docx-Builder liegen im Skill **`admkrs-cs-creative-briefing`**; dieser Skill scoped sie auf **Statics/Carousel**.

## Vorgehen
Folge dem Workflow aus `admkrs-cs-creative-briefing` (Briefing-Typ bestimmen → Brand-Profil → Intake → Strategie-Pass → Creatives → Dokument → Quality-Check → Übergabe), aber **nur für Statics/Carousel**:
- **Dokument-Skelett (schlank, build-fertig — keine Callouts, kein Intro, kein `h1 "Briefing"`):** **„Auf einen Blick"** (Ziel · Zielgruppe · Idee · Formate · Deadline · **Assets** · Abgabe · „Wichtige Infos" nur wenn konkret) → **3-Zeilen-Legende** (Fett = Creative · Texte 1:1 · [Platzhalter] nicht füllen) → Briefing-Tabelle `[# | Static | Dateiname | Produkt | Creative Format | Hook | Subline | USPs / Badge | CTA | Disclaimer | Visual-Direction]` (**eine Zeile pro Static**, Zellen zeilenweise; #-Spalte NUR die Ziffer, Name in Spalte 2, kein Angle-Label wie „Pain" in der Tabelle; optionale Spalten weglassen, wenn im Set leer. **Gilt auch beim Fortschreiben älterer Briefings: Standard schlägt Vorlage.**) → optional `h3 "Sternchentexte im Wortlaut"` UNTER der Tabelle (nur Langtexte). Offene Punkte leben in ClickUp/Chat, im Dokument nur `[Platzhalter: …]` inline; **keine Personennamen** (Rollen statt Namen). **Keine Strategie-Layer-/Hebel-Tabelle** im Designer-Dokument. Carousel: letzte Tabelle = `[Card | Visual | On-Card-Text | Zweck]`, Card 1 = Standalone-Hook, letzte Card = CTA.
- **Format-Regel (Meta):** 4:5 + 9:16 Standard, **kein 1:1**. Sonderformate (andere Plattformen) extra mit Plattform + Format + Pixeln — nur im „Auf einen Blick", nie in Visual-Direction.
- **Bold-Konvention (beide Richtungen):** **fett = landet auf dem Creative, und NUR das** (Hook, Subline, USPs/Badge, Disclaimer). Nie fett: #, Konzept-Name, Dateiname, Creative Format, Visual-Direction. **Kein Ads-Manager-CTA in der Tabelle** — CTA-Text nur, wenn er als gestaltetes Element auf dem Bild liegt.
- **Creative Format** je Static benennen (Ad-Style aus `creative-formats.md`: USP Ad, Review, Product-Hero, Us vs Them, Organic Screen, Problem/Solution …).
- **Visual-Direction so weit wie möglich reduzieren — Default leer (`–`):** Spalte bleibt, aber nur füllen, wenn das Konzept eine visuelle Richtung zwingend braucht oder eine klare Kunden-Vorgabe existiert. Sonst leer, Designer entscheidet die Optik. Keine Detail-/Stimmungs-Beschreibung, keine Formate/Farben.
- **References lesen** (im Skill `admkrs-cs-creative-briefing`, Ordner `references/` — relativ `../admkrs-cs-creative-briefing/references/`): `creative-strategy.md` · `hook-library.md` (inkl. Kat. 16 Voss) · `copywriting.md` · `copywriting-frameworks.md` (PAS/BAB/4Ps/Comparative für Static) · `creative-formats.md` (§6 Static) · `voss-principles.md` · `document-format.md` · `field-notes.md`.
- **Bauen** mit der gemeinsamen Engine: `node skills/admkrs-cs-creative-briefing/assets/build_briefing.js <briefing.json> <YYMMDD_BRAND_Product_Statics_LANG.docx>`. Muster: `examples/example_statics_briefing.json`.

## Leitprinzipien (kurz — Details in `admkrs-cs-creative-briefing`)
**Hooks zuerst · Konkret schlägt generisch · Klarheit vor Kunst, dann Haltung (Voss) · Eine Idee pro Static · nichts erfinden (Claims/Offers 1:1, Neues als [Ergänzung]).** Offer-Statics mit klarem Offer sind der Effizienz-Hebel. Banned-Buzzwords gelten.
**Build-fertig & zeilenweise:** Zellen zeilenweise (`\n`), nie als Block; **Ausführer-Test** — nur was der Designer zum Bauen braucht; Build-Zellen final entschieden (keine offenen Fragen); ein konkreter Fakt statt Floskel; fehlende Werte als `[Platzhalter: …]` **inline**, offene Punkte intern in ClickUp/Chat. **Sicherheits-Regeln:** nie senden/posten/löschen ohne Freigabe; vor Launch durch `admkrs-cs-ad-compliance-check`.

<sub>**ADMKRS Creative Suite** · © ADMKRS GmbH, München · v1.8.0 · interner Gebrauch · Format-Tür zu `admkrs-cs-creative-briefing` (gemeinsame Engine, keine Duplikate).</sub>
