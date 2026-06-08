# Operating-Methods — die konkreten Stellschrauben (2026)

Die quantitativen, fortgeschrittenen Methoden hinter dem OS-Runbook: *wie viel* produzieren, *wie* recherchieren, *wie* das Konto strukturieren, *wie* testen und skalieren. Verifiziert 2026; **Vendor-/Praktiker-Zahlen sind als solche markiert** und gegen die eigene Baseline zu prüfen. Nichts erfinden.

---

## 1 — Research-Tiefe (vor jedem Creative)
**3-Quellen-Methode** (mind. ~1 Woche bei einer neuen Brand, bevor die erste Kampagne läuft):
1. **Reviews & Kommentare** (eigene + Konkurrenz, inkl. 1-Sterne) — die rohe Kundensprache.
2. **Umfragen** (Post-Purchase: „Was hat dich fast vom Kauf abgehalten?").
3. **Echte Kundentelefonate / CS-Transkripte** — Tonfall, Einwände, Aha-Momente.
**Leitsatz:** *Ein Kommentar = viele stille Menschen mit demselben Einwand.* Jeder wiederkehrende Einwand wird ein Creative. Ergebnis verdichtest du im **5-teiligen Message-Mining** (Kundenverständnis → Market Sophistication → Unique Mechanism → Creative Strategy → Swipe Files) → Template `assets/templates/message-mining.md`.

## 2 — Creative-Volumen nach Umsatz (wie viel produzieren?)
Volumen richtet sich nach Spend/Umsatz und Produktionskapazität. Richtwerte (Praktiker-Konsens):

| Monatsumsatz/-spend | Net-New-Konzepte / Woche |
| --- | --- |
| 0–100k | 3–5 Batches |
| 100–250k | 5–8 Batches |
| 250k–1M | 8–15 Batches |
| 1M+ | 20+ Batches |

*1 Batch ≈ 5 Ads × 3 Hooks.* Hintergrund: ~5 % der Creatives werden echte Winner → Produktion auf diese Trefferquote auslegen, **aber Qualität vor Menge** (Klone werden gedrosselt).

## 3 — Die 60/30/10-Regel (Mix der Produktion)
- **60 % Net-New-Konzepte** (neue Angles/Personas/Formate — echte Diversität).
- **30 % Iteration** bestehender Gewinner (genau EINE Sache ändern).
- **10 % Remake/Refresh** (Evergreen neu auflegen).
*Wer nur iteriert, killt mittelfristig den ROAS — die Pipeline braucht ständig frische Konzepte.*

## 4 — Konto-Struktur 2026 (was Andromeda belohnt)
- **ASC-Monostruktur als Skaling-Engine** (~60–70 % Budget) + **eine separate ABO-Test-Kampagne** (~15–20 %, nur Net-New) + **kein** klassisches Retargeting als eigene Kampagne (ASC übernimmt es intern).
- **Existing-Customer-Budget-Cap** in ASC auf ~15–25 % — sonst verbrennt ASC Akquise-Budget an Bestandskunden.
- Mehr als 2–3 parallele ASC-Kampagnen = das Fragmentierungsproblem, das ASC lösen soll. *(Quelle: Praktiker-Konsens 2026, Agenturdaten — direktional.)*

## 5 — Bidding (Kontrolle ohne Delivery zu würgen)
- **Cost Cap:** Einstieg bei **85 % des historischen *Median*-CPA** (nicht Average — Ausreißer verzerren). Wöchentlich 5–10 % senken, bis Volumen kippt. Tagesbudget = **5–10× Cost Cap** (das Verhältnis ist der kritischste Setup-Faktor).
- **Bid Cap** nur als harter Auktions-Deckel für Preis-Disziplin in umkämpften Nischen — nicht zum Skalieren (würgt Delivery).
- **Minimum-ROAS** als Alternative, wenn Margen je SKU stark variieren.
*(ATTN Agency 2026, Agenturdaten — Vendor.)*

## 6 — CAPI & LTV-Signal-Loop (das Mess-Fundament)
- **CAPI ist Pflicht** (Offline-Conversions-API abgeschaltet): Pixel + CAPI dual = Signal-Recovery (~17–19 % mehr attribuierte Conversions, Meta-Vendor-Zahl).
- **LTV-Loop:** Purchase-Value als Custom Event übergeben — idealerweise prognostizierter **90-Tage-LTV** statt AOV. So lernt ASC, dass ein 29-€-Erstkauf eigentlich 180 € wert ist (relevant für Abo/hoher LTV). *(Technisch dokumentiert; Praxis-Ergebnis variiert je Datenlage.)*

## 7 — Modulares Testing: Hook → Body → CTA (nacheinander)
Nicht alles gleichzeitig testen (Confounding). Sequenz:
1. **Phase 1:** Body + CTA konstant, **3–5 Hook-Varianten** gegeneinander.
2. **Phase 2:** Gewinner-Hook fixieren, **Body-Varianten** (Proof/Demo/Story) testen.
3. **Phase 3:** **CTA**-Sprache/-Timing testen.
Meta-Detail: verschiedene CTA-Buttons auf **demselben** Post laufen lassen — kein Duplicate-Content, Social-Proof-Zähler bleibt gebündelt. *(Praktiker-Konsens 2026.)*

## 8 — Scaling: zwei getrennte Probleme (nicht verwechseln)
- **Stufe 1 — strategisch:** Findet das *Konzept* überhaupt Resonanz? (Kill, wenn nach definiertem Spend kein Signal.)
- **Stufe 2 — operativ:** Gewinner-Konzept in diverse **Asset-Varianten** skalieren (Hooks/Formate/Längen), erst im Testing +50–100 %, dann graduieren; alte Gewinner nicht pausieren.
*Wer die Stufen verwechselt, skaliert ungetestete Konzepte oder produziert Varianten ohne validierte Basis. (Andrew Faris / CTC-Framework.)*

## 9 — Creative-Ops & Automation (Velocity, Mensch bleibt Gate)
- **Asset-Pipeline:** automatisierter Workflow (z. B. n8n) scannt einen Drive-Ordner, legt Kampagnen/Ad-Sets/Ads **pausiert** an, schreibt Copy-Varianten, loggt in Sheets → spart 10–15 h/Woche/Buyer. **Nie autonom aktivieren — Human-Review ist Pflicht-Gate.**
- **Multivariate-Static-Tests** (z. B. Marpipe): Variablen (Hintergrund/Headline/Produktfoto/CTA) kombinatorisch zu vielen Statics. *(Vendor.)*
- **Meta-Gen-AI** (Image-Expansion/Backdrop/Video-Enhancement) für *Velocity*, nicht für Voll-Automation — vollautomatische Gen-AI-Creatives performen bisher schwächer als Human-Crafted. **KI-Disclosure beachten** (→ `creative-briefing` field-notes / `ad-compliance-check`).

## 10 — Retention-Creatives als eigener Layer
Bestandskunden-Creatives (Cross-Sell, Abo-Upgrade, Re-Engagement) laufen **nicht** in ASC (durch den Existing-Cap limitiert), sondern als separate Manual-Kampagne mit Purchaser-Custom-Audiences. Brief: **kein** Awareness-Hook — direkter Einstieg mit Product-Familiarity-Signal.

## 11 — Erfolg = Profit, nicht ROAS
Steuere auf **MER / Contribution / nCAC**, nicht auf Plattform-ROAS (überschätzt 30–60 %). Details + Formeln: `performance-reporting` SKILL.md §2. Höherer **CLV** ist ein Wettbewerbsvorteil — er erlaubt eine höhere leistbare CPA als die Konkurrenz.

---

## Quellen
Praktiker/Agentur-2026: alexneiman.com & metalla.digital (ASC-Struktur) · attnagency.com & theoptimizer.io (Cost/Bid Cap) · triplewhale.com & wetracked.io (CAPI/LTV) · n8n.io & marpipe.com (Automation/Multivariate) · ajfgrowth.com / motionapp.com (2-Stufen-Scaling, Faris) · Common-Thread / Eightx (Profit/MER). Research-Methodik & 5-Part-Mining: etablierte Creative-Strategy-Praxis (DACH/US). *Agentur-/Vendor-Zahlen direktional — eigene Baseline schlägt jeden Benchmark.*
