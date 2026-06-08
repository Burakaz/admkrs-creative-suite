# Changelog — ADMKRS Creative Suite

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
