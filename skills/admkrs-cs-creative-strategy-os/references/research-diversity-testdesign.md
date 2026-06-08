# Phase 2–4 — Research → Diversity → Test-Design

Das Herzstück: aus echten Insights echte Vielfalt bauen und sie sauber testen. Reihenfolge zwingend — Research vor Diversity vor Test-Design.

---

## Phase 2 — Research → Insight → Angle-Bank

### 2.1 Voice-of-Customer-Mining (die Quelle der Wahrheit)
Angles werden nicht erfunden, sie werden **gefunden** — in der Sprache der Kunden.
Quellen: eigene Reviews (Shop/Trustpilot/Amazon), **Reddit** & Foren der Nische, **Ad-Kommentare** (eigene + Konkurrenz), **CS-/Sales-Transkripte & Support-Tickets**, Umfragen (Post-Purchase: „Was hat dich fast vom Kauf abgehalten?"), Konkurrenz-1-Sterne-Reviews (deren Pains = deine Angles).
Scanne auf **wiederkehrende Formulierungen** — wiederholte Sprache = validiertes Verkaufsargument. Extrahiere pro Fund: **Pain · Trigger · Objection · Transformation · swipeable Phrase** (wörtliches Zitat).
**AI-Support:** AI scrapen/clustern lassen; dann menschlich kuratieren (keine erfundenen Zitate).

### 2.2 Angle-Bank (psychografisch, nicht demografisch)
Cluster die VoC in eine wiederverwendbare **Angle-Bank**. Struktur **P.D.A. = Persona × Desire × Angle**:
- **Persona:** psychografisch (z. B. „gestresste Vielbeschäftigte, die abends nicht abschalten"), nicht „Frauen 25–45".
- **Desire:** das gewünschte Gefühl/Ergebnis (Loslassen, Sicherheit, Status, Genuss-ohne-Reue).
- **Angle:** die Verkaufstür (Pain, Mechanism, Proof, Comparison, Identity, Offer … 16er-Liste in `admkrs-cs-creative-briefing/references/field-notes.md`).
Lege zusätzlich die **Awareness-Stage** je Angle fest (Unaware → Most-Aware) — sie bestimmt, wo der Hook ansetzt.
Ergebnis: 4–8 belastbare Angles + der **ownable Twist** (meist Mechanism × Trade-off), den nur diese Brand besitzt.

---

## Phase 3 — Creative-Diversity bestimmen

### 3.1 Warum Diversität (Andromeda)
Meta vergibt pro *echtem* Konzept eine eigene Entity-ID und einen eigenen Retrieval-Versuch. **50 Varianten = 1 Eintrag; 10 echte Konzepte = 10.** Klone werden über Similarity-Detection gedrosselt. Diversität ist der #1-Performance-Hebel — aber nur *echte* (anderer Gedanke), nicht kosmetische.

### 3.2 Die Concept-Matrix (so bestimmst du Vielfalt konkret)
Spanne ein Raster auf: **Persona × Angle × Format** (Format = Static / Carousel / Motion / UGC-Video / Founder-VSL). Optional 4. Achse Awareness.
- Jede *besetzte Zelle* = ein Konzept mit eigener Idee.
- Wähle für Runde 1 **6–10 Zellen, die sich über alle drei Achsen unterscheiden** — nicht 8 Zellen, die nur das Format variieren.
- Priorisiere nach **Bottleneck** (Phase 1.3) und nach **Kategorie-Gewinnern** (Phase 1.1).
Vorlage: `assets/templates/concept-matrix.md`.

### 3.3 Ad Families statt Variationen
Ein **Konzept (Angle)** wird zur **Ad Family**, indem du denselben Winkel über mehrere Formate spielst (UGC-Testimonial + Static-Quote + Motion-Stat). Das ist sinnvolle Vielfalt. **Nicht** 4 Headlines auf demselben Video — das ist eine Iteration, kein Konzept.

### 3.4 Diversity-Math (wie viel?)
- ~5 % der Creatives werden echte Winner → plane Volumen entsprechend (mehr Konzepte = mehr Schuss aufs Tor), **aber Qualität vor Menge**.
- Pragmatischer Start: **6–10 Konzepte/Runde**, je 1–3 Format-Treatments. Tempo richtet sich nach Produktionskapazität (Phase 0.3) und Budget.
- **Diversity-Check:** „Würde Meta nach Concept gruppieren — wie viele *verschiedene* Stapel?" Wenn < Hälfte deiner Assets → zu viele Klone.

---

## Phase 4 — Test-Architektur (sauber testen)

### 4.1 Kampagnen-Struktur
- **Testing-Kampagne (ABO):** gleiches Budget je Ad-Set = sauberer, vergleichbarer Read. Ein Ad-Set je Konzept(-Family) ODER ein breites Ad-Set mit den Konzepten — je nach Spend.
- **Scaling-Kampagne (CBO / Advantage+):** dorthin graduieren Gewinner.
- **new-vs-new:** neue Creatives nie gegen gealterte Gewinner testen (History-Vorteil verzerrt).
- Struktur nach Spend: klein → ASC+/CBO; mittel → ABO (schnelleres Signal); groß → Cost-Cap, 1 ABO-Ad-Set/Konzept.

### 4.2 Budget & Geduld
- **20–40 % des Budgets** ins Testing.
- Pro Konzept **≥ ~1.000 Impressionen / 5–7 Tage**, bevor geurteilt wird. Andromedas schnelles Signal verleitet dazu, frühe Varianz für Insight zu halten — nicht tun.

### 4.3 Entscheidungsregeln *vorab* (das macht es zum System)
Definiere **vor** dem Launch (Vorlage: `assets/templates/test-plan.md`):
- **Kill:** Ad-Set bei **2–3× Ziel-CPA** ohne Signal.
- **Winner:** schlägt/matched den aktuellen Besten (BAU) bei akzeptabler CPA.
- **„Signifikanz":** pragmatisch **~20–30 Conversions** zu gutem CPA → so kommunizieren: *operative* Entscheidung, **nicht** statistisch sauber. Nie eine Signifikanz behaupten, die nicht da ist.
- **Eine Variable pro Iteration** (sonst lernst du nichts).

### 4.4 Häufige Test-Fehler (vermeiden)
Zu früh urteilen · zu viele Variablen gleichzeitig · Klone statt Konzepte · Gewinner zu früh pausieren · ein bereits gelerntes Creative in neues Ad-Set „zwingen" · Branchen-Benchmarks statt eigener Baseline · Signifikanz vortäuschen.

**Output von Phase 2–4:** Angle-Bank + Concept-Matrix + ein dokumentierter Test-Plan mit Regeln. Damit briefst du (Phase 5 via `admkrs-cs-creative-briefing`) und launchst.
