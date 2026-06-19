---
name: admkrs-cs-google-cross-channel
description: >
  Brieft Creatives für Google: Demand Gen, Performance Max und YouTube - mit exakten
  2026-Specs (Asset-Counts, Zeichenlimits, Ratios, Video-Längen) und Best Practices.
  Use when the user wants to create/brief Google Ads creative, Demand Gen or PMax
  asset groups, YouTube ads (in-stream/Shorts/bumper), needs Google ad specs, or wants
  to adapt Meta creative to Google. Pairs with admkrs-cs-creative-briefing und admkrs-cs-creative-strategy-os.
---

# Google Cross-Channel Creative (Demand Gen / PMax / YouTube)

ADMKRS macht Meta **und** Google. Google-Formate haben andere Specs, Asset-Gruppen und eine **Search-Intent-Schicht** - Meta-Assets lassen sich nicht 1:1 übernehmen. Specs unten = offiziell (Google Ads Help, Stand Juni 2026); vor Produktion am aktuellen Help-Center gegenchecken.

## Demand Gen - Specs
**Placements:** Discover, Gmail, YouTube (Home/Search/Watch-Next/In-stream/Shorts), GDN.
| Text | Limit | Anzahl |
| --- | --- | --- |
| Headline | 40 Zeichen | bis 5 |
| Description | 90 Zeichen | bis 5 |
| Business Name | 25 Zeichen | 1 (Pflicht) |
| CTA | 10 Zeichen | auto/manuell |

**Bilder (Rule of Three - ≥3 je Ratio):** 1.91:1 (min 600×314, empf. 1200×628, Pflicht) · 1:1 (min 300×300, empf. 1200×1200, Pflicht) · 4:5 (min 480×600, optional) · 9:16 (min 600×1067, empf. 1080×1920, Shorts). Max 5 MB. **9:16-Bild kann in DV360 abgelehnt werden → 4:5 als sicheres Vertikal.**
**Logo:** 1:1 (min 128×128, empf. 1200×1200, Pflicht), bis 5; rendert in Gmail als Kreis.
**Video:** 1–5 je Ad, **min 5 s** (unter 10 s serviert **nicht** auf YouTube In-stream; ≥15 s empfohlen). 16:9 / 1:1 / 4:5 / 9:16. Muss auf YouTube gehostet sein.
**Carousel:** 2–10 Cards, gleiche Ratio; **nicht** mit Merchant-Center-Feed kombinierbar (dafür Product-Feed-Ads). **Product-Feed-Ads:** ≥1 Produkt, ≥4 für max. Placement-Eligibility, 50+ empfohlen.

## Performance Max - Specs
| Text | Limit | Min–Max |
| --- | --- | --- |
| Headline | 30 Zeichen (≥1 ≤15) | 3–15 |
| Long Headline | 90 Zeichen | 1–5 |
| Description | 90 Zeichen | 2–5 |
| Business Name | 25 Zeichen | 1 |
| URL-Pfad | 15 Zeichen | 1–2 |
Ad-Strength „Excellent": **11+ Headlines, 2+ Long Headlines, 4+ Descriptions.**
**Bilder:** 1.91:1 & 1:1 Pflicht (je 4+, bis 20), 4:5 optional (2+); Logo 1:1 Pflicht (128×128+), 4:1 optional. Max ~5 MB.
**Video:** 16:9 / 1:1 / 9:16, **je min 10 s**, 1 je Orientierung empfohlen. **Lädst du 0 Videos hoch, generiert Google automatisch eins (nicht vorab prüf-/downloadbar)** → alle 3 Orientierungen hochladen, um das zu verhindern + „Excellent" zu erreichen.
**Asset-Gruppen:** 1–100/Kampagne, nicht teilbar, je eigene Audience-Signale.
**⚠️ Final-URL-Expansion** kann LP-URL **und** Copy dynamisch ersetzen → bei Compliance/Brand-Copy explizit deaktivieren.

## YouTube - Formate
| Format | Länge | Skip | Billing |
| --- | --- | --- | --- |
| Skippable In-stream | kein Max (empf. <3 min) | nach 5 s | CPV (30 s/voll/Interaktion) |
| Non-skippable (Standard) | 7–15 s | nein | tCPM |
| Non-skippable (CTV/erweitert) | 16–30 s | nein | tCPM |
| Bumper | max 6 s | nein | tCPM |
| In-feed | kein Max | Click-to-watch | Click/10 s-Autoplay |
| Shorts | bis 3 min (erste 60 s im Feed; <60 s empf.) | swipe | CPM/CPV/Engagement |
**Shorts:** 9:16 stark empfohlen (horizontal = Blur-Fill); Sound-on, social-first (Sound +20 % Conversions, Google). CTA-Button bei PMax/App/DG nach 3 s. **Bumper gibt es NICHT in DG/PMax** (nur Video-Reach/Reservation). „Views" heißt seit Okt 2025 „TrueView views".

## AI/Generative 2026
DG „AI Image & Video Enhancements" (Nov 2025: resize/remix/adapt aus Uploads) · DG Asset-Uplift-A/B-Experimente · Shorts „Video Enhancement" (vertikal aus horizontal) · Trim-Tool · PMax Auto-Video & Final-URL-Expansion · Shoppable CTV (DG, GA Jan 2026). Lookalikes in DG default „suggestion mode" (März 2026).

## DG/PMax vs. Meta (praktisch)
- **Search-Intent-Schicht** (PMax matcht auf Suchanfragen) - gibt es bei Meta nicht; kompensiert teils schwächere Hooks.
- Eine Kampagne bespielt viele Formate (Search/Shopping/Display/YouTube/Gmail/Discover) aus einer Asset-Gruppe.
- **Reporting gröber** (PMax nur Asset-Gruppen-Level) als Metas Ad-Level.
- Hook-Fenster: YouTube skippable = 5 s, Shorts 1–2 s; Meta unerbittlicher (erste 2–3 Frames). Trotzdem: **vertikal + Sound-on + Caption** auch hier Pflicht.

## Briefing-Hinweise
Pro Kampagne: genug Text-Assets für „Excellent" liefern; **alle 3 Video-Orientierungen** (sonst Auto-Video); Bilder in allen Pflicht-Ratios (Rule of Three); Business-Name = verifizierte Domain/Rechtsname; Final-URL-Expansion bei Brand/Compliance aus. Meta-UGC für YouTube/Shorts wiederverwendbar, aber Specs/Längen prüfen.

## Prinzipien
Exakte, aktuelle Specs (am Help-Center gegenchecken) · DG-Headline 40 ≠ PMax-Headline 30 · Auto-Generierung bewusst steuern · vertikal+Sound-on · nichts erfinden.

## Related skills (Bundle)
`admkrs-cs-creative-briefing` (Hooks/Copy je Format) · `admkrs-cs-creative-strategy-os` (Cross-Channel-Diversität) · `admkrs-cs-landing-page-cro` (Final-URL/Match) · `admkrs-cs-ad-compliance-check` (Google-Policies separat prüfen).

## Quellen (Google Ads Help, Juni 2026)
DG-Specs support.google.com/google-ads/answer/13704860 · PMax 17091269 · Video-Formate 2375464 · Shorts 16041697 · blog.google Demand-Gen-Drop (Feb 2026). ⚠️ „Non-skippable bis 60 s" mischt Format-Übersicht mit Self-Serve-Limit - praktisch 15 s (Standard)/30 s (CTV).

---
<sub>**ADMKRS Creative Suite** · © ADMKRS GmbH, München · v1.1.0 · interner Gebrauch · erstellt von ADMKRS. Quellen am jeweiligen Skill-Ende; Specs/Policies an Primärquellen prüfen.</sub>
