---
name: admkrs-cs-motion-ad-briefing
description: >
  Erstellt ADMKRS Creative Briefings für MOTION ADS (animierte Ads, kinetische Typografie,
  Motion-Graphics, faceless/Data-led - keine Live-Faces) als formatiertes .docx im ADMKRS-Stil,
  mit time-coded Storyboard. Use this skill when the user wants a motion ad, animated ad, kinetic
  typography, motion graphics, or says "Motion Ad", "Motion", "Animation", "kinetische Typo",
  "Motion Graphic" and wants the creative briefed. VOICE-OVER-FIRST. Nutzt die gemeinsame Engine
  von admkrs-cs-creative-briefing.
---

# ADMKRS Motion-Ad Briefing

Brieft **Motion Ads** (animiert, kinetische Typo, Motion-Graphics, faceless) im ADMKRS-Stil. **Format-spezifische Tür** zur ADMKRS-Briefing-Methode - Engine & References liegen in **`admkrs-cs-creative-briefing`**, hier auf **Motion** gescoped.

## VOICE-OVER-FIRST (Pflicht)
**Jedes Motion-Konzept wird vom Voice-Over her gebrieft.** Das **VO-Script (Spine)** ist das Rückgrat - als zusammenhängender, am Stück lesbarer Block (`h3` „VO-Script (Spine)" + `p`) **vor** dem time-coded Storyboard; Bild & On-Screen-Text hängen sich an die VO-Beats. Das VO ist ein **natürlich gesprochener Take** (Hook 0–2 s → Spannung → Auflösung → CTA), **kein** Stakkato. Schreibregeln: `admkrs-cs-creative-briefing/references/creative-formats.md` §5b · Struktur: `references/document-format.md` · Vorher/Nachher: `references/copywriting-frameworks.md` §4b.

## Vorgehen
Folge dem Workflow aus `admkrs-cs-creative-briefing`, **nur für Motion**:
- **Dokument-Skelett (keine Callouts, kein Intro):** **„Auf einen Blick"** (Ziel & Zielgruppe · **Deliverables-Zählung** (Konzepte × Hooks × Formate = Exporte) · Formate · Deadline · **Assets-Link** (Produktbilder/Logo/Fonts/Referenz-Ads) · VO & Captions (Quelle + Stil) · Abgabe) (**nur Zeilen mit echter Info**, fehlende Werte im Intake nachfragen, sonst Zeile weglassen; **keine Legende**) → optional Overview `[# | Title | Length | Exporte]` (ab 3+ Konzepten) → pro Konzept: h2 (ID + Titel, **kein Family-Label**) + keyvalue (**Idee** (1 Satz) · Length · Offer · VO-Direction · Music mit konkreter Referenz - **zeilenweise**, kein Target-Audience) + 3 Hooks (verschiedene Kategorien, je Hook 2. Zeile „Visual 0–2 s: …") + **VO-Script (Spine)** (**Hook-Varianten-Notation:** der Spine beginnt mit drei Zeilen „Hook A: …", „Hook B: …", „Hook C: …" - wortidentisch mit der Hooks-Tabelle, in Dokumentsprache; danach läuft der Take für alle Varianten gemeinsam weiter. Storyboard-Zeile 1 trägt in der Voice-Over-Spalte exakt dieselben drei Hook-Zeilen. **Keine eckigen Klammern**, keine Anweisungs-Marker wie „pick A/B/C") + time-coded Storyboard `[Time | Visual | On-Screen-Text | Voice-Over]` - **letzte Zeile = End-Card-Beat** (CTA/Offer/Disclaimer), kein outro. **1 Angle = 1 Konzept.**
- **Format-Regel (Meta):** produziert wird 4:5 + 9:16, kein 1:1 (außer explizit gewünscht). **Im Dokument steht nur die Meta-Standard-Zeile**; Kein-1:1-/Sonderformat-Hinweise nur bei echtem Anlass (Sonderformate dann mit Plattform + Pixeln). **Bold-Konvention:** fett = landet auf dem Creative (On-Screen-Text).
- **References lesen** (Ordner `references/` von `admkrs-cs-creative-briefing`): `creative-strategy.md` · `hook-library.md` (inkl. Kat. 16 Voss) · `copywriting.md` · `copywriting-frameworks.md` (§4b VO-Redefluss, AIDA/SLAP, BAB/DASER) · `creative-formats.md` (§5b VO-First + Gruppe D) · `voss-principles.md` · `document-format.md` · `field-notes.md` (§2b VO-Retention-Evidenz).
- **Bauen:** `node ../admkrs-cs-creative-briefing/assets/build_briefing.js (einmalig `npm install docx` in dessen assets/, falls node_modules fehlt) <briefing.json> <YYMMDD_BRAND_Product_Motion_LANG.docx>`. Muster: `examples/example_motion_briefing.json` (mit VO-Spine).

## Leitprinzipien (kurz)
**Hooks zuerst · VO-First & Redefluss · Klarheit vor Kunst, dann Haltung (Voss) · eine Idee pro Konzept · nichts erfinden.** Plattform-nativ, sound-off-tauglich (Captions).
**Build-fertig & zeilenweise:** Property-/Storyboard-Zellen zeilenweise (`\n`); **Ausführer-Test** - nur was der Motion-Designer zum Bauen braucht (keine Strategie-Prosa, keine Callouts); final entschieden; fehlende Werte **nachfragen, sonst weglassen** (kein `[Platzhalter: …]` im Dokument), offene Punkte intern in ClickUp/Chat; **keine Personennamen** (Rollen statt Namen); **kein „·" als Trenner** im Dokument-Inhalt (Kommas oder Zeilen) - gerade in keyvalue-Zellen und dek-Zeilen. **Sicherheit:** nie senden/posten/löschen ohne Freigabe; Abnahme durch `admkrs-cs-creative-verifier`, dann vor Launch `admkrs-cs-ad-compliance-check`.

<sub>**ADMKRS Creative Suite** · © ADMKRS GmbH, München · v1.13.0 · interner Gebrauch · Format-Tür zu `admkrs-cs-creative-briefing` (gemeinsame Engine, keine Duplikate).</sub>
