---
name: admkrs-cs-motion-ad-briefing
description: >
  Erstellt ADMKRS Creative Briefings für MOTION ADS (animierte Ads, kinetische Typografie,
  Motion-Graphics, faceless/Data-led — keine Live-Faces) als formatiertes .docx im ADMKRS-Stil,
  mit time-coded Storyboard. Use this skill when the user wants a motion ad, animated ad, kinetic
  typography, motion graphics, or says "Motion Ad", "Motion", "Animation", "kinetische Typo",
  "Motion Graphic" and wants the creative briefed. VOICE-OVER-FIRST. Nutzt die gemeinsame Engine
  von admkrs-cs-creative-briefing.
---

# ADMKRS Motion-Ad Briefing

Brieft **Motion Ads** (animiert, kinetische Typo, Motion-Graphics, faceless) im ADMKRS-Stil. **Format-spezifische Tür** zur ADMKRS-Briefing-Methode — Engine & References liegen in **`admkrs-cs-creative-briefing`**, hier auf **Motion** gescoped.

## VOICE-OVER-FIRST (Pflicht)
**Jedes Motion-Konzept wird vom Voice-Over her gebrieft.** Das **VO-Script (Spine)** ist das Rückgrat — als zusammenhängender, am Stück lesbarer Block (`h3` „VO-Script (Spine)" + `p`) **vor** dem time-coded Storyboard; Bild & On-Screen-Text hängen sich an die VO-Beats. Das VO ist ein **natürlich gesprochener Take** (Hook 0–2 s → Spannung → Auflösung → CTA), **kein** Stakkato. Schreibregeln: `admkrs-cs-creative-briefing/references/creative-formats.md` §5b · Struktur: `references/document-format.md` · Vorher/Nachher: `references/copywriting-frameworks.md` §4b.

## Vorgehen
Folge dem Workflow aus `admkrs-cs-creative-briefing`, **nur für Motion**:
- **Dokument-Skelett:** Overview → pro Konzept: Property-Table + Strategic anchor + 3 Hooks (verschiedene Kategorien) + **VO-Script (Spine)** + time-coded Storyboard `[Time | Visual | On-Screen-Text | Voice-Over]`. **1 Angle = 1 Konzept.**
- **References lesen** (Ordner `references/` von `admkrs-cs-creative-briefing`): `creative-strategy.md` · `hook-library.md` (inkl. Kat. 16 Voss) · `copywriting.md` · `copywriting-frameworks.md` (§4b VO-Redefluss, AIDA/SLAP, BAB/DASER) · `creative-formats.md` (§5b VO-First + Gruppe D) · `voss-principles.md` · `document-format.md` · `field-notes.md` (§2b VO-Retention-Evidenz).
- **Bauen:** `node skills/admkrs-cs-creative-briefing/assets/build_briefing.js <briefing.json> <YYMMDD_BRAND_Product_Motion_LANG.docx>`. Muster: `examples/example_motion_briefing.json` (mit VO-Spine).

## Leitprinzipien (kurz)
**Hooks zuerst · VO-First & Redefluss · Klarheit vor Kunst, dann Haltung (Voss) · eine Idee pro Konzept · nichts erfinden.** Plattform-nativ, sound-off-tauglich (Captions). **Sicherheit:** nie senden/posten/löschen ohne Freigabe; vor Launch `admkrs-cs-ad-compliance-check`.

<sub>**ADMKRS Creative Suite** · © ADMKRS GmbH, München · v1.3.0 · interner Gebrauch · Format-Tür zu `admkrs-cs-creative-briefing` (gemeinsame Engine, keine Duplikate).</sub>
