---
name: admkrs-cs-creative-strategy-os
description: >
  Das Operating System für Creative Strategy auf höchstem Niveau — wie man eine
  NEUE Brand (als Agentur oder in-house) von Tag 1 bis zum skalierten, lernenden
  Creative-Test-Motor führt. Lehrt das Vorgehen Schritt für Schritt: Onboarding,
  Audit, Research/Insight, Creative-Diversity bestimmen, Test-Architektur, Launch,
  Performance-Diagnose, Iteration, Scaling, Cadence & Reporting — im Andromeda-Zeitalter.
  Use this skill when the user wants to know HOW to do creative strategy / creative
  testing as a process: onboarding a new brand/client, "wie teste ich richtig",
  "wie bestimme ich Creative Diversity", "wie skaliere ich Creatives", building a
  creative testing plan, setting up a creative strategy function, "creative strategist"
  workflow, "wie geht man als Creative Strategist vor", scaling Meta/paid-social creative.
  AI-supported and pairs with the `admkrs-cs-creative-briefing` skill (which writes the
  actual briefs). This skill is the PROCESS; that one is the OUTPUT.
---

# Creative Strategy OS

Dies ist das **Vorgehen**, nicht das Output-Tool. Es bringt bei, wie man als Creative Strategist eine neue Brand übernimmt und daraus einen **lernenden Creative-Motor** macht — verständlich, in Phasen, mit klaren Entscheidungen. Wo es Sinn ergibt, ist es AI-supported (welche Skills/Tools wann), aber **der Mensch versteht und steuert jeden Schritt**.

> Companion: `admkrs-cs-creative-briefing` schreibt die eigentlichen Briefings (Hooks, Konzepte, Storyboards, docx). Dieser Skill sagt dir, *wann* und *warum* du briefst, *was* du testest und *wie* du liest. Beide zusammen = volle Creative-Strategy-Funktion.

---

## Das mentale Modell (warum das alles)

Im Andromeda-Zeitalter findet Meta die Zielgruppe über das Creative — **das Creative IST das Targeting**. Daraus folgt alles:
1. **Gewinner sind selten.** ~5 % der Creatives sind echte Winner (Motion 2026, gemessen), ~50 % bekommen fast kein Budget — das ist normal. Du brauchst **Volumen an *echt verschiedenen* Konzepten**, nicht Klone.
2. **Deine Aufgabe ist ein Kreislauf, kein Projekt:** Research → Diversity → Test → Diagnose → Iterate → Scale → (zurück zu Research). Jedes Ergebnis ist Input für die nächste Runde. Das nennen wir das **Flywheel**.
3. **Klarheit vor Kunst, Daten leiten die Richtung, nichts erfinden.** Echte Kundensprache schlägt Bauchgefühl; Account-Daten schlagen Branchen-Benchmarks; gesperrte Fakten bleiben 1:1.

Wenn du nur eine Sache mitnimmst: **Du verkaufst nicht „mehr Creatives", du baust ein System, das systematisch herausfindet, *welche Idee* bei *welchem Menschen* zündet — und das verdoppelt, was gewinnt.**

---

## Die Phasen (das Rückgrat)

Grober Zeitrahmen für eine neue Brand: **Tag 1 → Woche 1 → Woche 2–4 → laufend.** Reihenfolge ist bewusst — nicht überspringen.

### Phase 0 — Setup & Ökonomie  ·  *Tag 1*  ·  „bevor du irgendetwas testest"
**Was zuerst:** Zugänge + Zahlen, sonst kannst du Gewinner nicht erkennen.
- **Zugänge holen:** Ad-Account, Analytics/DatAds, Pixel/CAPI-Status, Shop/GA4, Brand-Assets, **frühere Creatives + Performance-Export**.
- **Erfolg definieren (Unit Economics):** Primär-KPI (ROAS/CPA/CPL), **Marge, Ziel-CAC, AOV, Payback, Attributionsmodell**. Ohne Ökonomie ist „Winner" Meinung.
- **Constraints mappen:** gesperrte Claims/Legal, Brand-Safe-Regeln, Budget, **Produktionskapazität** (wie viele Creatives/Woche schaffen wir?).
**Worauf schauen:** Stimmen Tracking & Attribution? Was ist die echte Ziel-CAC bei der Marge?
**AI-Support:** noch keiner — das ist Zugang + Alignment. → Vorlage: `assets/templates/brand-onboarding-worksheet.md`.

### Phase 1 — Audit & Diagnose  ·  *Tag 1–3*  ·  „verstehe, wo die Brand steht"
- **Account-Audit (DatAds):** Was läuft? Was hat historisch gewonnen/verloren (*Bestperformer*, *Best Hooks*, *Ads to Kill*)? Format-Mix, Diversity-/Hook-/Fatigue-Scores, Naming-Hygiene.
- **Creative-Audit:** Top- und Flop-Creatives zerlegen (Format/Hook/Angle) — Competitor-Teardown via Meta Ad Library.
- **Bottleneck-Diagnose:** Wo klemmt es? **Scroll-Stop** (Hook) · **Verlangen** (Angle) · **Vertrauen** (Proof) · **Conversion** (Offer/LP)? Der Bottleneck priorisiert die ersten Tests.
**Worauf schauen:** Welcher *Angle/Format* gewinnt in dieser Kategorie schon? Wo ist die Lücke?
**AI-Support:** DatAds; `admkrs-cs-creative-briefing/references/performance-playbook.md`. Details: `references/onboarding-and-audit.md`.

### Phase 2 — Research → Insight → Angle-Bank  ·  *Tag 2–5*  ·  „hol die Wahrheit aus dem Kunden"
- **Voice-of-Customer-Mining:** Reviews, Reddit, Ad-Kommentare, CS-Transkripte, Umfragen → **wiederkehrende Sprache, Pains, Desires, Objections, Transformations, swipeable Phrases**.
- **Angle-Bank bauen:** Cluster in **psychografische** Angles (nicht Demografie). Methode **P.D.A. = Persona × Desire × Angle**.
- **Message-Market-Fit:** ownable Twist + Botschaft je Awareness-Stage (Schwartz).
**Worauf schauen:** Welche Formulierungen wiederholen sich? (Wiederholung = validiertes Verkaufsargument.) Was ist der eine Twist, den nur diese Brand besitzt?
**AI-Support:** AI zum Scrapen/Clustern der VoC; `admkrs-cs-creative-briefing` references `creative-strategy.md` (Angle-Library) + `field-notes.md` (P.D.A.). Details: `references/research-diversity-testdesign.md`.

### Phase 3 — Creative-Diversity bestimmen  ·  *Woche 1*  ·  „so entsteht echte Vielfalt"
- **Concept-Matrix:** **Persona × Angle × Format** (+ Awareness). Jede besetzte Zelle = ein Konzept mit *eigener* Idee (eigene Andromeda-Entity-ID).
- **Test-Slate Runde 1:** **6–10 *echt verschiedene*** Konzepte, jedes als **Ad Family** (ein Angle über mehrere Formate), nicht 4 Headlines auf einem Video.
- **Priorisierung:** nach Bottleneck (Phase 1) + nach dem, was in der Kategorie/Account schon gewinnt.
- **Diversity-Math:** ~5 % Trefferquote → plane Volumen; aber **Qualität vor Menge** (Klone werden gedrosselt). Diversität misst sich über **Angle/Persona/Format**, nicht Farbe.
**Worauf schauen:** Würde Meta unsere Library nach *Concept* gruppieren — wie viele *unterschiedliche* Stapel? (Meist weniger als gedacht.)
**AI-Support:** AI generiert die Matrix + Varianten-Optionen; `admkrs-cs-creative-briefing` schreibt die Briefs. → Vorlage: `assets/templates/concept-matrix.md`.

### Phase 4 — Test-Architektur  ·  *Woche 1*  ·  „so testest du sauber"
- **Struktur:** dedizierte **Testing-Kampagne** (ABO = gleiches Budget = sauberer Read) + **Scaling-Kampagne** (CBO/ASC+). **new-vs-new** testen (nie gegen gealterte Gewinner).
- **Budget & Geduld:** **20–40 %** aufs Testing; pro Konzept **≥ ~1.000 Impressionen / 5–7 Tage**, bevor du urteilst (Andromedas schnelles Signal verleitet zu Frühurteilen).
- **Entscheidungsregeln *vorab* festlegen:** Kill bei **2–3× Ziel-CPA**; Winner = schlägt/matched den aktuellen Besten; **„Signifikanz" = pragmatisch ~20–30 Conversions** (klar als *operativ*, nicht statistisch sauber kommunizieren).
- **Eine Variable pro Iteration.**
**Worauf schauen:** Ist der Test *fair* (gleiche Startbedingungen)? Sind die Kill/Scale-Regeln *vor* dem Launch definiert?
**AI-Support:** keiner — das ist Media-Buyer-Disziplin. Details + Math: `references/research-diversity-testdesign.md`.

### Phase 5 — Produzieren & Launchen  ·  *Woche 1–2*
- **Briefs** mit `admkrs-cs-creative-briefing` (eine Briefing-Datei = die Konzepte der Runde). **Alles benennen:** `Format_Hook_Angle_Audience`.
- **Bei ~80 % shippen**, dann iterieren. AI für *Velocity* (Static-Varianten, Mockups), aber **menschliches Urteil über die Idee**.
- **Compliance 2026:** KI-invariante Elemente markieren (Logo/Claim/Zahlen — Advantage+ kann Text ändern); extern KI-generierte Assets per **AI-Disclosure**-Toggle kennzeichnen.
**AI-Support:** `admkrs-cs-creative-briefing`; AI-Bild/Video-Gen (SLCT/Pass³ aus `field-notes.md`).

### Phase 6 — Lesen & Diagnostizieren  ·  *laufend, wöchentlich*  ·  „worauf du schaust"
- **Das Dashboard:** Primär (Spend, ROAS/CPA, CVR) sagt *ob*; **Storytelling-KPIs** sagen *warum*: **Thumbstop/Hook · Hold/Retention · CTR · Completion**. Immer gegen die **eigenen** Top-Performer lesen, nicht Branchen-Schnitt.
- **Diagnose-Entscheidungsbaum:** niedriger Thumbstop → Hook/Frame fixen · hoher Thumbstop + niedrige CTR → Body/Offer · hohe CTR + niedrige CVR → **Landingpage** · usw.
- **Breakdown-Effect-Guardrail:** Budget-Allokation **nie nach Ø-CPA** in Breakdown-Reports bewerten (Meta optimiert *marginal*).
- **Nicht überreagieren** auf frühe Varianz; respektiere das Fenster.
**AI-Support:** DatAds; Entscheidungsbaum in `references/diagnose-iterate-scale.md`.

### Phase 7 — Iterieren  ·  *laufend*
- **Winner →** iterieren (**genau EINE** Sache ändern: Hook, Talent, Proof-Layer, LP, Format) → zu Ad Families ausbauen.
- **Verlierer →** killen. **„Nichts sticht heraus" →** diagnostizieren, was du gelernt hast, und neu anwinkeln.
- **Learned-Concepts-Log** pflegen: *welcher* Angle/Hook/Format gewinnt für *diese* Brand. (Das ist das wertvollste Asset, das entsteht.)
**AI-Support:** `admkrs-cs-creative-briefing` Iterationen; DatAds.

### Phase 8 — Skalieren  ·  *laufend*
- **Gewinner graduieren:** erst im Testing **+50–100 %** (übersteht es Budget?), dann ~2 Wochen später in die Scaling-Kampagne; **alte Gewinner nicht pausieren**.
- **Creative-Demand-Score** entscheidet, *wie viel* neues Creative der Account braucht (Zero-Spend-Rate, Concentration, ROAS-/Spend-Degradation, Evergreen-Share).
**AI-Support:** DatAds Creative-Demand-Score; Details: `references/diagnose-iterate-scale.md`.

### Phase 9 — Cadence, Reporting & Flywheel  ·  *wöchentlich/monatlich*
- **Wöchentliches Ritual:** Review → Entscheidungen (kill/iterate/scale) → nächstes Briefing. **Refresh nach Fatigue-Signal** (Frequenz **2,5–3,0×** + **20 % CTR-Drop**), nicht nach Kalender.
- **Reporting = Learnings, nicht nur Metriken:** *welche* Angles/Hooks/Formate gewinnen → zurück in die Research.
- **Flywheel schließen:** jedes Ergebnis startet die nächste Runde.
**AI-Support:** AI entwirft den Wochen-Report aus DatAds. → Vorlagen: `assets/templates/weekly-creative-review.md`, `test-plan.md`.

---

## Maturity-Modell (wo steht die Brand — was tust du?)
- **Crawl (Woche 1–4):** Tracking sauber, Angle-Bank steht, erster 6–10-Konzept-Test live, Naming diszipliniert. Ziel: erste echte Winner finden.
- **Walk (Monat 2–3):** wöchentliche Test-Cadence läuft, Learned-Concepts-Log wächst, 2–3 Ad Families skalieren, Diagnose-Routine sitzt.
- **Run (ab Monat 3):** Flywheel dreht, Produktion auf 5 %-Trefferquote ausgelegt, systematische Iteration der Gewinner, Reporting treibt Research. Diversity & Demand-Score steuern das Volumen.

## Was ein Creative Strategist *wirklich* tut (die Rolle)
Kein „Ideen-Lieferant", sondern **Betreiber eines Lern-Systems**: VoC-Research → Angle-Bank → Diversity-Plan → Test-Design → Diagnose → Iteration/Scaling → Reporting. Eigene KPIs: **Hit-Rate, Winner-Volumen, Creative-Demand-Score, Zeit-bis-Winner, Spend hinter Gewinner-Konzepten.** Wöchentliche Rituale, ein lebendes Learned-Concepts-Log, Disziplin bei kill/iterate/scale. Details, Maturity, häufige Fehler & AI-Stack: `references/strategist-playbook.md`.

## Prinzipien (nicht verhandelbar)
- **Echte Diversität** (Angle/Persona/Format), keine Klone — sonst drosselt Andromeda.
- **Daten leiten, Handwerk schärft.** Daten sagen *welcher Angle*; Hooks/Frameworks machen ihn scharf.
- **Klarheit vor Kunst**, nichts erfinden (Zahlen/Claims/Testimonials/Offers 1:1, Neues als [Ergänzung]).
- **Sauberes Naming & ein Learned-Log** — ohne Auswertbarkeit kein Lernen.
- **Nie senden/posten/skalieren ohne Freigabe**, nie löschen ohne Freigabe.

## Reference-Dateien
- `references/onboarding-and-audit.md` — Phase 0–1: Zugangs-/Ökonomie-Checkliste, Account- & Creative-Audit, Competitor-Teardown, Bottleneck-Diagnose.
- `references/research-diversity-testdesign.md` — Phase 2–4: VoC-Pipeline, Angle-Bank/P.D.A., Concept-Matrix & Ad Families, Test-Architektur + Math + Entscheidungsregeln.
- `references/diagnose-iterate-scale.md` — Phase 6–8: Metrik-Diagnose-Baum, Breakdown-Effect, Iterations-Playbook, Scaling, Creative-Demand-Score, Fatigue/Refresh.
- `references/operating-methods.md` — die konkreten Stellschrauben 2026: **3-Quellen-Research**, **Creative-Volumen-nach-Umsatz**-Tabelle, **60/30/10-Mix**, ASC-Struktur, **Cost Cap @ 85 % Median-CPA**, CAPI/LTV-Loop, **Hook→Body→CTA-Modular-Testing**, 2-Stufen-Scaling, Creative-Ops-Automation. **Lesen in Phase 2–4 & 8.**
- `references/strategist-playbook.md` — die Rolle, Maturity-Modell, AI-Support-Stack, häufige Fehler, KPIs, Wochen-Rhythmus.
- `assets/templates/` — Onboarding-Worksheet, **Message-Mining (5-teilig)**, Concept-Matrix, Test-Plan, Weekly-Creative-Review (copy-paste).
- Format-Bibliothek (alle Video-/Static-Styles + Einsatzzweck + Style-Decoder): siehe `admkrs-cs-creative-briefing` → `references/creative-formats.md`.

---
<sub>**ADMKRS Creative Suite** · © ADMKRS GmbH, München · v1.1.0 · interner Gebrauch · erstellt von ADMKRS. Quellen am jeweiligen Skill-Ende; Specs/Policies an Primärquellen prüfen.</sub>
