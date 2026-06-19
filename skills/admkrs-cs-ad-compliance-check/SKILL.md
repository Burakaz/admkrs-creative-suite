---
name: admkrs-cs-ad-compliance-check
description: >
  Prüft Creatives, Hooks, Copy und Briefings gegen Meta Advertising Standards 2026 und
  EU/DACH-Recht, bevor sie live gehen. Use when the user wants to compliance-check an ad,
  avoid Meta rejection, review health/supplement/finance claims, handle personal-attributes
  rules, AI-disclosure, before/after, testimonials, special ad categories, or asks "ist das
  zulässig / wird das abgelehnt". High-stakes guardrail — pairs with every other bundle skill.
---

# Ad Compliance Check (Meta 2026 + EU/DACH)

Risiko-Guardrail. Meta prüft 2026 **proaktiv per AI vor der ersten Impression** — Ablehnungen kosten Lernphase und Account-Health. Dieser Skill prüft *vor* Launch. Bei rechtlichen Grenzfällen (Health/Finance/EU) ist das **keine Rechtsberatung** — im Zweifel Kunde/Anwalt einbinden.

## 1 — Personal Attributes (häufigster Ablehnungsgrund)
Ads dürfen ein persönliches Attribut der Person **nicht behaupten oder implizieren** (Gesundheit, Alter, Race, Religion, sexuelle Orientierung, Gender, Behinderung, finanzielle Lage, Vorstrafen, Name …).
- ✗ Direkt: „Bist du über 40 und hast Gelenkschmerzen?" · „Als Diabetiker verdienst du …" · „Bist du pleite?"
- ✗ Indirekt (seit März 2026 gleich streng): „Für Menschen mit Diabetes" · „Für alle ab 50".
- ✓ Erlaubt: generisches „du/dein" ohne Attribut („Du verdienst einen besseren Morgen"), benefit-fokussiert, breite Alters-/Geo-Nennung neutral.
- ⚠️ **Audience-/Custom-Audience-Namen** werden gescannt (z. B. „diabetics_retarget" hat Account-Flags ausgelöst).

## 2 — Health / Supplement / Weight-Loss / Body-Image
**Verboten:** Before/After (Gewicht/Body/Supplement) — auch **impliziert** (Produkt neben fittem Körper); gezoomte Körperteile (Fett/Cellulite/Haut); Krankheits-Heil-/Behandlungs-Claims („senkt Blutzucker"); konkrete Zahlen-Outcomes in Testimonials („−14 kg in 6 Wochen"); BMI/negative Selbstwahrnehmung; Scham/Angst-Messaging; sensationelle/medizinisch-grafische Bilder.
**Restricted (mit Auflagen):** Supplement-Ads 18+, ohne Krankheits-/Transformations-Claim; **2026: der Disclaimer „Dieses Produkt dient nicht zur Diagnose/Behandlung/Heilung/Vorbeugung von Krankheiten" muss in der Ad-Copy selbst stehen** (nicht nur LP) — sonst Auto-Ablehnung; Weight-Management ohne Mengen/Zeit-Claim. Fitness-Performance teils ok, Body-Fokus bleibt restringiert (Grauzone → Einzelfall). *Supplements: 64 % der Accounts in Q1 2026 mind. einmal geprüft (+41 % YoY).*

## 3 — Testimonials & „Results Not Typical"
Müssen typische Erfahrung abbilden; atypische Ergebnisse brauchen klare, sichtbare Offenlegung (nicht hinter „mehr"); Material Connection offenlegen; konkrete Zahlen-Claims (Health/Finance) faktisch ohne Substanziierung gebannt. ✓ „Ich fühle mich energiegeladener" meist sicher; ✗ „−18 kg, Prä-Diabetes geheilt" = Mehrfach-Verstoß.

## 4 — AI-Disclosure (2026-Pflicht)
**Kennzeichnen:** KI-generierte Produktbilder/Szenen/Hintergründe als Ad-Subjekt, Face/Body-Modifikation über Standard-Filter hinaus, synthetische Voiceovers/Audio, KI-Video, Composite mit realer Person in nie-passierter Situation. **Nicht nötig:** Farbkorrektur/Crop/Helligkeit, KI-Copy-Vorschläge, Standard-Background-Removal. Politik/Issue: Pflicht bei fotorealistischer KI realer Personen. *Undisclosed-AI ist 2026 der #3-Ablehnungsgrund (~14 %).*

## 5 — Unrealistic Outcomes & Misleading
Verboten: nicht-typische/garantierte Outcomes (Health/Weight/Beauty/Finance), Einkommensgarantien/„kündige deinen Job", **Fake-Urgency** („nur noch 3!" wenn unwahr), irreführende Vergleiche, **Ad-Claim ≠ LP** (eigener Ablehnungsgrund → `admkrs-cs-landing-page-cro`).

## 6 — Special Ad Categories (SAC)
Kredit · Beschäftigung · Wohnen · Soziale Themen/Politik. Bei Deklaration: **kein** Alters-/Gender-/PLZ-/Detailed-Demographics-/Custom-Lookalike-Targeting; min. ~25 km Radius. **2026:** proaktive AI erkennt HEC-nahe Motive (Immobilien-/Hiring-Bilder) auch **ohne** Deklaration → kann als SAC klassifiziert/zur Prüfung gehalten werden. Soziale Themen brauchen Authorized-Advertiser-Status (auch DE).

## 7 — Sensational/Graphic
Schockierende/grausame Bilder verboten — auch in Gesundheits-/Aufklärungskontext (Wunden, Organe, Gewebe). In Ads strenger als in Community-Standards.

## 8 — EU / DACH (Recht × Meta-Policy — keine Rechtsberatung)
- **EU Health-Claims-VO (EG 1924/2006):** Lebensmittel/Supplement-Health-Claims nur, wenn im EU-Register zugelassen; unzulässige Claims („boostet Immunsystem", „unterstützt Fettverbrennung") verletzen **DE-Recht UND Meta-Policy** gleichzeitig.
- **DMA:** EU-Nutzer haben Wahl zur personalisierten Werbung → kleinere addressable Audience in DE/AT/CH (First-Party-Daten wichtiger).
- **BaFin:** Finanz-Ads (Kredit/Investment) in DE brauchen Autorisierung (Meta enforced account-level).
- **Age-Gating:** manche Kategorien (Supplements/Alkohol) brauchen in DE strengere Gates als Metas 18+-Default — manuell setzen.

## Pre-Flight-Check (vor jedem Launch)
Personal-Attributes (direkt/indirekt/Audience-Name) · Before/After-impliziert? · Krankheits-/Zahlen-Health-Claim? · Supplement-Disclaimer in der Copy? · Testimonial typisch + Disclosure? · KI-Disclosure nötig? · Fake-Urgency? · Ad-Claim = LP? · SAC-Trigger (auch implizit)? · grafisch? · EU/DE-Claim zugelassen? · Age-Gate? Vorlage: `assets/templates/compliance-checklist.md`.

## Prinzipien
Im Zweifel nicht behaupten · gesperrte/freigegebene Fakten 1:1, nichts erfinden · keine Rechtsberatung (Health/Finance/EU → Kunde/Anwalt) · proaktiv prüfen, nicht auf Ablehnung warten.

## Related skills (Bundle)
Läuft als **rechtliches Gate NACH** `admkrs-cs-creative-verifier` (QA-Gate: Briefing-Treue/Handwerk/Kunde — kommt zuerst; reicht offensichtliche Health-Claim-/Claim-Mismatch-Treffer hierher weiter). Prüft Output von `admkrs-cs-creative-briefing`, `admkrs-cs-ugc-briefing` (Hooks/Scripts/Kennzeichnung), `admkrs-cs-ugc-creator-ops` (Disclosure), `admkrs-cs-offer-promo-strategy` (Preis-/Rabatt-Auslobung), `admkrs-cs-landing-page-cro` (Ad↔LP-Match). Google-Policies separat (→ `admkrs-cs-google-cross-channel`).

## Quellen (Meta Transparency Center / Business Help, Juni 2026)
Ad-Standards-Index · Personal Attributes · Health & Wellness · Sensational Content · EU-Kommission DMA (Dez 2025) · EU Health-Claims-VO. ⚠️ Drittquellen-Stats (z. B. „64 % Accounts geprüft", „14 % AI-Ablehnungen") direktional, nicht als harte Garantie.

---
<sub>**ADMKRS Creative Suite** · © ADMKRS GmbH, München · v1.1.0 · interner Gebrauch · erstellt von ADMKRS. Quellen am jeweiligen Skill-Ende; Specs/Policies an Primärquellen prüfen.</sub>
