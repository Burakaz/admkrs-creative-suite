---
name: admkrs-cs-creative-teardown
description: >
  Zerlegt fremde und eigene Werbe-Creatives systematisch und baut Swipe-Files mit
  übertragbaren Insights. Use when the user wants to analyze/teardown a competitor's
  ads, deconstruct a winning ad, read the Meta Ad Library, build a swipe file, or
  understand "warum funktioniert diese Ad". Liefert die 6-Pass-Teardown-Methode,
  ein Longevity=Winner-Scoring für die Meta Ad Library (2026) und ein
  Swipe-File-System. Pairs with admkrs-cs-creative-strategy-os (Audit) und admkrs-cs-creative-briefing.
---

# Creative Teardown & Swipe

Aus fremden und eigenen Gewinner-Ads lernen - strukturiert, nicht nach Bauchgefühl. Output: ein wiederholbares Teardown + ein Swipe-File mit übertragbaren Mustern, das Audit (OS) und Briefing füttert. Wichtig: Die Ad Library zeigt **kein** Performance-Daten - wir lesen *Signale* (v. a. Laufzeit), keine Wahrheiten.

## Wann nutzen
Onboarding/Audit einer Brand · Konkurrenz verstehen · Pitch-Vorbereitung · ein eigenes Gewinner-Creative für Iteration zerlegen · Swipe-File für eine Kategorie aufbauen.

## Die 6-Pass-Teardown-Methode
Das Creative **sechsmal** ansehen, je mit einem Fokus (nach Mirella Crespi / Motion):
1. **Concept/Angle** - Was ist die zentrale Verkaufsidee? Pain oder Aspiration? Welcher emotionale Trigger? Positionierung (besser-für-weniger / mühelos / Social Proof / Curiosity-Gap)?
2. **Hook (0–3 s)** - Frame für Frame: Was stoppt den Daumen (Visual/Audio/Text)? Welche Emotion in 1–3 s? Hook-Kategorie: Problem-Aware · Benefit-Led · Social Proof · Direct Offer · Curiosity · Comparison.
3. **Script/Ad-Blocks** - Body in Bausteine zerlegen (Problem → Solution → Demo → CTA ist *eine* Sequenz, nicht die einzige). Reihenfolge & Warum.
4. **Visuals** - Shot-Typen (UGC, Demo, Talking-Head, Green-Screen, Split-Screen), Text-Treatment (native vs. Brand-Fonts, animiert), Transitions.
5. **Pacing** - Cut-Frequenz, Copy pro Sekunde, Energie-Kurve; abrupte Pacing-Brüche = Drop-off.
6. **Congruency** - CTA klicken: Hält die Landingpage das Hook-Versprechen? Bruch = Conversion-Killer (und bei Konkurrenz: ausnutzbare Schwäche). Vertiefung: `admkrs-cs-landing-page-cro` (Konkurrenz: Schwäche dokumentieren; eigene Ads: CRO-Audit fahren).

**Static/Carousel-Mapping** (Passes 1 + 6 identisch): Pass 2 = Erst-Fixation statt 0–3 s - wo landet das Auge zuerst, ist der Hook im Feed auf Handy-Größe lesbar? Pass 3 = Text-Hierarchie + Subtraktions-Test - welche Zeile macht welchen Job, welche kann weg, ohne dass die Ad zusammenbricht? Pass 4 = Bildsprache (Produkt/Lifestyle/UGC-Foto/Grafik), Text-Treatment, Badges/Preis-Elemente. Pass 5 = Blickführung statt Pacing - in welcher Reihenfolge liest man die Elemente, führt ein klarer Pfad zum CTA? Carousel zusätzlich: Karte 1 = Hook; trägt jede Karte auch allein?

Für die strukturierte Ausgabe: `assets/templates/teardown-template.md`. (Format-/Hook-Taxonomien tiefer in `admkrs-cs-creative-briefing` → `references/field-notes.md`.)

## Meta Ad Library 2026 - was sie zeigt & wie man sie liest
- URL: facebook.com/ads/library - kostenlos, kein Login. Alle aktiven Ads je Page, durchsuchbar nach Marke/Keyword; Format, Primary Text, Headline, CTA, Placement, **Startdatum** (= Laufzeit-Signal).
- **Seit Jan 2026:** jede Ad trägt einen groben **Impression-Range-Bucket** (<1K / 1K–5K / … / 1M+), filter- und sortierbar - großes Upgrade.
- **EU/DSA-Transparenz** (kommerziell, aktiv): Targeting-Parameter (Ort/Alter/Geschlecht), demografische Reichweite, Zahler/Begünstigter, 1 Jahr archiviert - granularer als außerhalb EU.
- **Zeigt NICHT:** CTR, ROAS, Conversions, exakten Spend (kommerziell), Audience-Größe, A/B-Ergebnisse.
- **Hinweis (korrekt zitieren):** Politische/Issue-Ads sind in der EU seit Okt 2025 ausgesetzt (TTPA) - deren Spend-Daten werden nicht mehr generiert. Für kommerzielle Kunden irrelevant.
- **Bedienung fürs Scoring:** Page-Suche (exakte Brand) für Teardowns, Keyword-Suche für Kategorie-Scans. Long-Runner finden: auf aktive Ads filtern und per Datums-Filter ältere Startzeiträume prüfen. Varianten zählen: fasst Meta mehrere Versionen unter einer Ad zusammen, zählt das als 1 Ad mit n Varianten; separate Ads desselben Angles zusätzlich addieren. Länder: in der Ad-Detail-Ansicht über die EU-Transparenz-Sektion ablesen.

## Longevity = Winner (Signal-Scoring)
Marken halten verlierende Ads selten lange - **Laufzeit ist das beste öffentliche Signal**. 5 Signale, je 1–3 Punkte (max 15); **9+ = wahrscheinlicher Winner zum Remixen** (nach HeyOz, ADMKRS-adaptiert: Impression-Bucket statt des redundanten „Überlebt seit"):
| Signal | 1 | 2 | 3 |
| --- | --- | --- | --- |
| Laufzeit | <14 T | 14–30 T | 30+ T |
| Varianten | 1 | 2–4 | 5+ |
| Länder | 1 | 2–4 | 5+ |
| Impressionen (Bucket) | <10K | 10K–100K | 100K+ |
| Format-Vielfalt | 1 | 2 | 3+ |
Die Impressions-Schwellen sind ADMKRS-Faustwerte, keine Meta-Vorgabe - an die Zielmarkt-Größe relativieren (Nischen-B2B erreicht 100K+ selten, Mass-Market-D2C schnell). Optionales Langzeit-Signal on top: Datum der Erstsichtung notieren, nach 2 und 4 Wochen re-checken; läuft die Ad dann noch, wiegt das Laufzeit-Signal doppelt schwer.
Faustregeln: **30 Tage = wahrscheinlich profitabel · 60 = bewiesen · 90 = evergreen.** 5+ Varianten desselben Angles = skaliert aktiv; 10+ = Top-Performer. *Es bleibt ein Signal, kein Beweis - Laufzeit kann auch Trägheit sein.*

## Swipe-File-System
Speichere nicht „schöne Ads", sondern **Muster**: Angle · Hook-Kategorie · Format · Proof-Typ · Longevity-Score · „warum es funktioniert" + Quelle/Datum. Tag nach Kategorie/Brand, damit es im Briefing auffindbar ist. Tools (eine Zeile): **Foreplay** (Swipe + Brief, ~$149–175/mo), **Atria** (AI-Grading A–D auf $1B+ Spend, ~$129/mo), **Motion** (Performance-Reporting, ab ~$250/mo), **TikTok Creative Center / Top Ads** (frei, TikTok-Trends), **Meta Ad Library MCP** (open source, automatisierte Scans). Tool-Preise vor Zitat verifizieren.

**Agentur-Standard (Ablage, Pflege, Retrieval):** Ein fester Ablageort pro Kunde (Drive-Ordner „Swipe" oder Foreplay-Board je Kategorie), Einträge nach Schema `Kategorie_Brand_Angle_Datum`. Pflege als wiederkehrender 15–30-min Review-Slot (z. B. wöchentlich) statt Ad-hoc-Sammeln. Retrieval ist ein expliziter Schritt im Briefing-Intake: Swipe-File nach Kategorie-/Angle-Tags durchsuchen und 1–2 Referenzen mit „warum es wirkt" ins Briefing ziehen.

## Prinzipien
Signale lesen, nicht Wahrheiten behaupten · Muster extrahieren, nicht Ads kopieren (Marken-/Urheberrecht) · jeder Teardown endet mit *einer übertragbaren Hypothese* fürs nächste Briefing · nichts erfinden.

## Related skills (Bundle)
`admkrs-cs-creative-strategy-os` (Audit/Bottleneck) · `admkrs-cs-creative-briefing` (Teardown → Briefing) · `admkrs-cs-landing-page-cro` (Vertiefung von Pass 6: LP-Audit) · `admkrs-cs-pitch-teardown` (Teardown als Sales-Asset) · `admkrs-cs-ad-compliance-check` (bevor man fremde Hooks adaptiert).

## Quellen
Motion - Competitor Ads Analysis (Crespi) · HeyOz - Meta Ad Library Spy System (Apr 2026) · Meta Ad Library (facebook.com/ads/library) · about.fb.com (EU/DSA, Okt 2025). *Sekundärquellen direktional; Specs/Policies an Meta gegenchecken.*

---
<sub>**ADMKRS Creative Suite** · © ADMKRS GmbH, München · v1.13.0 · interner Gebrauch · erstellt von ADMKRS. Quellen am jeweiligen Skill-Ende; Specs/Policies an Primärquellen prüfen.</sub>
