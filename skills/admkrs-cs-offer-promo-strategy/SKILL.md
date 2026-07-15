---
name: admkrs-cs-offer-promo-strategy
description: >
  Designt und plant Offers & Promotions für DTC / Paid Social margenbewusst. Use when
  the user wants to design an offer, plan a promo, choose between % vs € off / bundle /
  free shipping / BOGO / gift, set a free-shipping threshold, run break-even math,
  plan a promo calendar, or reduce discount fatigue. Offer-Statics sind über DTC-Accounts
  der Effizienz-Hebel. Pairs with admkrs-cs-creative-briefing (Offer-Static) und admkrs-cs-landing-page-cro.
---

# Offer & Promo Strategy

Offers sind der zuverlässigste Effizienz-Hebel auf DR-Creatives - aber jeder Rabatt frisst Marge. Dieser Skill wählt den richtigen Offer **margenbewusst** und plant die Cadence, ohne die Marke zu erodieren. Jeder Promo geht die **Break-even-Rechnung** voraus.

## Offer-Toolkit (wann was)
- **% off** - sub-€100, wo die Prozentzahl größer „liest" als der Euro-Betrag (Rule of 100). Akquise. Margen-Kosten skalieren mit AOV → nur bei 45–85 % GM (Beauty/Supplement/Apparel).
- **€ off** - über €100 („€50 off" > „20 %"). Auch Retention/Loyalty (greifbarer).
- **Free Shipping** - fixe, gedeckelte Kosten/Order → sicherster Hebel bei niedriger Marge. **Threshold bei 1,3–1,5× aktueller AOV** setzen. ⚠️ „80 % füllen den Warenkorb auf" ist *stated preference* (Shopify); reales Verhalten ~58 % (Red Stag 2026).
- **BOGO** - starker AOV-/Perceived-Value-Hebel, aber effektiv **50 % Rabatt** in der Break-even-Formel: unter 50 % GM ist jede Order margen-negativ, ein Break-even existiert nicht - egal wie viel Mehrabsatz. Selbst bei 65 % GM braucht's +333 % Mehrabsatz (daher die 65-%-Schwelle: GM muss deutlich über dem 50-%-Effektivrabatt liegen). Nie als Effizienz-Hebel rechnen, nur für Lager-Clearing langsamer SKUs oder AOV-Push mit bewusst einkalkulierten Kosten.
- **Bundles/Kits** - schützen Marge (Perceived Value statt Preis-Cut). Kuratierte Themen-Sets > generische Multipacks.
- **Gift-with-Purchase / Free-Gift-Threshold** - Wert ohne Preis-Cut, schützt Referenzpreis; „Geschenk" visuell als starker Hook im Static/Carousel; langsame Ware als Geschenk = Lager-Clearing ohne Markdown.
- **Spend-Tiered (spend-more-save-more)** - starker AOV-Hebel; treibt Korb nach oben.
- **First-Order / Subscription-First** - Erstkauf ist meist unprofitabel; Rechtfertigung = LTV (Order 2–3), als Akquisekosten behandeln, nur wenn das LTV-Modell den Payback trägt.
- **BNPL (Klarna/Afterpay)** - AOV-Uplift real, aber Vendor-Daten mit Selektionsbias → konservativ **10–20 %** ansetzen, am besten ab ~€150 AOV.

## Break-even (vor jedem Promo rechnen)
**Nötiger Mehrabsatz = 1 ÷ (1 − Rabatt ÷ GM) − 1.** Beispiele: 20 % Rabatt bei 35 % GM → +133 % Units (nach Kannibalisierung unmöglich); 20 % bei 70 % GM → +40 % (machbar). **BOGO = 50 % Rabatt in die Formel: unter 50 % GM existiert kein Break-even, bei 65 % GM sind +333 % nötig.** Zweite Pflicht-Rechnung: der **Break-even-ROAS steigt im Promo**, weil die Marge um den Rabatt schrumpft (Beispiel GM 70 %, 20 % Rabatt: 1,43 → 1,6) - tROAS/Cost-Caps fürs Promo-Fenster auf den Promo-Break-even setzen, nicht auf den normalen (Formel im Planner). Vorlage: `assets/templates/offer-planner.md`. Intake vor dem Rechnen: AOV, GM und freigegebene Offer-Konditionen sind Pflicht-Rückfragen; Planner nur vollständig ausgefüllt ausliefern, ungeklärte Zeilen weglassen und intern nachhalten.

## Psychologie (caveated)
**Anchoring** (Was-Preis neben Offer) erzeugt Referenzpreis-Effekt - Compliance-/Vertrauensrisiko bei Übertreibung. **Preisrecht DE/EU (hart, nicht optional):** Ein Streichpreis muss der niedrigste Gesamtpreis der letzten 30 Tage sein (§ 11 Abs. 1 PAngV, Umsetzung der EU-Omnibus-Richtlinie). UVP-Anker fallen nicht unter § 11, sind aber nur zulässig, wenn die UVP real und aktuell ist (sonst Irreführungsrisiko). Individuelle/personalisierte Preisermäßigungen sind von § 11 ausgenommen (§ 11 Abs. 4 Nr. 1) - ein weiteres Argument für Segment-Codes statt Public-Streichpreis. **Loss-Aversion** („verpass nicht X" > „hol dir X") - Lift direktional (Vendor-Quellen, kein Peer-Review). **Scarcity/Urgency** nur bei echtem Limit; ⚠️ der kursierende „226 % Conversion-Lift durch Scarcity" ist **unbelegt** - nicht in Kunden-Material zitieren. Nicht Scarcity + Loss-Aversion + Urgency gleichzeitig stapeln (Skepsis).

## Offers unter Andromeda (im Creative)
Offer muss in **Sekunde 1–2** lesbar sein (Andromedas Creative-/CTR-Signal). Offer-Statics + founder-led UGC mit Offer-Callout führen DR. Codes verstärken Message-Match Ad↔LP (→ `admkrs-cs-landing-page-cro`), aber breite Public-Codes haben **20–60 % Kannibalisierung** (direktional, s. Cadence) → segment-spezifische Codes (Neukunden/Email-only). Offer-Angle vs. Non-Offer-Angle als Test-Achse im Set (→ `admkrs-cs-creative-strategy-os`).

## Cadence, Kannibalisierung & Marken-Equity
~50–60 % der Promos liefern keinen positiven Return (diskontieren Käufe, die eh passiert wären) - **ohne Holdout nicht messbar** (direktionaler BCG-Prior). Holdout-Minimal-Setup: 5–10 % Audience- oder Geo-Split, gemessen über Promo-Fenster plus ~2 Wochen (Pull-Forward-Effekt). Kannibalisierung (Praktiker-Bänder, Single-Source, direktional - eigene Holdout-Messung schlägt jede Benchmark): breiter Sitewide-Code 20–60 % · Flash 30–45 % · Lifecycle/Neukunden-only 10–25 % · Exit-Intent 10–15 %. **RFM-Routing:** Champions → Exklusivität/Early-Access, **nie** Coupons; At-Risk → eskalierende Sequenz; Lost → Win-Back tief oder unterdrücken. Persistente Rabatte trainieren Warten → strukturierter Kalender (1–2 große Promos/Jahr + Lifecycle-Trigger) + klare „kein Sale"-Phasen schützt Referenzpreis. Die „kein Sale"-Phasen sind auch **rechtlich nötig**: Back-to-back-Streichpreis-Promos zerstören den zulässigen 30-Tage-Referenzpreis (§ 11 PAngV) - nach jedem Promo genug Vollpreis-Phase, damit er sich wieder aufbaut. Q4/BFCM-CPMs ~+41 % → für Retention/Loyalty nutzen, nicht Cold-Akquise.

## Promo-Kalender (ADMKRS-Standard-Gerüst)
- **Jahres-Slots:** 1–2 Tentpoles (z. B. BFCM + 1 Brand-Moment) + Lifecycle-Trigger (Welcome, Winback, At-Risk) + explizite Kein-Sale-Fenster, die den 30-Tage-Referenzpreis wieder aufbauen.
- **Tentpole-Phasing:** Teaser (2–5 Tage, ohne Preis, Hook auf den Moment) → Early Access (24–48 h für Liste/Champions, Exklusivität statt Extra-Rabatt) → Main (5–7 Tage) → Last Call (24–48 h, echtes Ende, kein stilles Verlängern).
- **Creative-Bedarf je Phase:** eigene Hooks für Teaser, Main und Last Call statt ein Static fürs ganze Fenster; Last-Call-Urgency nur mit echter Deadline.

## Non-Discount-Offers (Marge schützen)
Limited Editions/Drops · Gift-with-Purchase · Members-Only-Early-Access · Service (Free Returns, Priority Shipping) · exklusiver Content/Community.

## Prinzipien
Break-even vor jedem Offer · Marge & Referenzpreis schützen · echte Knappheit, keine Fake-Timer · Vendor-Zahlen konservativ · gesperrte/freigegebene Offer-Konditionen 1:1, nichts erfinden.

## Related skills (Bundle)
`admkrs-cs-creative-briefing` (Offer-Static/-Hook) · `admkrs-cs-landing-page-cro` (Offer-Darstellung/Code-Match) · `admkrs-cs-creative-strategy-os` (Offer als Test-Achse) · `admkrs-cs-ad-compliance-check` (Rabatt-/Preis-Auslobung).

## Quellen
§ 11 PAngV (Volltext: gesetze-im-internet.de/pangv_2022/__11.html, abgerufen 13.07.2026) · Digital Applied (Margin-Aware Playbook, Mai 2026) · Growth Suite (Rule of 100) · Red Stag (Free-Shipping 2026) · Chargeflow (BNPL) · AB Tasty (Loss-Aversion) · Eightx / StickyDigital (Retention/Spend-Trends) · Jetfuel (Andromeda/Offer). ⚠️ „226 % Scarcity-Lift" & „80 % Threshold" als Behauptungen markiert.

---
<sub>**ADMKRS Creative Suite** · © ADMKRS GmbH, München · v1.13.0 · interner Gebrauch · erstellt von ADMKRS. Quellen am jeweiligen Skill-Ende; Specs/Policies an Primärquellen prüfen.</sub>
