---
name: admkrs-cs-ad-compliance-check
description: >
  Prüft Creatives, Hooks, Copy und Briefings gegen Meta Advertising Standards 2026 und
  EU/DACH-Recht, bevor sie live gehen. Use when the user wants to compliance-check an ad,
  avoid Meta rejection, review health/supplement/finance claims, handle personal-attributes
  rules, AI-disclosure, before/after, testimonials, special ad categories, or asks "ist das
  zulässig / wird das abgelehnt". Also covers Streichpreis/Rabatt-Recht (§ 11 PAngV,
  Fake-Urgency/UWG), DSA-Targeting-Grenzen, permission-gated categories (gambling, dating,
  crypto, pharmacy, alcohol) und den Umgang mit Ablehnungen. High-stakes guardrail - pairs
  with every other bundle skill.
---

# Ad Compliance Check (Meta 2026 + EU/DACH)

Risiko-Guardrail. Meta prüft 2026 **proaktiv per AI vor der ersten Impression** - Ablehnungen kosten Lernphase und Account-Health. Dieser Skill prüft *vor* Launch. Bei rechtlichen Grenzfällen (Health/Finance/EU) ist das **keine Rechtsberatung** - im Zweifel Kunde/Anwalt einbinden.

## 1 - Personal Attributes (häufigster Ablehnungsgrund)
Ads dürfen ein persönliches Attribut der Person **nicht behaupten oder implizieren** (Gesundheit, Alter, Race, Religion, sexuelle Orientierung, Gender, Behinderung, finanzielle Lage, Vorstrafen, Name …). Trennlinie (Metas eigene Beispiele, s. Quellen): **Zuschreibung an den Betrachter = verboten. Beschreibung von Produkt/Angebot/Zielgruppe = erlaubt.**
- ✗ Zuschreibung direkt: „Bist du über 40 und hast Gelenkschmerzen?" · „Hast du Diabetes?" · „Bist du pleite?"
- ✗ Zuschreibung indirekt (v. a. „andere/other"-Konstruktionen): „Triff andere Senioren" · „Als Diabetiker verdienst du …" - impliziert, dass der Betrachter das Attribut hat.
- ✓ Produkt-/Angebotsbeschreibung: „Neue Diabetes-Behandlung verfügbar" · „Ein Service für Senioren" · „Kurse für 50+" · generisches „du/dein" ohne Attribut („Du verdienst einen besseren Morgen"), benefit-fokussiert.
- ⚠️ Grauzone „Für Menschen mit Diabetes": von Metas Beispielen gedeckt ist die Angebotsbeschreibung („Diabetes-Beratung verfügbar"), nicht die Anrede des Betrachters. ADMKRS-konservativ: je näher die Copy an „du hast X" rückt, desto eher als Produktbeschreibung umformulieren.
- ⚠️ **Audience-/Custom-Audience-Namen** werden gescannt (z. B. „diabetics_retarget" hat Account-Flags ausgelöst).

## 2 - Health / Supplement / Weight-Loss / Body-Image
**Verboten:** Before/After (Gewicht/Body/Supplement) - auch **impliziert** (Produkt neben fittem Körper); gezoomte Körperteile (Fett/Cellulite/Haut); Krankheits-Heil-/Behandlungs-Claims („senkt Blutzucker"); konkrete Zahlen-Outcomes in Testimonials („−14 kg in 6 Wochen"); BMI/negative Selbstwahrnehmung; Scham/Angst-Messaging; sensationelle/medizinisch-grafische Bilder.
**Restricted (mit Auflagen):** Supplement-Ads 18+, ohne Krankheits-/Transformations-Claim; Weight-Management ohne Mengen/Zeit-Claim. Fitness-Performance teils ok, Body-Fokus bleibt restringiert (Grauzone → Einzelfall).
**Disclaimer** („Dieses Produkt dient nicht zur Diagnose/Behandlung/Heilung/Vorbeugung von Krankheiten"): in Metas Health-&-Wellness-Policy **nicht als Pflicht in der Ad-Copy belegt** (Stand Abruf 07/2026, s. Quellen). ADMKRS-konservative Empfehlung bei claim-nahen Supplement-Ads: Disclaimer sichtbar ans Ende des Primary Text oder als on-creative Fußzeile, mindestens auf der LP. Das ist Risiko-Reduktion, keine bestätigte Meta-Regel mit Auto-Ablehnung. *Erfahrungswert: Supplement-Accounts werden überdurchschnittlich oft proaktiv geprüft; belastbare öffentliche Prüfquoten existieren nicht.*

## 3 - Testimonials & „Results Not Typical"
Müssen typische Erfahrung abbilden; atypische Ergebnisse brauchen klare, sichtbare Offenlegung (nicht hinter „mehr"); Material Connection offenlegen; konkrete Zahlen-Claims (Health/Finance) faktisch ohne Substanziierung gebannt. ✓ „Ich fühle mich energiegeladener" meist sicher; ✗ „−18 kg, Prä-Diabetes geheilt" = Mehrfach-Verstoß.

## 4 - AI-Disclosure (2026-Pflicht)
**Kennzeichnen:** KI-generierte Produktbilder/Szenen/Hintergründe als Ad-Subjekt, Face/Body-Modifikation über Standard-Filter hinaus, synthetische Voiceovers/Audio, KI-Video, Composite mit realer Person in nie-passierter Situation. **Nicht nötig:** Farbkorrektur/Crop/Helligkeit, KI-Copy-Vorschläge, Standard-Background-Removal. Politik/Issue: Pflicht bei fotorealistischer KI realer Personen. *Fehlende AI-Kennzeichnung ist in der Praxis ein häufiger Ablehnungsgrund; belastbare öffentliche Quoten existieren nicht.*

## 5 - Unrealistic Outcomes & Misleading
Verboten: nicht-typische/garantierte Outcomes (Health/Weight/Beauty/Finance), Einkommensgarantien/„kündige deinen Job", **Fake-Urgency** („nur noch 3!" wenn unwahr), irreführende Vergleiche, **Ad-Claim ≠ LP** (eigener Ablehnungsgrund → `admkrs-cs-landing-page-cro`).

## 6 - Special Ad Categories (SAC)
Kredit · Beschäftigung · Wohnen · Soziale Themen/Politik. Bei Deklaration: **kein** Alters-/Gender-/PLZ-/Detailed-Demographics-/Custom-Lookalike-Targeting; min. ~25 km Radius. **2026:** proaktive AI erkennt HEC-nahe Motive (Immobilien-/Hiring-Bilder) auch **ohne** Deklaration → kann als SAC klassifiziert/zur Prüfung gehalten werden. Soziale Themen brauchen Authorized-Advertiser-Status (auch DE).

## 7 - Sensational/Graphic
Schockierende/grausame Bilder verboten - auch in Gesundheits-/Aufklärungskontext (Wunden, Organe, Gewebe). In Ads strenger als in Community-Standards.

## 8 - EU / DACH (Recht × Meta-Policy - keine Rechtsberatung)
- **EU Health-Claims-VO (EG 1924/2006):** Lebensmittel/Supplement-Health-Claims nur, wenn im EU-Register zugelassen; unzulässige Claims („boostet Immunsystem", „unterstützt Fettverbrennung") verletzen **DE-Recht UND Meta-Policy** gleichzeitig.
- **DMA:** EU-Nutzer haben Wahl zur personalisierten Werbung → kleinere addressable Audience in DE/AT/CH (First-Party-Daten wichtiger).
- **DSA (VO (EU) 2022/2065):** keine Werbung auf Basis von Profiling mit sensiblen Datenkategorien wie Gesundheit, Religion, sexueller Orientierung (Art. 26 Abs. 3) und keine profiling-basierte Werbung an Minderjährige (Art. 28 Abs. 2). Betrifft auch Custom-Audience-Quellen (z. B. Health-Quiz-Leads) - nicht darauf verlassen, dass Meta alles automatisch blockt. Querverweis Sektion 1 (Audience-Namen-Scanning).
- **BaFin:** Finanz-Ads (Kredit/Investment) in DE brauchen Autorisierung (Meta enforced account-level).
- **Preis- & Rabatt-Auslobung (DACH):** Streichpreis/Rabatt muss sich auf den **niedrigsten Gesamtpreis der letzten 30 Tage** beziehen (§ 11 PAngV); UVP nur, wenn real und aktuell; Countdown/Verknappung nur bei echter Begrenzung - die unwahre „nur für kurze Zeit"-Angabe ist per UWG-Anhang Nr. 7 stets unzulässig (Abmahnrisiko unabhängig von Meta); Sternchen-Hinweise sichtbar auflösen. Angebots-Mechanik → `admkrs-cs-offer-promo-strategy`.
- **Influencer-/Creator-Kennzeichnung (DE):** kommerziellen Zweck klar kenntlich machen: „Werbung"/„Anzeige" am Anfang, nicht in der Hashtag-Wolke versteckt; bei bezahlter Kooperation/Whitelisting zusätzlich das Paid-Partnership-Label. Details → `admkrs-cs-ugc-creator-ops`.
- **Age-Gating:** manche Kategorien (Supplements/Alkohol) brauchen in DE strengere Gates als Metas 18+-Default - manuell setzen.

## 9 - Kategorien mit Vorab-Genehmigung (bei neuem Kunden ZUERST klären)
Genehmigung vor dem ersten Launch über Meta Business Suite → „Authorizations and Verifications" beantragen; Vorlauf einplanen (Nachweise, Prüfung durch Meta). Ohne Genehmigung wird nicht ausgeliefert - das fällt sonst erst beim abgelehnten Ad-Account auf.

| Kategorie | Meta verlangt | DACH-Besonderheit |
|---|---|---|
| Online-Glücksspiel / Real-Money-Gaming | schriftliche Genehmigung + Lizenznachweis; 18+ | DE: GGL-Lizenz (GlüStV 2021) |
| Online-Dating | schriftliche Genehmigung; 18+ | - |
| Krypto (Exchange/Trading) | Lizenz-/Registrierungsnachweis + schriftliche Genehmigung; Education/News ausgenommen | DE: BaFin-/MiCAR-Zulassung |
| Online-Apotheke / Telehealth (Rx) | LegitScript-Zertifizierung + Meta-Autorisierung | DE: Publikumswerbung für Rx-Arzneimittel verboten (§ 10 HWG) |
| CBD / Hemp | LegitScript + schriftliche Genehmigung; nur wenige Länder | für DACH aktuell kein zulässiger Meta-Weg → Einzelfall/Anwalt |
| Alkohol | keine Genehmigung, aber lokale Gesetze + min. 18+; in manchen Ländern ganz verboten | DE/AT/CH: 18+ konservativ briefen |
| Finanzprodukte (Kredit/Investment) | marktabhängige Verifizierung/Autorisierung | DE: BaFin (s. Sektion 8) |

## Pre-Flight-Check (vor jedem Launch)
Personal-Attributes (Zuschreibung direkt/indirekt/Audience-Name) · Before/After-impliziert? · Krankheits-/Zahlen-Health-Claim? · Supplement-Disclaimer gesetzt (ADMKRS-Empfehlung)? · Testimonial typisch + Disclosure? · KI-Disclosure nötig? · Fake-Urgency? · Streichpreis = 30-Tage-Bestpreis? · Ad-Claim = LP? · SAC-Trigger (auch implizit)? · Kategorie mit Vorab-Genehmigung? · grafisch? · EU/DE-Claim zugelassen? · Age-Gate? Vorlage: `assets/templates/compliance-checklist.md`.

## Wenn doch abgelehnt
Abgelehnte Ad **nicht blind duplizieren** - wiederholte Verstöße kumulieren auf Account-Ebene und eskalieren Richtung Werbebeschränkung. Bei klarem Fehl-Reject: Review über Account-Status / Business-Support-Home anfordern statt neu einreichen. Bei echtem Grauzonen-Treffer: Copy/Creative fixen und als neue Ad einreichen, nicht die abgelehnte recyceln. Account-Status regelmäßig prüfen, nicht erst wenn die Auslieferung stoppt.

## Prinzipien
Im Zweifel nicht behaupten · gesperrte/freigegebene Fakten 1:1, nichts erfinden · keine Rechtsberatung (Health/Finance/EU → Kunde/Anwalt) · proaktiv prüfen, nicht auf Ablehnung warten.

## Related skills (Bundle)
Läuft als **rechtliches Gate NACH** `admkrs-cs-creative-verifier` (QA-Gate: Briefing-Treue/Handwerk/Kunde - kommt zuerst; reicht offensichtliche Health-Claim-/Claim-Mismatch-Treffer hierher weiter). Prüft Output von `admkrs-cs-creative-briefing`, `admkrs-cs-ugc-briefing` (Hooks/Scripts/Kennzeichnung), `admkrs-cs-ugc-creator-ops` (Disclosure), `admkrs-cs-offer-promo-strategy` (Preis-/Rabatt-Auslobung), `admkrs-cs-landing-page-cro` (Ad↔LP-Match). Google-Policies separat (→ `admkrs-cs-google-cross-channel`).

## Quellen (Primärquellen, Abruf 13.07.2026)
- Ad-Standards-Index: https://transparency.meta.com/policies/ad-standards/
- Personal Attributes: https://transparency.meta.com/policies/ad-standards/objectionable-content/privacy-violations-personal-attributes/ (Change-Log dort: Jun 2024)
- Health & Wellness: https://transparency.meta.com/policies/ad-standards/restricted-goods-services/health-wellness/ (Change-Log dort: Dez 2024)
- Restricted Categories (transparency.meta.com, Pfad `/policies/ad-standards/restricted-goods-services/` plus): `gambling-games/` · `dating-ads/` · `cryptocurrency-products-and-services/` · `drugs-pharmaceuticals/` · `alcohol/`
- § 11 PAngV: https://www.gesetze-im-internet.de/pangv_2022/__11.html · UWG-Anhang Nr. 7: https://www.gesetze-im-internet.de/uwg_2004/anhang.html
- DSA: VO (EU) 2022/2065, Art. 26 Abs. 3 + Art. 28 Abs. 2 · EU Health-Claims-VO (EG) 1924/2006 · EU-Kommission zum DMA
⚠️ Was nicht mit Primärquelle belegt ist, ist im Text ausdrücklich als konservative ADMKRS-Empfehlung gekennzeichnet. Statistiken ohne belastbare Quelle wurden entfernt. Policies ändern sich: vor High-Stakes-Entscheidungen Primärquelle neu prüfen.

---
<sub>**ADMKRS Creative Suite** · © ADMKRS GmbH, München · v1.13.0 · interner Gebrauch · erstellt von ADMKRS. Quellen am jeweiligen Skill-Ende; Specs/Policies an Primärquellen prüfen.</sub>
