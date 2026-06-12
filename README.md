<div align="center">

# ADMKRS Creative Suite

**Das Creative-Strategy-Betriebssystem der ADMKRS GmbH.**
14 verzahnte Skills für Paid-Social- & Google-Creative-Strategy auf höchstem Niveau — Meta (Andromeda) & Google.

`v1.8.0` · © 2026 ADMKRS GmbH, München · interner Gebrauch

</div>

---

## Was das ist
Ein installierbares Skill-Bundle (Claude-Plugin), das den kompletten Creative-Workflow einer Performance-Agentur abbildet: von der Strategie über das Briefing, die Produktion, das Testing bis zum Reporting — alles unter einer Haube, alle Skills referenzieren sich gegenseitig.

Grundprinzipien (in allen Skills): **Klarheit vor Kunst · echte Creative-Diversity (Andromeda) · Daten leiten, Handwerk schärft · nichts erfinden (Fakten/Claims/Offers 1:1) · nie senden/posten/skalieren/löschen ohne Freigabe.** Faktenbasis Stand 2026, verifiziert; Vendor-/Marketing-Zahlen sind als solche markiert. **Es sind keine echten Kundendaten enthalten — nur die fiktive Beispielmarke „NOVA".**

## Die 14 Skills
| Skill | Wofür |
| --- | --- |
| **admkrs-cs-creative-strategy-os** | Das Vorgehen: neue Brand von Tag 1 bis zum skalierten Test-Motor (Onboarding → Audit → Research → Diversity → Test → Diagnose → Iterate → Scale → Cadence). |
| **admkrs-cs-creative-briefing** | **Engine + Generalist:** schreibt Briefings (Hooks, Konzepte, Storyboards) als docx im ADMKRS-Stil. Enthält Strategy-, Hook- & Framework-Engines, die **Creative-Format-Bibliothek**, Voss-Haltung & VO-First — und versorgt die Format-Türen unten. |
| **admkrs-cs-static-briefing** | Format-Tür: Static- & Carousel-Ads (nutzt die creative-briefing-Engine, auf Static gescoped). |
| **admkrs-cs-motion-ad-briefing** | Format-Tür: Motion Ads — **VO-First** (VO-Script als Rückgrat, Storyboard mappt auf VO-Beats). |
| **admkrs-cs-video-ad-briefing** | Format-Tür: gedrehte Video-Ads (Talking-Head, Studio, VSL, Demo). Reines UGC → `ugc-briefing`. |
| **admkrs-cs-ugc-briefing** | Erstellt das komplette UGC-Creator-Briefing als docx (B4) — ein Dokument für Creator UND Kunden: Brand-Vorstellung, virale Hook-Tricks, Storytelling-Frameworks je Awareness, drehfertige Scripts (3 Hooks · 1 Body) + Out-of-the-box-/Scroll-Breaker-Layer. |
| **admkrs-cs-creative-teardown** | Fremde/eigene Gewinner-Ads zerlegen (6-Pass), Meta-Ad-Library lesen, Swipe-File. |
| **admkrs-cs-performance-reporting** | Reports mit Learnings statt Vanity: Metrik-Stack, Profit/MER, Attribution 2026, Report-Architektur, Campaign-Tracker. |
| **admkrs-cs-landing-page-cro** | Landingpages auf Conversion briefen/auditieren (Message-Match, Core Web Vitals, Checkout-Friction). |
| **admkrs-cs-offer-promo-strategy** | Offers margenbewusst designen (Break-even-Math, Cadence). |
| **admkrs-cs-ugc-creator-ops** | Creator sourcen/briefen, Partnership-Ads, Rechte & EU-Kennzeichnung. |
| **admkrs-cs-google-cross-channel** | Creatives für Demand Gen / PMax / YouTube mit exakten 2026-Specs. |
| **admkrs-cs-pitch-teardown** | Neukunden über audit-/teardown-geführtes Selling gewinnen. |
| **admkrs-cs-ad-compliance-check** | Creatives gegen Meta-Standards 2026 + EU/DACH prüfen, bevor sie live gehen. |

**Wie sie zusammenspielen:** `admkrs-cs-creative-strategy-os` dirigiert — Audit nutzt `admkrs-cs-creative-teardown` + `admkrs-cs-performance-reporting`; Research/Diversity speist `admkrs-cs-creative-briefing`; das Briefing zieht `admkrs-cs-offer-promo-strategy` und (für Google) `admkrs-cs-google-cross-channel`; für Creator-Content liefert `admkrs-cs-ugc-briefing` das UGC-Briefing-Dokument und `admkrs-cs-ugc-creator-ops` die Operations (Sourcing/Rechte/Partnership-Ads); vor Launch läuft `admkrs-cs-ad-compliance-check`; die Landingpage über `admkrs-cs-landing-page-cro`; nach Launch diagnostiziert `admkrs-cs-performance-reporting` → nächste Runde. `admkrs-cs-pitch-teardown` gewinnt die Brand überhaupt erst. Die **Format-Türen** (`static-`/`motion-ad-`/`video-ad-briefing`) sind gescopte Einstiegspunkte auf dieselbe `creative-briefing`-Engine — ein Format pro Tür, keine Duplikate.

## Struktur
```
admkrs-creative-suite/
├── .claude-plugin/
│   ├── plugin.json          # Plugin-Manifest (Skills werden automatisch erkannt)
│   └── marketplace.json     # Marketplace-Eintrag
├── skills/                  # die 14 Skills (je SKILL.md + references/ + assets/)
├── README.md · LICENSE · CHANGELOG.md · .gitignore
```

## Installation

### A) Als Plugin fürs ganze Team (empfohlen) — via GitHub-Marketplace
1. Dieses Verzeichnis liegt als GitHub-Repo bereit (öffentlich, teilbar).
2. Im Team (Claude Code / kompatibler Client):
   ```
   /plugin marketplace add Burakaz/admkrs-creative-suite
   /plugin install admkrs-creative-suite
   ```
   Alle 14 Skills werden automatisch erkannt. Updates: `git push` → Team aktualisiert das Marketplace.

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
> Das Repo ist **öffentlich** (per Link teilbar; LICENSE bleibt proprietär, © ADMKRS, `noindex`). Die Skills `admkrs-cs-creative-briefing` und `admkrs-cs-ugc-briefing` nutzen für die docx-Generierung `docx` (Node) — einmalig je `cd skills/<skill>/assets && npm install`.

### Team-Website
Eine fertige Info-Website fürs Team liegt unter [`docs/index.html`](docs/index.html) — einfach lokal öffnen, oder via **GitHub Pages** veröffentlichen: Repo → *Settings → Pages → Source: `main` / `/docs`*. Sie erklärt die Suite, die 14 Skills und die Installation.

## Lizenz & Urheberschaft
Proprietär — © 2026 **ADMKRS GmbH**, München. Alle Rechte vorbehalten. Erstellt von und für ADMKRS. Keine öffentliche Weitergabe ohne schriftliche Genehmigung. Details: [LICENSE](LICENSE).

<div align="center"><sub>ADMKRS GmbH · Performance Marketing & High-Quality Creative · München</sub></div>
