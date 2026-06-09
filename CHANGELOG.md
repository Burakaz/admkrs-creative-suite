# Changelog — ADMKRS Creative Suite

## v1.3.1 — 2026-06
`creative-briefing`: Klarheit hart durchgesetzt (gegen „gewollt kreative", kontext-abhängige Hooks).

- **Neue harte Tests** in `copywriting.md` §1 + Qualitäts-Check (`SKILL.md`): **Kontext-frei-Test** (jedes Substantiv konkret — kein offenes „welche Zahl/Rechnung?"), **Schachtel-Test** (ein Gedanke/Hauptsatz), **Kürzen-Pass (Pflicht)** und **Detail-Regel** (Beweise/Zahlen/Listen in Sub/USP, nicht in den Hook).
- **Neuer Abschnitt `copywriting.md` §1b „Anti-Patterns — sofort umschreiben"**: kontext-abhängiger Claim · Schachtelsatz · vage Dreierliste · gewollt kreatives Wortspiel · abstrakte Gleichsetzung — je mit Vorher/Nachher.
- **weak→strong** um Praxisfälle erweitert (u. a. „Eine Zahl im Monat…" → „Ein Fixpreis im Monat. Alles drin.").
- **hook-library.md**: Klarheits-Gate über allen Templates; kontext-freie Beispiele für Kategorien, die vorher keins hatten (Curiosity/Authority/Story/Emotional); Klarheit **über** Haltung (Voss-Kat 16).
- Leitprinzip „Klarheit vor Kunst" in `SKILL.md` verschärft (mit Beispiel). Motion-/Statics-Beispiele bauen weiter; ein vager Beispiel-Hook auf ein konkretes (verbatim) Review-Fragment korrigiert.
- **ADMKRS-Hausregel: kein langer Gedankenstrich „—" (Em-Dash)** in produzierter Copy — verankert in `copywriting.md` §8, Quality-Check (`SKILL.md`) & `ugc-briefing`. Lange „—" in den Beispiel-Briefings + Copy-Docs auf „–"/Satzzeichen umgestellt (Quell-Zitate in `field-notes.md`/`voss-principles.md` unangetastet).

## v1.3.0 — 2026-06
Format-Türen: Static / Motion / Video als eigene Skills (gleiche Engine).

- Neue **format-spezifische Einstiegs-Skills**: `admkrs-cs-static-briefing` (Statics/Carousel), `admkrs-cs-motion-ad-briefing` (Motion, **VO-First**), `admkrs-cs-video-ad-briefing` (gedrehtes Video/VSL). Sie nutzen die **gemeinsame `creative-briefing`-Engine + References 1:1** (keine Duplikate); `creative-briefing` bleibt Engine + Generalist, `ugc-briefing` deckt Creator/UGC ab. → **14 Skills**.
- Repo **öffentlich** gestellt (teilbar; LICENSE bleibt proprietär, `noindex`). Website-Hinweise entsprechend (kein Login nötig); Plugin-Weg bleibt empfohlen (Auto-Update).
- Website: neue Detailseite **`prozess.html`** — Creative Strategy als chronologischer Prozess (Schritt 0–8) mit Skill-für-Skill-Durchklick und „Was du lernst"-Takes; von der Startseite verlinkt.

## v1.2.0 — 2026-06
`creative-briefing`: Oliver-Voss-Haltung + Voice-Over-First.

- **Oliver-Voss-Haltung:** neue `references/voss-principles.md` (verifizierte Voss-Zitate, Ton-Guide, Voss-Hook-Konstruktionen, Quellen). Hook-Library um **Kategorie 16 „Haltung/Anti-Kategorie"** ergänzt. **Haltungs-/Voss-Test** in `copywriting.md` & Qualitäts-Check (Position beziehen statt Kategorie-Claim) — „Klarheit vor Kunst" bleibt explizit oberstes Gesetz. Neue **Voss-Schärfe**-Stufe im Workflow (1/2/3, Default 2; Stufe 3 → `ad-compliance-check`).
- **Voice-Over-First (Doktrin für alle Motion/Video):** das **VO-Script (Spine)** ist das führende, am Stück lesbare Element pro Konzept — VO zuerst, Storyboard mappt `Time·Visual·On-Screen` auf die VO-Beats. Schreibregeln in `creative-formats.md` §5b, Struktur in `document-format.md`, **VO-Flow-Test** im Qualitäts-Check. VO-Retention-Evidenz (Google ABCD, TikTok, Motion — Plattform-Doku vs. Practitioner getrennt) in `field-notes.md` §2b. Motion-Beispiel um VO-Spine-Blöcke erweitert.
- Recherche-basiert (parallele Multi-Agent-Recherche + Zitat-Verifikation gegen die Quell-URLs); nicht belegbare Zitate bewusst weggelassen/markiert.

## v1.1.4 — 2026-06
Anzeigename & Feinschliff.

- `displayName: "ADMKRS – Creative Strategy Suite"` in plugin.json — Plugin erscheint in der UI unter diesem Namen (technischer `name` / Install-ID bleibt `admkrs-creative-suite`).
- Website-Downloads zeigen jetzt auf `releases/latest` (kein versioniertes Nachziehen mehr nötig).

## v1.1.3 — 2026-06
Motion-Ad-Voice-over: Pflicht + Redefluss statt Stakkato.

- **Regel** in `creative-briefing` (SKILL.md, `copywriting-frameworks.md` §4b, `document-format.md`): Motion Ads laufen **immer mit Voice-over**, und das VO muss ein **zusammenhängender, natürlich gesprochener Take** sein, der die Zielgruppe abholt — keine aneinandergereihten Schlagwörter/Slogans. Jede VO-Zeile knüpft an die vorige an; inkl. Vorher/Nachher-Beispiel.
- **Motion-Beispiel-JSON** (`example_motion_briefing.json`): alle 4 Storyboard-VOs von Stakkato auf echten Redefluss umgeschrieben (das Beispiel prägte den Output am stärksten).

## v1.1.2 — 2026-06
Dateinamen-Konvention & Ablage-Best-Practice für generierte Dokumente.

- **Dateiname-Konvention** in `creative-briefing` & `ugc-briefing`: `YYMMDD_BRAND_Product_Type_LANG` — Datum (YYMMDD) immer zuerst (chronologisch sortierbar), **Markt/Sprache am Ende** (`DE`/`EN`/`NL`/`FR`/`AT`), z. B. `260608_NOVA_ProteinCoffee_Statics_DE`.
- **Best Practice:** fertiges .docx in **Google Drive** im Kunden-Ordner unter „Briefings" ablegen (aus Cowork), nicht nur lokal — Speichern/Verschieben in der Kunden-Drive ok, kein ungefragtes Posten in Slack/ClickUp.
- Website: Titel „ADMKRS Creative Strategy Suite" + Tagline; Aktivierung per Satz („Nutze die ADMKRS Creative Suite") erklärt; Claude-Code-Weg eingeklappt/als optional markiert; Cowork-Drive-Ablage ergänzt.

## v1.1.1 — 2026-06
Einheitliches Namens-Schema: alle 11 Skills tragen jetzt den Prefix **`admkrs-cs-`** (z.B. `admkrs-cs-creative-briefing`), damit sie in Claude sauber als ADMKRS-Suite gruppiert auftauchen und mit `/admkrs` gefiltert werden können.

- Ordnernamen, `name:`-Felder und alle internen Querverweise konsistent auf den Prefix umgestellt.
- Team-Website, README & Download-Pakete entsprechend aktualisiert (Skill-Aufruf jetzt z.B. `/admkrs-cs-creative-briefing`).
- Keine inhaltlichen Skill-Änderungen — reines Rename/Branding.

## v1.1.0 — 2026-06
Neuer Skill **ugc-briefing** (11. Skill): generiert ein vollständiges UGC-Creator-Briefing als ADMKRS-.docx (B4 Querformat) — ein Dokument für Creator UND Kunden zugleich.

- **Brand-Foundation + Dual-Purpose-Layer:** Brand-Vorstellung & Datengrundlage für den Creator, Strategie-/KPI-Layer für den Kunden — in einem Dokument.
- **Hook-Bank** (verbal/visuell/Text/Audio) + **Out-of-the-box-/Scroll-Breaker-Layer** (Comment-Reply, Green-Screen, Street-Interview, POV-Skit, Expectation-vs-Reality …).
- **Storytelling-Frameworks** (18) gemappt auf Schwartz-Awareness, Produkt-Typ & Branche + Quick-Selector.
- **Virale Mechaniken 2026** (IG/TikTok/Shorts): Algorithmus-Signale, Share-/Save-Psychologie, Hook-Fenster, Musik-Rechte, Mythen-Check — verifiziert & quellengelabelt.
- **Drehfertige time-coded Scripts** (3 Hooks · 1 Body) + Creator-Delivery-Craft + Disclosure (DE/EU/FTC).
- Reuse der **identischen B4-Builder-Engine** wie creative-briefing; vollständiges fiktives Beispiel (NOVA · Protein Coffee).
- Cross-Refs zu ugc-creator-ops, creative-briefing, ad-compliance-check, performance-reporting.

## v1.0.0 — 2026-06
Erstes Release. 10 verzahnte Skills für Paid-Social- & Google-Creative-Strategy:
creative-strategy-os, creative-briefing, creative-teardown, performance-reporting,
landing-page-cro, ugc-creator-ops, pitch-teardown, google-cross-channel,
offer-promo-strategy, ad-compliance-check.

- Verifizierte 2026-Faktenbasis (Multi-Agent-Recherche + Fact-Check), Vendor-Zahlen markiert.
- Vollständige Creative-Format-Bibliothek (Video + Static) inkl. Style-Decoder & Diversitäts-Matrix.
- Operating-Methods (Research, Volumen, 60/30/10, ASC/Cost-Cap/CAPI/Modular-Testing, Scaling).
- Performance-Reporting (Profit/MER, Attribution 2026, Report-Architektur, Campaign-Tracker).
- 100 % kundenfrei (nur fiktive Beispielmarke „NOVA").
