# Brand-Foundation & Dual-Purpose-Layer

Das UGC-Briefing hat **zwei Leser**: den **Creator** (braucht eine perfekte Datengrundlage, um drehfertig zu liefern) und den **Kunden** (will die Strategie sehen, bevor gedreht wird). Dieselbe Datei bedient beide — über klar getrennte Layer. Das ist der Kern dieses Skills.

---

## 1 — Was der Creator braucht vs. was der Kunde sieht

| Element | Creator | Kunde |
| --- | --- | --- |
| Brand auf einen Blick | ✅ | ✅ |
| Produkt-Facts / USPs | ✅ | ✅ |
| Zielperson | ✅ (handlungsleitend) | ✅ (als Begründung) |
| **Strategische Grundlage** (Angle-/Hook-Logik, Awareness, „warum UGC") | — | ✅ |
| **KPI-Hypothesen / Expected Reads** | — | ✅ |
| Hook-Varianten | ✅ (nur die Hooks) | ✅ (+ Begründung) |
| Script (Beats) | ✅ | ✅ |
| Claim-Guardrails | ✅ | ✅ |
| Specs / Delivery / Naming | ✅ | optional |

**Praxis:** *ein* Dokument. Der Client-Layer steht als Kapitel **„Strategische Grundlage"** oben (Kunde liest es, Creator überspringt es). Alternativ zwei Exporte aus derselben JSON (eine mit, eine ohne Strategie-Kapitel). Default: **ein Dokument mit beidem** — es macht die Arbeit teurer-aussehend und legitimiert die Creative-Entscheidungen.

---

## 2 — „Brand auf einen Blick" (Snapshot)

Eine halbe Seite, die der Creator in 30 Sekunden erfasst und der Kunde als korrekt abnickt. Als `keyvalue`-Tabelle:

| Feld | Inhalt (Beispiel NOVA) |
| --- | --- |
| Marke | NOVA — Protein-Food, die schmeckt wie das Original |
| Kategorie | Functional Food / Protein |
| Produkt (dieses Briefing) | NOVA Protein Coffee |
| Was es ist | Iced-Coffee-Mix mit 19 g Protein, 95 % weniger Zucker |
| Ton | ehrlich, alltagsnah, erwachsen — kein Fitness-Bro |
| Was die Brand *nicht* ist | kein „Diät"-Produkt, kein medizinisches Versprechen, kein Hype |
| Offer / Code | 10 % auf die 1. Bestellung · Code TRYNOVA |

Dazu **ein** Positionierungssatz als `lede`: *„NOVA macht aus dem Kaffee, den du eh trinkst, deine einfachste Protein-Quelle des Tages."*

---

## 3 — Produkt-Facts & USPs (die „sagbaren" Fakten)

Nicht die Broschüre — die **3–5 Dinge, die ein Creator glaubwürdig in 30 s sagen kann**. Als `headerrow`-Tabelle [Fact | Warum es zählt / wie im Video nutzbar]. Beispiele:

- „19 g Protein pro Portion" → konkrete Zahl on-screen, schlägt „viel Protein".
- „95 % weniger Zucker als ein Café-Iced-Latte" → der Trade, den die Zielperson fühlt.
- „Schmeckt wie ein Iced Latte, nicht wie Kreide" → entkräftet die #1-Skepsis bei Protein.
- „In 30 Sekunden gemixt" → einfaches Ritual, zeigbar.
- „10 % auf die erste Bestellung, Code TRYNOVA" → CTA.

Alle Zahlen/Claims kommen aus den **gesperrten Fakten** der Brand. Nichts erfinden; neue Vorschläge als **[Ergänzung]** markieren und zur Freigabe stellen.

---

## 4 — Zielperson (konkret, nicht demografisch)

Schwach: „Frauen 25–45, gesundheitsbewusst." Stark — eine benannte Person mit Alltag, Trigger-Moment, Vorerfahrung, Kaufverhalten:

> **Sarah, 34, Projektleiterin in München.** Trinkt 2–3 Kaffee am Tag, fällt um 15 Uhr in ein Loch, isst „eigentlich gesund", erreicht ihr Protein-Ziel trotzdem nie. Hat Shakes probiert — „schmecken nach Kreide". Sucht keine Diät, sondern etwas, das sich in ihren Tag einfügt. Kauft nach Bewertungen und Zutaten.

Als `keyvalue`: Persona · Awareness-Stufe · Trigger-Moment · Vorerfahrung · Einwand · Wo sie kauft. Der Creator soll **zu Sarah** sprechen, nicht „zu Menschen, die X".

---

## 5 — Strategische Grundlage (Client-Layer)

Der Teil, der das Briefing zum Kunden-Deliverable macht. Vier kurze Bausteine:

**a) Strategie-Absatz** (1 kurzer Paragraph): Wer ist die Zielperson, welche Awareness-Stufe, welcher Funnel, welche Angle-Logik, was die Hypothese ist.
> „Cold Traffic, Problem-Aware. Wir öffnen mit dem 15-Uhr-Crash — ein Moment, den Sarah jeden Tag fühlt — und positionieren NOVA als die einfachste Lösung im Kaffee, den sie eh trinkt. Drei Hook-Varianten testen drei Einstiege: Pain, Social-Proof, Result-First. Body identisch. Hypothese: Social-Proof-Hook gewinnt bei Warm-Lookalikes, Result-First bei kaltem Prospecting."

**b) Konzept-Übersicht** als `headerrow`-Tabelle [Konzept | Angle | Framework | Awareness | Hypothese] — der Kunde sieht das Warum jeder Idee.

**c) Angle-Begründung je Hook** (1 Satz): warum dieser Einstieg gewählt wurde (z. B. „basiert auf dem häufigsten Pain in Wettbewerber-Reviews").

**d) Expected Reads / KPI-Hypothesen:** was nach 3–5 Tagen gelesen wird — Hook-Rate (welcher Einstieg stoppt), dann Hold-Rate (Qualität), CVR/CPA erst nach signifikantem Spend; kein Creative-Urteil vor ausreichend Impressionen pro Variante (→ `admkrs-cs-performance-reporting`).

**„Warum UGC für dieses Produkt"** (optional, bei neuen Kunden): erklärbedürftiges Produkt + niedrige Brand-Awareness → UGC überbrückt Skepsis besser als polierte Spots. (Vendor-Benchmarks zu UGC-vs-Polished als *direktional* kennzeichnen, nicht als Garantie.)

---

## 6 — „Wie wir filmen" (Creator-Standards, einmal für alle Clips)

Ein Block, der für alle Konzepte gilt — `keyvalue` für die Specs + zwei Callouts:

- **Specs:** Ratio (9:16, optional 4:5), Länge (25–35 s + 15-s-Cut), **3 Hook-Varianten / gleicher Body**, Rohmaterial separat, Captions ohne Einbrennen, Edit-Level minimal, Licht/Ton/Setting, Dateiname-Konvention.
- **`anchor`-Callout — Performance-Regeln:** erste Zeile Energie · in die Linse · 10 % langsamer sprechen · keine Sales-Energie · Produkt in der Hand · je Hook 3 Takes.
- **`locked`-Callout — Kennzeichnung & Claims:** „Werbung" sichtbar im gesamten werblichen Teil; keine englischen Labels; Disclaimer 1:1; verbotene Formulierungen. Detail: `admkrs-cs-ad-compliance-check`.

---

## 7 — Locked-Facts-Disziplin

Wie im `admkrs-cs-creative-briefing`: **Gesperrt 1:1** hält fest, was unverändert bleibt (Zahlen, Claims, Disclaimer, Code, Review-Wortlaut). **[Ergänzung]** markiert jeden neuen Fakt/Vorschlag, der noch Freigabe braucht. Nie senden/posten/veröffentlichen ohne explizite Freigabe — das Briefing geht **als Entwurf** an den Kunden.

---
<sub>**ADMKRS Creative Suite** · © ADMKRS GmbH, München · v1.1.0 · interner Gebrauch · erstellt von ADMKRS. Beispiel NOVA ist fiktiv; echte Brand-Fakten 1:1, nichts erfinden.</sub>
