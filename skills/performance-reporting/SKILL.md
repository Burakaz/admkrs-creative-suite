---
name: performance-reporting
description: >
  Erstellt Creative-Performance-Reports und Weekly/Monthly Reviews für Paid Social, die
  Entscheidungen & Learnings liefern statt Vanity-Metriken. Use when the user wants a
  creative report, weekly/monthly performance review, client report, to interpret ad
  metrics (hook/hold/CTR/CVR/ROAS), understand MER vs platform ROAS, profit/contribution
  reporting, attribution 2026, or "wie reporte ich Creative-Performance". Liefert
  Report-Architektur, Metrik-Definitionen, ein Creative-Tracker-Template und Cadence.
  Pairs with creative-strategy-os (Phase 6 & 9) und creative-teardown.
---

# Performance Reporting & Weekly Review

**Der Kern in einem Satz:** Ein gutes Report sagt *was wir gelernt haben und was als Nächstes passiert* — nicht „ROAS 2,4, 1,2 Mio. Impressionen". Zahlen sind die Beweise, **Learnings + Entscheidungen** sind das Produkt. Datenquelle: DatAds (+ ggf. Triple Whale/GA4). Dieser Skill schließt Phase 6 (Diagnose) und Phase 9 (Cadence) des `creative-strategy-os`.

> **Warum das wichtig ist:** Kunden bleiben nicht wegen schöner Dashboards. Sie bleiben, wenn sie sehen, dass jemand *systematisch lernt*, was bei *ihrer* Zielgruppe zündet — und danach handelt. Reporting ist dein Retention-Tool.

---

## 1 — Der Metrik-Stack: drei Ebenen, die zusammen gelesen werden

Eine Zahl allein lügt fast immer. Lies immer **eine Ergebnis-Metrik** zusammen mit den **Diagnose-Metriken**, die erklären *warum*.

**Ebene 1 — Ergebnis (ob es funktioniert):** Spend · CPA/ROAS bzw. CPL · CVR · AOV. *Sagt dir, ob Geld verdient wird — aber nicht, woran es liegt.*

**Ebene 2 — Storytelling/Diagnose (warum es funktioniert):**
- **Thumbstop / Hook-Rate** = 3-Sek-Views ÷ Impressions (TikTok: 2 s). → diagnostiziert den **Opener/Hook**. Richtwerte (Vendor — gegen eigene Baseline messen): <25 % = Hook fixen · 25–35 % = solide · >35 % = stark.
- **Hold / Retention** = 15-Sek-Views ÷ 3-Sek-Views. → diagnostiziert den **Body** (hält das Hook-Versprechen?). Ø 40–50 %; >60 % stark; <30 % = Pacing/Struktur-Problem.
- **CTR — Link vs. Outbound:** Outbound-CTR (verlässt die Plattform Richtung LP) ist der saubere Intent-Wert. Meta-Ø Outbound ~0,9–1,5 %; >1,5 % (E-Com) stark. CTR ist **Diagnostik, kein North-Star**.
- **Completion / ThruPlay:** Narrative ≥60 %, Demo ≥75 %.

**Ebene 3 — Health-Signale:** **Frequency** (Fatigue: steigende CPA + steigende Frequenz) · **Creative-Demand-Score** (braucht der Account mehr/weniger neues Creative?).

**Worked Example (so liest man den Stack):** Ein Creative hat ROAS 1,1 (schwach). Ebene 2 zeigt: Thumbstop 42 % (top), aber Outbound-CTR 0,4 % (schwach). → **Diagnose: Hook zieht, Body/Offer versagt.** Fix = Body neu, länger im Problem bleiben vor dem Produkt-Reveal — Hook behalten. Hätte man nur den ROAS gesehen, hätte man das ganze Creative gekillt und den starken Hook mitverloren.

---

## 2 — Die Geld-Wahrheit: Plattform-ROAS lügt → MER & Profit

Plattform-ROAS (in Ads Manager) **überschätzt strukturell**: Multi-Plattform-Doppelzählung, View-Through, modellierte Conversions. Summierte Plattform-Zahlen liegen oft **30–60 % über** dem echten Umsatz. Deshalb nie allein darauf steuern — immer die Konto-Wahrheit danebenlegen.

| Kennzahl | Formel | Wofür |
| --- | --- | --- |
| **Break-even-ROAS** | 1 ÷ Marge% | ab wann profitabel (40 % Marge → 2,5) |
| **MER** (Blended) | Gesamtumsatz ÷ Gesamt-Marketing-Spend | attributions-agnostische Wahrheit aus dem P&L |
| **Blended ROAS** | Gesamtumsatz ÷ Ad-Spend | Konto-Gesamtbild |
| **aMER** | Neukunden-Umsatz ÷ Paid-Spend | Akquise-Effizienz |
| **nCAC** | Paid-Spend ÷ Neukunden | ehrlichste Scaling-Metrik (mit LTV koppeln) |
| **Contribution Margin** | Umsatz − COGS − Ad-Spend − var. Kosten | der Betrag, der wirklich übrig bleibt |

**Ziel-Heuristik:** LTV : nCAC **> 3 : 1**. Erstkauf darf unprofitabel sein, *wenn* das LTV-Modell den Payback trägt.

**Die wichtigste Diagnose-Regel:** Plattform-ROAS fällt, **MER stabil** → Attributions-/Tracking-Shift, *kein* echtes Problem. **Beide fallen** → echtes Problem (Fatigue/Sättigung/Budget). Diese eine Regel verhindert die häufigste Panik-Fehlentscheidung.

> **Modernes Framing für den Kunden:** Sprich nicht „ROAS", sprich **Profit / Contribution / nCAC**. „ROAS ist tot" ist überspitzt, aber der Punkt stimmt: skaliere auf den Deckungsbeitrag, nicht auf eine Attributions-Zahl.

---

## 3 — Attribution 2026 (was gilt gerade)

- **Meta-Default:** 7-Tage-Click + 1-Tag-View. Die **7-/28-Tage-View-Fenster wurden am 12. Jan 2026 abgeschaltet** → reported Conversions können −15–30 % gegenüber Altfenstern wirken (ist Mess-Artefakt, kein Performance-Einbruch).
- **CAPI ist Pflicht-Infrastruktur:** Server-side-Events füllen iOS-Lücken; Meta-eigene Angabe ~17–19 % mehr attribuierte Conversions vs. Pixel-only (Vendor-Zahl). Die Offline-Conversions-API ist abgeschaltet — Events laufen über CAPI.
- **Incrementality = die ehrliche Messung** (für Scaling-Entscheidungen):
  - **Conversion-Lift / Incremental-Attribution** (nur Meta-Ökosystem, Geo-/User-Split).
  - **Geo-Lift** (kanalübergreifend, Gold-Standard; Test-vs-Holdout-Regionen, 2–4 Wochen).
  Faustregel: monatlich/quartalsweise eine Incrementality-Frage stellen („wäre der Umsatz auch ohne diese Ausgabe gekommen?"), nicht jede Woche.

⚠️ Vendor-/Plattform-Zahlen (z. B. „+46 % incremental") immer als solche kennzeichnen.

---

## 4 — Die Report-Architektur (7 Teile)

Ein starker Report ist eine **Story mit Beweisen**, kein Zahlen-Dump. Reihenfolge:

1. **Executive Summary (1 Seite, in 3 Min lesbar):** Was lief, was nicht, was ändert sich. Wenn der Kunde nur das liest, muss er die Lage verstehen.
2. **Creative-Performance nach Konzept/Angle** (nicht nach Kampagnenname): Thumbnail + Hook/Hold/CTR/CVR/CPA/Spend je Creative. So sieht man *welche Idee* gewinnt.
3. **Funnel-Diagnose je Verlierer:** wo brach es (Hook/Hold/LP/Offer)? — die Diagnose aus §1.
4. **„Was wir gelernt haben"** — der wichtigste Teil. **Falsifizierbare** Sätze: *„Direct-Offer-Hooks schlugen Testimonial-Hooks 2,3× auf CVR bei Audience X."* Nicht „Video lief gut".
5. **„Was wir als Nächstes testen"** — konkrete Hypothesen, an die Learnings gekoppelt.
6. **Business-Metriken (getrennt vom Creative-Teil):** MER-Trend · Blended ROAS · nCAC · Contribution. Plattform-ROAS nie allein.
7. **„Diese Woche gekillt — und warum"** — Kunden vertrauen datengetriebenen Kill-Entscheidungen mehr als nur Erfolgsmeldungen.

Template: `assets/templates/weekly-report.md`. Operativer Test-/Asset-Tracker (woher die Zahlen kommen): `assets/templates/campaign-tracker.md`.

---

## 5 — Cadence (Rhythmus)

| Takt | Fokus | Was anschauen |
| --- | --- | --- |
| **Täglich** (nur Launch/Scaling) | Puls / Anomalien | Spend-Pacing, CPA-Ausreißer, neue Creatives angelaufen? |
| **Wöchentlich** | Creative-Entscheidungen | Metrik-Stack §1, kill/iterate/scale, Fatigue-Check |
| **Monatlich** | volle Creative-Review | Learnings, Angle-/Format-Gewinner, Demand-Score, MER-Trend |
| **Quartalsweise** | Strategie & Incrementality | Budget-Reallokation, Geo-/Conversion-Lift, LTV:CAC |

Format: **Live-Dashboard** (DatAds/Looker) für die Zahlen + **narrativer Report** (PDF/Deck) für die Story. Beides, nicht nur das Dashboard.

---

## 6 — Der Creative-Tracker (operatives Rückgrat)
Damit Reporting überhaupt möglich ist, braucht es eine saubere Test-/Asset-Dokumentation. Das `campaign-tracker.md`-Template hat: Campaign-Master → **Asset-Tracker** (Format · Concept · Angle · Hook · Creator · Status) → **Decision-Spalte** (Test/Winner/Scale/Kill) → **Hook-Rate/Hold/CTR/CVR je Asset** → Skript-Iterationen → Drehplan. Die zwei kritischen Spalten, die in vielen Trackern fehlen: **Decision** (sonst lernt niemand) und **Hook-Rate** (sonst diagnostiziert niemand). Naming-Konvention `Format_Hook_Angle_Audience` macht die Auswertung erst möglich.

---

## 7 — Tools 2026 (Orientierung, Preise vor Zitat prüfen)
**DatAds** (euer Stack — Cross-Client, Best-Hooks/Bestperformer/Deconstruction/Ads-to-Kill) · **Motion** (Creative-Analytics/Dashboards) · **Triple Whale** (Shopify-Attribution, MER, Creative Cockpit) · **Northbeam/Polar** (Multi-Touch, längere Cycles) · **Measured/Geo-Lift-Tools** (Incrementality).

## Prinzipien
Learnings vor Vanity · gegen die *eigene* Baseline lesen, nicht Branchen-Benchmark · Plattform-ROAS nie allein (MER/Profit daneben) · Vendor-Benchmarks als solche kennzeichnen · nichts erfinden · Kill-Entscheidungen transparent begründen.

## Related skills (Bundle)
`creative-strategy-os` (Phase 6 Diagnose, Phase 9 Cadence) · `creative-teardown` (Gewinner zerlegen) · `landing-page-cro` (bei CTR↑/CVR↓) · `creative-briefing` (nächste Runde aus Learnings).

## Quellen
Motion / Billo (Creative-Metriken, Juni 2026) · Triple Whale & Eightx (MER/Blended/Contribution, 2026) · TrackBee / DOJO AI / Jon Loomer (Attribution 2026, View-Fenster-Abschaltung) · Common Thread Collective (Profit-/nCAC-Reporting) · DatAds. *Vendor-Benchmarks direktional; Attributionsfenster & CAPI an Meta-Primärquelle gegenchecken.*

---
<sub>**ADMKRS Creative Suite** · © ADMKRS GmbH, München · v1.1.0 · interner Gebrauch · erstellt von ADMKRS. Quellen am jeweiligen Skill-Ende; Specs/Policies an Primärquellen prüfen.</sub>
