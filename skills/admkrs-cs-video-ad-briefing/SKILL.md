---
name: admkrs-cs-video-ad-briefing
description: >
  Erstellt ADMKRS Creative Briefings für VIDEO ADS (Talking-Head, Studio/produziert, Demo,
  Before/After, VSL, Expert — gedrehtes Video) als formatiertes .docx im ADMKRS-Stil, mit
  time-coded Script/Shotlist. Use this skill when the user wants a video ad, talking-head, studio
  video, demo video, VSL, before/after video, or says "Video Ad", "Videowerbung", "VSL",
  "Talking-Head", "Spot", "Shotlist" and wants the creative briefed. Für reines UGC nutze
  admkrs-cs-ugc-briefing. Nutzt die gemeinsame Engine von admkrs-cs-creative-briefing.
---

# ADMKRS Video-Ad Briefing

Brieft **gedrehte Video-Ads** (Talking-Head, Studio/produziert, Demo, Before/After, VSL, Expert) im ADMKRS-Stil. **Format-spezifische Tür** zur ADMKRS-Briefing-Methode — Engine & References liegen in **`admkrs-cs-creative-briefing`**, hier auf **Video** gescoped.

> **Reines Creator-/UGC-Video?** → dedizierter Skill **`admkrs-cs-ugc-briefing`** (vollständiges Creator-Dokument: virale Hooks, Frameworks je Awareness, drehfertige Scripts). Dieser Skill ist für gedrehte/produzierte Video-Ads (auch VSL).

## Voice-Over / Script-Flow
Gesprochenes (VO/Dialog) ist ein **zusammenhängender Take**, kein Stakkato — Hook 0–2 s, jede Zeile zieht in die nächste, sound-off-tauglich via Captions. Bei VO-getriebenen Spots gilt **VO-First** wie bei Motion (VO-Script als Rückgrat; `creative-formats.md` §5b, `copywriting-frameworks.md` §4b).

## Vorgehen
Folge dem Workflow aus `admkrs-cs-creative-briefing`, **nur für Video**:
- **Dokument-Skelett:** Overview → pro Konzept: Property-Table + Strategic anchor + 3 Hooks + (bei VO-Spots: VO-Script-Spine) + time-coded **Script/Shotlist** `[Time | Visual | On-Screen-Text | Voice-Over/VO]`. **1 Angle = 1 Konzept.** Before/After: **Nachher zuerst**. Demo: Problem → Produkt greift → Ergebnis.
- **References lesen** (Ordner `references/` von `admkrs-cs-creative-briefing`): `creative-strategy.md` · `hook-library.md` (inkl. Kat. 16 Voss) · `copywriting.md` · `copywriting-frameworks.md` (QUEST/PASTOR/Star-Story-Solution; §4b) · `creative-formats.md` (Gruppen A–C + §5b) · `creative-methods.md` (Video-/Short-Form-Anatomie) · `voss-principles.md` · `document-format.md` · `field-notes.md`.
- **Bauen:** `node skills/admkrs-cs-creative-briefing/assets/build_briefing.js <briefing.json> <YYMMDD_BRAND_Product_Video_LANG.docx>`. Engine/Struktur wie Motion-Beispiel.

## Leitprinzipien (kurz)
**Hooks zuerst · gesprochener Flow statt Stakkato · Klarheit vor Kunst, dann Haltung (Voss) · eine Idee pro Konzept · nichts erfinden.** Drehfertige Visual-Direction (Specs, Ratio, Licht/Ton). **Sicherheit:** nie senden/posten/löschen ohne Freigabe; vor Launch `admkrs-cs-ad-compliance-check`.

<sub>**ADMKRS Creative Suite** · © ADMKRS GmbH, München · v1.3.0 · interner Gebrauch · Format-Tür zu `admkrs-cs-creative-briefing` (gemeinsame Engine, keine Duplikate).</sub>
