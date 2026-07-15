---
name: admkrs-cs-video-ad-briefing
description: >
  Erstellt ADMKRS Creative Briefings für VIDEO ADS (Talking-Head, Studio/produziert, Demo,
  Before/After, VSL, Expert - gedrehtes Video) als formatiertes .docx im ADMKRS-Stil, mit
  time-coded Script/Shotlist. Use this skill when the user wants a video ad, talking-head, studio
  video, demo video, VSL, before/after video, or says "Video Ad", "Videowerbung", "VSL",
  "Talking-Head", "Spot", "Shotlist" and wants the creative briefed. Für reines UGC nutze
  admkrs-cs-ugc-briefing. Nutzt die gemeinsame Engine von admkrs-cs-creative-briefing.
---

# ADMKRS Video-Ad Briefing

Brieft **gedrehte Video-Ads** (Talking-Head, Studio/produziert, Demo, Before/After, VSL, Expert) im ADMKRS-Stil. **Format-spezifische Tür** zur ADMKRS-Briefing-Methode - Engine & References liegen in **`admkrs-cs-creative-briefing`**, hier auf **Video** gescoped.

> **Reines Creator-/UGC-Video?** → dedizierter Skill **`admkrs-cs-ugc-briefing`** (vollständiges Creator-Dokument: virale Hooks, Frameworks je Awareness, drehfertige Scripts). Dieser Skill ist für gedrehte/produzierte Video-Ads (auch VSL).

## Voice-Over / Script-Flow
Gesprochenes (VO/Dialog) ist ein **zusammenhängender Take**, kein Stakkato - Hook 0–2 s, jede Zeile zieht in die nächste, sound-off-tauglich via Captions. **VO-First ist Pflicht für jedes Konzept mit gesprochenem Wort** (Off-VO oder On-Camera-Dialog; beim Talking-Head ist das gesprochene Script der Spine): das **VO-Script (Spine)** ist das Rückgrat, steht als am Stück lesbarer Block **vor** dem time-coded Script/Shotlist und ist **wortidentisch** mit der Voice-Over-Spalte (eine Quelle, kein Drift). Begründete Ausnahme nur reine sound-on-ASMR/Cinematic (`creative-formats.md` §5b · Struktur: `document-format.md` · Vorher/Nachher: `copywriting-frameworks.md` §4b).

## Vorgehen
Folge dem Workflow aus `admkrs-cs-creative-briefing`, **nur für Video**:
- **Dokument-Skelett (keine Callouts, kein Intro):** **„Auf einen Blick"** (Ziel & Zielgruppe · **Deliverables-Zählung** · Formate · Deadline · **Assets-Link inkl. Rohmaterial/Footage** · VO & Captions · Abgabe) (**nur Zeilen mit echter Info**, fehlende Werte im Intake nachfragen, sonst Zeile weglassen; **keine Legende**) → optional Overview `[# | Title | Length | Exporte]` (ab 3+ Konzepten) → pro Konzept: h2 (ID + Titel, **kein Family-Label**) + keyvalue (**Idee** (1 Satz) · Length · Offer · VO-Direction · Music mit konkreter Referenz - **zeilenweise**, kein Target-Audience) + 3 Hooks (je Hook 2. Zeile „Visual/Clip 0–2 s: …") + **VO-Script (Spine)** (Pflicht bei gesprochenem Wort, Ausnahme nur §5b) + time-coded **Script/Shotlist** `[Time | Visual | On-Screen-Text | Voice-Over/VO]` - Visual-Spalte je nach Modus (Edit oder Dreh, siehe unten), nie vage („UGC-Shot in Küche"), **letzte Zeile = End-Card-Beat**, kein outro. **1 Angle = 1 Konzept.** Before/After: **Nachher zuerst**. Demo: Problem → Produkt greift → Ergebnis.
- **Zwei Modi für die Visual-Spalte** (im Intake klären: Footage vorhanden?): (a) **Edit-Modus** (vorhandenes Rohmaterial): **Clip-Referenz** je Beat (Dateiname/Timecode). (b) **Dreh-Modus** (Neu-Dreh): **Shot-Anweisung** je Beat - Einstellungsgröße (Close/Medium/Wide), Setup/Location, Action, ggf. Props; zusätzlich je Konzept eine Zeile **Licht/Ton/Location** in der keyvalue-Tabelle (oder einmal in „Auf einen Blick", wenn für alle Konzepte gleich).
- **VSL:** Long-Form **5–10 min** (Hook mit Bold Claim → Lead lädt das Problem → Body erklärt Problem-/Solution-Mechanism → Close mit Value-Stack + Garantie) oder **Mini-VSL 30–90 s** (komplette VSL-Logik komprimiert, ein Hauptargument pro Video). Framework: PASTOR/QUEST/Star-Story-Solution (`copywriting-frameworks.md` §2). Script-Tabelle in **Beats/Kapiteln** statt Sekunden-Takt, Length-Zeile entsprechend. Details: `creative-formats.md` §6b („Video · DR-Story, Demo & Production").
- **Format-Regel (Meta):** produziert wird 4:5 + 9:16, kein 1:1 (außer explizit gewünscht). **Im Dokument steht nur die Meta-Standard-Zeile**; Kein-1:1-/Sonderformat-Hinweise nur bei echtem Anlass (Sonderformate dann mit Plattform + Pixeln). **Bold-Konvention:** fett = landet auf dem Creative (On-Screen-Text).
- **References lesen** (Ordner `references/` von `admkrs-cs-creative-briefing`): `creative-strategy.md` · `hook-library.md` (inkl. Kat. 16 Voss) · `copywriting.md` · `copywriting-frameworks.md` (QUEST/PASTOR/Star-Story-Solution; §4b) · `creative-formats.md` (Gruppen A–C + E, §5b, §6b Video-Abschnitte inkl. VSL/Mini-VSL) · `creative-methods.md` (Video-/Short-Form-Anatomie) · `intake-questions.md` (Pflicht-Rückfragen: Assets/Footage, Deadline, Offer) · `performance-playbook.md` (DatAds-Signale vor dem Briefen, wenn der Kunde dort liegt) · `voss-principles.md` · `document-format.md` · `field-notes.md`.
- **Bauen:** `cd <Pfad zu admkrs-cs-creative-briefing>/assets && npm install docx` (einmalig pro Umgebung), dann `node build_briefing.js <briefing.json> <YYMMDD_BRAND_Product_Video_LANG.docx>` - Details: `document-format.md` („Builder ausführen"). Engine/Struktur wie Motion-Beispiel (`examples/example_motion_briefing.json`).

## Leitprinzipien (kurz)
**Hooks zuerst · gesprochener Flow statt Stakkato · Klarheit vor Kunst, dann Haltung (Voss) · eine Idee pro Konzept · nichts erfinden.** Drehfertige Visual-Direction (Specs, Ratio, Licht/Ton).
**Build-fertig & zeilenweise:** Property-/Script-Zellen zeilenweise (`\n`); **Ausführer-Test** - nur was Regie/Editor zum Bauen braucht (keine Callouts); final entschieden; fehlende Werte **nachfragen, sonst weglassen** (kein `[Platzhalter: …]` im Dokument), offene Punkte intern in ClickUp/Chat; **keine Personennamen** (Rollen statt Namen); **kein „·" als Trenner** im Dokument-Inhalt (dek, Zellen, Absätze: Kommas oder Zeilen). **Sicherheit:** nie senden/posten/löschen ohne Freigabe; Abnahme durch `admkrs-cs-creative-verifier`, dann vor Launch `admkrs-cs-ad-compliance-check`.

<sub>**ADMKRS Creative Suite** · © ADMKRS GmbH, München · v1.13.0 · interner Gebrauch · Format-Tür zu `admkrs-cs-creative-briefing` (gemeinsame Engine, keine Duplikate).</sub>
