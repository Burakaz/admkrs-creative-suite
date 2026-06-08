<div align="center">

# ADMKRS Creative Suite

**Das Creative-Strategy-Betriebssystem der ADMKRS GmbH.**
11 verzahnte Skills für Paid-Social- & Google-Creative-Strategy auf höchstem Niveau — Meta (Andromeda) & Google.

`v1.1.0` · © 2026 ADMKRS GmbH, München · interner Gebrauch

</div>

---

## Was das ist
Ein installierbares Skill-Bundle (Claude-Plugin), das den kompletten Creative-Workflow einer Performance-Agentur abbildet: von der Strategie über das Briefing, die Produktion, das Testing bis zum Reporting — alles unter einer Haube, alle Skills referenzieren sich gegenseitig.

Grundprinzipien (in allen Skills): **Klarheit vor Kunst · echte Creative-Diversity (Andromeda) · Daten leiten, Handwerk schärft · nichts erfinden (Fakten/Claims/Offers 1:1) · nie senden/posten/skalieren/löschen ohne Freigabe.** Faktenbasis Stand 2026, verifiziert; Vendor-/Marketing-Zahlen sind als solche markiert. **Es sind keine echten Kundendaten enthalten — nur die fiktive Beispielmarke „NOVA".**

## Die 11 Skills
| Skill | Wofür |
| --- | --- |
| **creative-strategy-os** | Das Vorgehen: neue Brand von Tag 1 bis zum skalierten Test-Motor (Onboarding → Audit → Research → Diversity → Test → Diagnose → Iterate → Scale → Cadence). |
| **creative-briefing** | Schreibt die Briefings (Hooks, Konzepte, Storyboards) als docx im ADMKRS-Stil. Enthält Strategy-, Hook- & Framework-Engines, die **Creative-Format-Bibliothek** (Video + Static) und Field-Notes. |
| **ugc-briefing** | Erstellt das komplette UGC-Creator-Briefing als docx (B4) — ein Dokument für Creator UND Kunden: Brand-Vorstellung, virale Hook-Tricks, Storytelling-Frameworks je Awareness, drehfertige Scripts (3 Hooks · 1 Body) + Out-of-the-box-/Scroll-Breaker-Layer. |
| **creative-teardown** | Fremde/eigene Gewinner-Ads zerlegen (6-Pass), Meta-Ad-Library lesen, Swipe-File. |
| **performance-reporting** | Reports mit Learnings statt Vanity: Metrik-Stack, Profit/MER, Attribution 2026, Report-Architektur, Campaign-Tracker. |
| **landing-page-cro** | Landingpages auf Conversion briefen/auditieren (Message-Match, Core Web Vitals, Checkout-Friction). |
| **offer-promo-strategy** | Offers margenbewusst designen (Break-even-Math, Cadence). |
| **ugc-creator-ops** | Creator sourcen/briefen, Partnership-Ads, Rechte & EU-Kennzeichnung. |
| **google-cross-channel** | Creatives für Demand Gen / PMax / YouTube mit exakten 2026-Specs. |
| **pitch-teardown** | Neukunden über audit-/teardown-geführtes Selling gewinnen. |
| **ad-compliance-check** | Creatives gegen Meta-Standards 2026 + EU/DACH prüfen, bevor sie live gehen. |

**Wie sie zusammenspielen:** `creative-strategy-os` dirigiert — Audit nutzt `creative-teardown` + `performance-reporting`; Research/Diversity speist `creative-briefing`; das Briefing zieht `offer-promo-strategy` und (für Google) `google-cross-channel`; für Creator-Content liefert `ugc-briefing` das UGC-Briefing-Dokument und `ugc-creator-ops` die Operations (Sourcing/Rechte/Partnership-Ads); vor Launch läuft `ad-compliance-check`; die Landingpage über `landing-page-cro`; nach Launch diagnostiziert `performance-reporting` → nächste Runde. `pitch-teardown` gewinnt die Brand überhaupt erst.

## Struktur
```
admkrs-creative-suite/
├── .claude-plugin/
│   ├── plugin.json          # Plugin-Manifest (Skills werden automatisch erkannt)
│   └── marketplace.json     # Marketplace-Eintrag
├── skills/                  # die 11 Skills (je SKILL.md + references/ + assets/)
├── README.md · LICENSE · CHANGELOG.md · .gitignore
```

## Installation

### A) Als Plugin fürs ganze Team (empfohlen) — via GitHub-Marketplace
1. Dieses Verzeichnis in ein **privates** GitHub-Repo pushen (siehe unten).
2. Im Team (Claude Code / kompatibler Client):
   ```
   /plugin marketplace add Burakaz/admkrs-creative-suite
   /plugin install admkrs-creative-suite
   ```
   Alle 11 Skills werden automatisch erkannt. Updates: `git push` → Team aktualisiert das Marketplace.

### B) Einzeln in Cowork
Jeder Ordner unter `skills/<name>/` ist ein eigenständiger Skill. Die mitgelieferten `.skill`-Dateien per **„Save skill"** installieren — einzeln, je nach Bedarf.

### Repo auf GitHub bereitstellen (Befehle)
```bash
cd admkrs-creative-suite
git init && git add . && git commit -m "ADMKRS Creative Suite v1.1.0"
git branch -M main
git remote add origin git@github.com:Burakaz/admkrs-creative-suite.git   # privates Repo zuerst anlegen
git push -u origin main
```
> Repo **privat** halten, solange interne Methoden/IP enthalten sind. Die Skills `creative-briefing` und `ugc-briefing` nutzen für die docx-Generierung `docx` (Node) — einmalig je `cd skills/<skill>/assets && npm install`.

### Team-Website
Eine fertige Info-Website fürs Team liegt unter [`docs/index.html`](docs/index.html) — einfach lokal öffnen, oder via **GitHub Pages** veröffentlichen: Repo → *Settings → Pages → Source: `main` / `/docs`*. Sie erklärt die Suite, die 11 Skills und die Installation.

## Lizenz & Urheberschaft
Proprietär — © 2026 **ADMKRS GmbH**, München. Alle Rechte vorbehalten. Erstellt von und für ADMKRS. Keine öffentliche Weitergabe ohne schriftliche Genehmigung. Details: [LICENSE](LICENSE).

<div align="center"><sub>ADMKRS GmbH · Performance Marketing & High-Quality Creative · München</sub></div>
