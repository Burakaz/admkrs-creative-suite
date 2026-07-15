---
name: admkrs-cs-landing-page-cro
description: >
  Brieft und auditiert Landingpages / Post-Click-Erlebnisse für Paid Social & DTC
  auf Conversion. Use when the user wants to improve a landing page, audit an LP,
  fix low CVR / "high CTR but low conversions", build an LP brief, message-match a
  page to an ad, reduce checkout/form friction, or improve page speed for conversion.
  Evidence-based (Baymard, NNGroup, Google web.dev). Pairs with admkrs-cs-creative-briefing
  und admkrs-cs-performance-reporting (Diagnose CTR-hoch/CVR-niedrig = LP).
---

# Landing Page / Post-Click CRO

Der meistunterschätzte Hebel: Wenn die CTR gut ist, aber die CVR schwach, ist die **Landingpage** der Hauptverdächtige - aber nicht automatisch der Täter. Vor dem LP-Verdikt drei Dinge prüfen: (1) **Hook-Intent** - lockt der Hook Klicks ohne Kaufabsicht (Curiosity/Clickbait)? Dann ist die Ad das Problem. (2) **Overpromise** - verspricht die Ad etwas, das keine LP halten kann (Message-Match-Bruch verursacht durch die Ad)? Dann Ad fixen, nicht LP. (3) **Tracking intakt?** Erst danach LP-Audit. Dieser Skill brieft und auditiert die Seite - evidenzbasiert, mit klarer Trennung von belegt vs. Vendor-Behauptung.

## Wann nutzen
Diagnose „hohe CTR + niedrige CVR" (aus `admkrs-cs-performance-reporting`) · neue Kampagne braucht eine passende LP · bestehende LP/PDP auditieren · Advertorial vs. dedizierte LP vs. PDP entscheiden.

## 1 - Ad-to-LP Message-Match (der #1-Hebel)
Der Klick erzeugt einen mentalen Vertrag; die LP muss ihn in 2–3 s einlösen. **Erstes Frame der LP spiegelt den Hook der Ad** - Headline, Visual, Offer. Sagt die Ad „278 Gründer nutzen X", steht das in der Hero-Zeile; zeigt die Ad ein Produkt im Einsatz, ist das Hero-Bild dieselbe Szene. Dedizierte LPs schlagen generische PDPs für Cold-Paid-Traffic verlässlich (Mechanismus: Fokus, keine Navigation/Ablenkung; in A/B-Tests ~1,7–2× CVR - Effektgröße variiert, Quellen teils Vendor).

## 2 - Above-the-Fold & Mobile-First
Meta-Paid-Traffic ist in der Praxis fast ausschließlich mobil - deutlich über dem allgemeinen Web-Schnitt (genaue Verteilung je Account im Ads Manager prüfen, Aufschlüsselung nach Gerät). Konsequenz: Die LP wird auf dem Phone gebaut und abgenommen, Desktop ist die Ausnahme. Above-the-fold muss ohne Scrollen leisten: (1) Message-Match bestätigen, (2) Value-Prop, (3) tappbarer CTA. NNGroup: **57 % der Betrachtungszeit über dem Fold**, ~74 % in den ersten zwei Screens. *Mythos „der Fold ist tot":* Nutzer scrollen nur, wenn der Hook über dem Fold sie dazu bringt.

## 3 - Page Speed / Core Web Vitals (2026-Schwellen, Google)
| Metrik | Gut | Verbesserungswürdig | Schlecht |
| --- | --- | --- | --- |
| LCP | ≤2,5 s | 2,5–4,0 s | >4,0 s |
| INP | ≤200 ms | 200–500 ms | >500 ms |
| CLS | ≤0,1 | 0,1–0,25 | >0,25 |
(75. Perzentil; Stand web.dev Mai 2025, keine Änderung 2026.) Dokumentierte Fälle (Google web.dev Case Studies): LCP −31 % → +8 % Sales (Vodafone IT); LCP halbiert → −50 % Bounce (NDTV); CLS/LCP-Fixes → −15 % Bounce (AliExpress). ⚠️ „1 s Delay = 7 % weniger Conversions" ist eine oft wiederholte, **nicht primär belegte** Faustregel - direktional nutzen.

## 4 - Checkout- & Form-Friction (Baymard, Primärquelle)
Cart-Abandonment-Ø (41 Studien): **~70 %** (direktional). Top-Abbruchgründe (Baymard 2025): **unerwartete Zusatzkosten 48 %** · Zwangs-Account 25 % · langsamer/komplizierter Checkout 18 % · Misstrauen Zahlung 17 %. Ø-Checkout zeigt ~23 Formfelder; optimal **12–14 Elemente** (7–8 echte Felder, Guest-Checkout). Checkout-UX-Fixes haben **Potenzial** für ~+35 % CVR (Baymard - Potenzial über fixbare Issues, **keine Garantie** je Einzelmaßnahme). Aktionen mit Evidenz: Guest-Checkout, Address-Autocomplete, Inline-Validierung, transparente Gesamtkosten **vor** dem letzten Schritt.

**Paid-Social-Spezifika (Praxis-Alltag der Meta-Agentur):** Meta-Klicks landen im **In-App-Browser** (WebView), nicht im Standard-Browser: Autofill ist eingeschränkt, bestehende Logins/Sessions fehlen oft, Performance kann abweichen - die LP genau dort testen (Ad-Vorschau aufs eigene Handy), nicht nur in Safari/Chrome. **Express-Wallets** (Apple Pay, Shop Pay, PayPal Express) prominent im Checkout anbieten: sie umgehen Formfelder und Zwangs-Account gleichzeitig und sind damit einer der stärksten Friction-Hebel im DTC-Checkout. **Consent-Banner** mobil auf Ein-Tap-Akzeptanz prüfen (verdeckt es CTA/Content?): schlechte Consent-UX kostet doppelt - Nutzererlebnis und Signalqualität (Pixel/CAPI, Attribution).

## 5 - Social Proof, Offer, Urgency, Risk-Reversal
- **Social Proof:** spezifische, quantifizierte Testimonials (Name, konkretes Ergebnis, Foto) > anonyme Sterne; UGC-Fotos nahe CTA. ⚠️ „UGC +102 % CVR" (PowerReviews) ist **Interaktions-Lift**, kein Site-Lift - nicht als Garantie.
- **Offer-Klarheit:** Versandkosten/Steuern/Gesamtpreis früh zeigen (unerwartete Kosten = #1-Abbruchgrund).
- **Urgency:** echte Limits wirken; **Fake-Countdowns** schaden Vertrauen (und sind regulatorisch riskant).
- **Risk-Reversal:** Geld-zurück-Garantie senkt wahrgenommenes Risiko (Loss-Aversion), v. a. bei unbekannten Marken/hohem Preis.

## 6 - Seitentyp wählen
**Dedizierte LP** für Cold-Paid (keine Exits außer Conversion). **PDP** eher für warm/Intent. **Advertorial** (redaktionelle Pre-Sell-Seite) für High-Consideration/Supplements/skeptische Audiences - wärmt vor und entschärft Claim-/Compliance-Risiko (→ `admkrs-cs-ad-compliance-check`). Kontext-abhängig, keine Universal-Regel. Aufbau je Seitentyp: `references/lp-brief-blueprint.md`.

## 7 - Messen & Diagnose (das WIE)
- **CWV messen:** PageSpeed Insights bzw. CrUX-**Felddaten** (mobil, 75. Perzentil) - nicht den Lighthouse-Laborscore als Wahrheit nehmen (Labor ≠ echte Nutzer). Zusätzlich die LP im Meta-In-App-Browser öffnen (siehe Sektion 4).
- **Funnel-Leck lokalisieren:** LP-View → Add-to-Cart → Checkout-Start → Purchase in GA4/Shop-Backend nebeneinanderlegen. ATC niedrig = LP-Problem (Message-Match, Fold, Offer). ATC ok, aber Purchase bricht ein = Checkout-Problem (Kosten-Transparenz, Felder, Wallets). Alles niedrig trotz guter CTR = zurück zur Differentialdiagnose oben (Hook-Intent, Overpromise, Tracking).
- **Verhalten sehen:** Session-Recordings und Heatmaps (z. B. Microsoft Clarity, Hotjar) für Scroll-Depth, Rage-Clicks, Formular-Abbrüche - als Diagnose-Werkzeug, nicht als Beweis.
- **Test-Hygiene:** A/B-Test nur mit vorher festgelegter Erfolgsmetrik und Laufzeit, ausreichend Conversions je Variante (Größenordnung: hunderte, nicht dutzende), kein tägliches Reinschauen mit frühem Abbruch (Peeking). Bei Low-Traffic-Accounts: eine große Änderung Pre/Post testen und das Ergebnis als Indiz werten, nicht als Beweis - ehrlicher als ein unterpowerter A/B-Test.

## Myth-Check (belegt vs. Mythos)
Fold irrelevant → **Mythos** · „lang schlägt kurz immer" → kontextabhängig · Fake-Countdown lift → schadet · „mehr Social Proof ist besser" → Platzierung/Spezifik schlägt Menge · Single-CTA auf Cold-LP → meist besser · Hero-Autoplay-Video → unbelegt universell (kann LCP/CVR schädigen) · Guest-Checkout optional → **falsch** (25 % brechen wegen Zwangs-Account ab).

## Vorgehen (kurz)
Audit: Message-Match → Above-fold (mobil) → CWV messen (Sektion 7) → Social-Proof/Offer-Klarheit → Checkout-Friction (Felder, Guest, Wallets, Kosten-Transparenz) → Seitentyp. Checkliste: `assets/templates/lp-audit-checklist.md`. Neue LP briefen: `references/lp-brief-blueprint.md` (Sektions-Anatomie je Seitentyp + Brief-Skelett).

## Prinzipien
Belegt vs. Vendor klar trennen · auf eigener Seite testen statt fremde Benchmarks glauben · Message-Match zuerst · mobil zuerst · nichts erfinden.

## Related skills (Bundle)
`admkrs-cs-performance-reporting` (Diagnose CTR↑/CVR↓ → LP) · `admkrs-cs-creative-briefing` (LP muss Hook spiegeln) · `admkrs-cs-offer-promo-strategy` (Offer-Darstellung) · `admkrs-cs-ad-compliance-check` (Advertorials/Claims) · `admkrs-cs-creative-verifier` (Abgrenzung: der Verifier prüft nur die *faktische* Claim-Deckung Ad↔LP; das *Message-Match fürs CVR* - spiegelt die Hero den Hook - gehört hierher).

## Quellen
Baymard Institute (Cart/Checkout) · NNGroup (Fold/Attention) · Google web.dev (Core Web Vitals, Case Studies) · Unbounce (CVR-Benchmarks, Vendor) · Scale Messaging (LP-vs-PDP-Test). *Vendor-Daten als solche markiert; auf eigener Seite verifizieren.*

---
<sub>**ADMKRS Creative Suite** · © ADMKRS GmbH, München · v1.13.0 · interner Gebrauch · erstellt von ADMKRS. Quellen am jeweiligen Skill-Ende; Specs/Policies an Primärquellen prüfen.</sub>
