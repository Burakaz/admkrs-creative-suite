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
- **Dokument-Skelett:** Strategie-Layer → Briefing-Tabelle (**eine Zeile pro Static**). Carousel: letzte Tabelle = `[Card | Visual | On-Card-Text | Zweck]`, Card 1 = Standalone-Hook, letzte Card = CTA.
- **References lesen** (im Skill `admkrs-cs-creative-briefing`, Ordner `references/` — relativ `../admkrs-cs-creative-briefing/references/`): `creative-strategy.md` · `hook-library.md` (inkl. Kat. 16 Voss) · `copywriting.md` · `copywriting-frameworks.md` (PAS/BAB/4Ps/Comparative für Static) · `creative-formats.md` (§6 Static) · `voss-principles.md` · `document-format.md` · `field-notes.md`.
- **Bauen** mit der gemeinsamen Engine: `node skills/admkrs-cs-creative-briefing/assets/build_briefing.js <briefing.json> <YYMMDD_BRAND_Product_Statics_LANG.docx>`. Muster: `examples/example_statics_briefing.json`.

## Leitprinzipien (kurz — Details in `admkrs-cs-creative-briefing`)
**Hooks zuerst · Konkret schlägt generisch · Klarheit vor Kunst, dann Haltung (Voss) · Eine Idee pro Static · nichts erfinden (Claims/Offers 1:1, Neues als [Ergänzung]).** Offer-Statics mit klarem Offer sind der Effizienz-Hebel. Banned-Buzzwords gelten. **Sicherheits-Regeln:** nie senden/posten/löschen ohne Freigabe; vor Launch durch `admkrs-cs-ad-compliance-check`.

<sub>**ADMKRS Creative Suite** · © ADMKRS GmbH, München · v1.3.0 · interner Gebrauch · Format-Tür zu `admkrs-cs-creative-briefing` (gemeinsame Engine, keine Duplikate).</sub>
