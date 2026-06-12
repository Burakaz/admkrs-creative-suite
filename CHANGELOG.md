# Changelog — ADMKRS Creative Suite

## v1.7.1 — 2026-06
Briefing-Tabelle: Nummern-Spalte und Konzept-Name getrennt, Bold-Konvention beidseitig hart, kein Ads-Manager-CTA.

- **`#`-Spalte**: nur noch die Ziffer (1, 2, 3 …), **superschmal** (~0,3 Gewicht), zentriert, nicht fett.
- **Neue Spalte 2** trägt den **Konzept-Namen** („WISMO", „Kalter Kaffee" …), nicht fett; Header heißt je Briefing-Typ **`Static`**, **`Motion`** oder **`Video`**.
- **Bold-Konvention in beide Richtungen:** fett = landet auf dem Creative, **und nur das**. #, Konzept-Name, Dateiname, Creative Format und Visual-Direction sind nie fett.
- **Final & ohne Ballast:** Build-Zellen enthalten nur On-Creative-Text + Visual-Direction. **Kein Ads-Manager-CTA** („Jetzt einkaufen"-Button aus Meta) im Briefing — CTA-Text nur als gestaltetes Element auf dem Creative selbst. Neuer **On-Creative-Test** im Quality-Check.
- Schema jetzt: `[# | Static | Dateiname | Produkt | Creative Format | Hook | Subline | USPs/Badge | Disclaimer | Visual-Direction]`. Doku, Skills und Beispiel-Briefing angepasst.

## v1.7.0 — 2026-06
Katalog in 25 Familien gegliedert + 27 Styles reintegriert (jetzt 219).

**Style-Bibliothek (`creative-formats.md`):**
- Neue **§0 „Die 25 Style-Familien"**: erste Orientierung mit Top-Picks je Familie; Familien als Diversity-Check-Raster.
- **WhatsApp-Chat-Static** und **iMessage-Chat-Static** explizit benannt (Native-Liste).

**Website (`styles.html`) — Katalog-V2:**
- Erste Ebene jetzt **25 Familien** (statt 219 flacher Karten): kompakte Familien-Karte mit Mini-Preview, Einsatz-Zeile und kuratierten **Top-Picks** (58 markiert), Substyles aufklappbar. Sidebar nach Medium gegliedert, Suche öffnet Treffer-Familien automatisch.
- **27 Styles reintegriert**, die bisher nur als Stichpunkte im Skill standen: WhatsApp/iMessage/Tweet/Reddit/Notes, Offer/Bundle/Seasonal, Before/After- und Split-Visual-Static, Infografik/Ingredient-Callout, Editorial/Advertorial, 7 Carousel-Basistypen, DPA/Advantage+ Catalog/Collection. WhatsApp mit eigenem Preview-Look (grüne Bubbles, Haken).
- Trend-Marker („steigt") aus den Namen in ein eigenes Badge-Feld bereinigt; `examples`-Feld je Style vorbereitet (für die kommende Beispiel-Bibliothek).

## v1.6.0 — 2026-06
iOS-native Ad-Styles + Preview-Feinschliff.

**Style-Bibliothek (`creative-formats.md` §6b · UI-Fakes):**
- **8 neue iOS-native Styles:** AirDrop-Share, iOS-Widget, Live-Activity / Dynamic-Island, Siri-Suggestion, Share-Sheet, Screen-Time, Wallet-Pass, System-Alert — Katalog jetzt **192 Styles**.

**Website (`styles.html`):**
- Alle 8 neuen Styles mit eigener NOVA-Preview (AirDrop-Radar mit Annehmen/Ablehnen, Homescreen-Widget, Island-Pille mit Live-Status, Siri-Karte, Share-Sheet mit Empfängern, Screen-Time-Balkenreport, Wallet-Pass, iOS-Dialog).
- Preview-Polish: 26 Hook-Duplikate bereinigt, detailliertere Produkt-Grafiken (Sorten-Label, Licht/Schatten), Reels-Rail + Sound-Bars bei Video, Phone-Statusleisten, CSS-Icons statt Emojis. **Statics stehen still**, nur bewegte Medien (Video/Motion/Carousel) animieren.
- Seiten-Zähler dynamisch aus den Katalog-Daten generiert.

## v1.5.0 — 2026-06
Designer-Standard + Ad-Style-Bibliothek (184 Styles) + neue Website-Seite.

**Designer-Briefing-Standard (Static/Motion/Video):**
- **„Auf einen Blick"-Block (Pflicht)** oben in jedem Designer-Briefing: Ziel · Zielgruppe · Formate · Deadline · Wichtige Infos.
- **Format-Regel Meta:** Standard ist **4:5 + 9:16 — kein 1:1 mehr** in Meta-Briefings. Sonderformate (andere Plattformen) immer extra mit Plattform + Format + Pixeln.
- **Bold-Konvention:** **Alles, was fett geschrieben ist, landet auf dem Creative** (Hook, Subline, USPs, Disclaimer). Konvention steht als Zeile über der Briefing-Tabelle.
- **Neue Statics-Tabellen-Spalten:** `# | Dateiname | Produkt | Creative Format | Hook | Subline | USPs/Badge (opt.) | Disclaimer (opt.) | Visual-Direction`. Optionale Spalten weglassen, wenn im Set leer. Subline = Klammer-Auflösung zum Hook.
- **Visual-Direction frei:** Inspos/Stimmung/Referenzen statt Vorgaben — keine Formatangaben, keine Farben (außer klare Kunden-Vorgabe). Designer kreativ arbeiten lassen.
- Neue Quality-Checks: Auf-einen-Blick-, Bold-, Format-, Style- und Visual-Frei-Test.

**Ad-Style-Bibliothek (`creative-formats.md` §6b):**
- **135 neue Ad-Styles** per Web-Recherche (Juni 2026, 10 parallele Sweeps, 242 Quellen-Domains, u. a. Motion, Foreplay, Superads, MagicBrief, TikTok Creative Center, Meta Business Help) — dedupliziert gegen den Bestand, kuratiert, mit Erkennungsmerkmal / Wofür gut / Aufbau, Trend-Markern (↑/↓) und inkl. der Kern-Styles USP Ad, Product Features, 3/5 Reasons Why, Problem/Solution, Organic Screen(shot).
- 10 neue Kategorien: Static DR & Produkt-Layout · Static Brand/Editorial · Static UI-Fakes & Screenshot-Proof · Video UGC/Creator · Video Social Proof · Video DR-Story/Demo/Production · Motion & CGI · Carousel-Formate · B2B & SaaS · Interactive & Platform-Mechaniken.
- Die `Creative Format`-Spalte im Briefing nimmt ihre Style-Namen aus dieser Bibliothek (§1–6b).

**Website:**
- Neue Seite **`styles.html`** — die komplette Style-Bibliothek (184 Styles, Bestand + Recherche) mit Filter-Tabs (Static/Video/Motion/Carousel/B2B) und Live-Suche; von index.html und prozess.html verlinkt.

## v1.4.0 — 2026-06
Dokument-Disziplin: zeilenweise statt Block, schlanke Designer-Briefings.

- **Builder (`build_briefing.js`, beide Engines identisch gepatcht):** Callouts sind jetzt **mehrzeilig** (jede `\n`-Zeile = eigener Absatz) statt ein Block. Neue Callout-Variante **`todo`** (warmer Balken) für **„Vor Produktion klären (blockiert sonst alles):"**. Mehr Zeilenluft in Tabellenzellen.
- **Zeile für Zeile statt Block (Pflicht):** Aufzählungen/Anweisungen kommen je auf eine eigene `\n`-Zeile — in Zellen wie Callouts. Verankert in `document-format.md` (beide Skills), den Leitprinzipien & im Quality-Check.
- **Schlanke Designer-Dokumente (Motion/Static/Video):** keine Strategie-/Hebel-Tabelle mehr — Strategie steckt in **einem** `anchor`-Callout (1–2 Zeilen). Build-Zellen **final entschieden** (keine offenen Fragen), **ein konkreter Fakt statt Floskel** (keine Badge-Doppler), Visual-Direction als **Schritt-Liste**. UGC-Briefing bleibt dual-purpose (Strategie-Layer für den Kunden).
- **Offene Punkte gebündelt:** alle Blocker/Rückfragen in **einen `todo`-Callout** ganz oben, fehlende Werte als `[Platzhalter: …]` — nie raten, nie erfinden.
- **Beispiele neu im Standard:** `example_statics_briefing.json` (todo-Block, Kern-Anker, zeilenweise Build-Zellen), `example_motion_briefing.json` (todo-Block, VO-Direction/Music zeilenweise), `example_ugc_briefing.json` (todo-Block). Alle bauen sauber.
- **Neue Quality-Checks:** Zeilen-Test · Designer-Schlank-Test · Final-statt-offen-Test · Floskel-Doppler-Test.
- Footer-Versionen aller Briefing-Skills auf **v1.4.0** vereinheitlicht.

## v1.3.1 — 2026-06
`creative-briefing`: Klarheit hart durchgesetzt (gegen „gewollt kreative", kontext-abhängige Hooks).

- **Neue harte Tests** in `copywriting.md` §1 + Qualitäts-Check (`SKILL.md`): **Kontext-frei-Test** (jedes Substantiv konkret — kein offenes „welche Zahl/Rechnung?"), **Schachtel-Test** (ein Gedanke/Hauptsatz), **Kürzen-Pass (Pflicht)** und **Detail-Regel** (Beweise/Zahlen/Listen in Sub/USP, nicht in den Hook).
- **Neuer Abschnitt `copywriting.md` §1b „Anti-Patterns — sofort umschreiben"**: kontext-abhängiger Claim · Schachtelsatz · vage Dreierliste · gewollt kreatives Wortspiel · abstrakte Gleichsetzung — je mit Vorher/Nachher.
- **weak→strong** um Praxisfälle erweitert (u. a. „Eine Zahl im Monat…" → „Ein Fixpreis im Monat. Alles drin.").
- **hook-library.md**: Klarheits-Gate über allen Templates; kontext-freie Beispiele für Kategorien, die vorher keins hatten (Curiosity/Authority/Story/Emotional); Klarheit **über** Haltung (Voss-Kat 16).
- Leitprinzip „Klarheit vor Kunst" in `SKILL.md` verschärft (mit Beispiel). Motion-/Statics-Beispiele bauen weiter; ein vager Beispiel-Hook auf ein konkretes (verbatim) Review-Fragment korrigiert.
- **ADMKRS-Hausregel: kein langer Gedankenstrich „—" (Em-Dash)** in produzierter Copy — verankert in `copywriting.md` §8, Quality-Check (`SKILL.md`) & `ugc-briefing`. Lange „—" in den Beispiel-Briefings + Copy-Docs auf „–"/Satzzeichen umgestellt (Quell-Zitate in `field-notes.md`/`voss-principles.md` unangetastet).

## v1.3.0 — 2026-06
Format-Türen: Static / Motion / Video als eigene Skills (gleiche Engine).

- Neue **format-spezifische Einstiegs-Skills**: `admkrs-cs-static-briefing` (Statics/Carousel), `admkrs-cs-motion-ad-briefing` (Motion, **VO-First**), `admkrs-cs-video-ad-briefing` (gedrehtes Video/VSL). Sie nutzen die **gemeinsame `creative-briefing`-Engine + References 1:1** (keine Duplikate); `creative-briefing` bleibt Engine + Generalist, `ugc-briefing` deckt Creator/UGC ab. → **14 Skills**.
- Repo **öffentlich** gestellt (teilbar; LICENSE bleibt proprietär, `noindex`). Website-Hinweise entsprechend (kein Login nötig); Plugin-Weg bleibt empfohlen (Auto-Update).
- Website: neue Detailseite **`prozess.html`** — Creative Strategy als chronologischer Prozess (Schritt 0–8) mit Skill-für-Skill-Durchklick und „Was du lernst"-Takes; von der Startseite verlinkt.

## v1.2.0 — 2026-06
`creative-briefing`: Oliver-Voss-Haltung + Voice-Over-First.

- **Oliver-Voss-Haltung:** neue `references/voss-principles.md` (verifizierte Voss-Zitate, Ton-Guide, Voss-Hook-Konstruktionen, Quellen). Hook-Library um **Kategorie 16 „Haltung/Anti-Kategorie"** ergänzt. **Haltungs-/Voss-Test** in `copywriting.md` & Qualitäts-Check (Position beziehen statt Kategorie-Claim) — „Klarheit vor Kunst" bleibt explizit oberstes Gesetz. Neue **Voss-Schärfe**-Stufe im Workflow (1/2/3, Default 2; Stufe 3 → `ad-compliance-check`).
- **Voice-Over-First (Doktrin für alle Motion/Video):** das **VO-Script (Spine)** ist das führende, am Stück lesbare Element pro Konzept — VO zuerst, Storyboard mappt `Time·Visual·On-Screen` auf die VO-Beats. Schreibregeln in `creative-formats.md` §5b, Struktur in `document-format.md`, **VO-Flow-Test** im Qualitäts-Check. VO-Retention-Evidenz (Google ABCD, TikTok, Motion — Plattform-Doku vs. Practitioner getrennt) in `field-notes.md` §2b. Motion-Beispiel um VO-Spine-Blöcke erweitert.
- Recherche-basiert (parallele Multi-Agent-Recherche + Zitat-Verifikation gegen die Quell-URLs); nicht belegbare Zitate bewusst weggelassen/markiert.

## v1.1.4 — 2026-06
Anzeigename & Feinschliff.

- `displayName: "ADMKRS – Creative Strategy Suite"` in plugin.json — Plugin erscheint in der UI unter diesem Namen (technischer `name` / Install-ID bleibt `admkrs-creative-suite`).
- Website-Downloads zeigen jetzt auf `releases/latest` (kein versioniertes Nachziehen mehr nötig).

## v1.1.3 — 2026-06
Motion-Ad-Voice-over: Pflicht + Redefluss statt Stakkato.

- **Regel** in `creative-briefing` (SKILL.md, `copywriting-frameworks.md` §4b, `document-format.md`): Motion Ads laufen **immer mit Voice-over**, und das VO muss ein **zusammenhängender, natürlich gesprochener Take** sein, der die Zielgruppe abholt — keine aneinandergereihten Schlagwörter/Slogans. Jede VO-Zeile knüpft an die vorige an; inkl. Vorher/Nachher-Beispiel.
- **Motion-Beispiel-JSON** (`example_motion_briefing.json`): alle 4 Storyboard-VOs von Stakkato auf echten Redefluss umgeschrieben (das Beispiel prägte den Output am stärksten).

## v1.1.2 — 2026-06
Dateinamen-Konvention & Ablage-Best-Practice für generierte Dokumente.

- **Dateiname-Konvention** in `creative-briefing` & `ugc-briefing`: `YYMMDD_BRAND_Product_Type_LANG` — Datum (YYMMDD) immer zuerst (chronologisch sortierbar), **Markt/Sprache am Ende** (`DE`/`EN`/`NL`/`FR`/`AT`), z. B. `260608_NOVA_ProteinCoffee_Statics_DE`.
- **Best Practice:** fertiges .docx in **Google Drive** im Kunden-Ordner unter „Briefings" ablegen (aus Cowork), nicht nur lokal — Speichern/Verschieben in der Kunden-Drive ok, kein ungefragtes Posten in Slack/ClickUp.
- Website: Titel „ADMKRS Creative Strategy Suite" + Tagline; Aktivierung per Satz („Nutze die ADMKRS Creative Suite") erklärt; Claude-Code-Weg eingeklappt/als optional markiert; Cowork-Drive-Ablage ergänzt.

## v1.1.1 — 2026-06
Einheitliches Namens-Schema: alle 11 Skills tragen jetzt den Prefix **`admkrs-cs-`** (z.B. `admkrs-cs-creative-briefing`), damit sie in Claude sauber als ADMKRS-Suite gruppiert auftauchen und mit `/admkrs` gefiltert werden können.

- Ordnernamen, `name:`-Felder und alle internen Querverweise konsistent auf den Prefix umgestellt.
- Team-Website, README & Download-Pakete entsprechend aktualisiert (Skill-Aufruf jetzt z.B. `/admkrs-cs-creative-briefing`).
- Keine inhaltlichen Skill-Änderungen — reines Rename/Branding.

## v1.1.0 — 2026-06
Neuer Skill **ugc-briefing** (11. Skill): generiert ein vollständiges UGC-Creator-Briefing als ADMKRS-.docx (B4 Querformat) — ein Dokument für Creator UND Kunden zugleich.

- **Brand-Foundation + Dual-Purpose-Layer:** Brand-Vorstellung & Datengrundlage für den Creator, Strategie-/KPI-Layer für den Kunden — in einem Dokument.
- **Hook-Bank** (verbal/visuell/Text/Audio) + **Out-of-the-box-/Scroll-Breaker-Layer** (Comment-Reply, Green-Screen, Street-Interview, POV-Skit, Expectation-vs-Reality …).
- **Storytelling-Frameworks** (18) gemappt auf Schwartz-Awareness, Produkt-Typ & Branche + Quick-Selector.
- **Virale Mechaniken 2026** (IG/TikTok/Shorts): Algorithmus-Signale, Share-/Save-Psychologie, Hook-Fenster, Musik-Rechte, Mythen-Check — verifiziert & quellengelabelt.
- **Drehfertige time-coded Scripts** (3 Hooks · 1 Body) + Creator-Delivery-Craft + Disclosure (DE/EU/FTC).
- Reuse der **identischen B4-Builder-Engine** wie creative-briefing; vollständiges fiktives Beispiel (NOVA · Protein Coffee).
- Cross-Refs zu ugc-creator-ops, creative-briefing, ad-compliance-check, performance-reporting.

## v1.0.0 — 2026-06
Erstes Release. 10 verzahnte Skills für Paid-Social- & Google-Creative-Strategy:
creative-strategy-os, creative-briefing, creative-teardown, performance-reporting,
landing-page-cro, ugc-creator-ops, pitch-teardown, google-cross-channel,
offer-promo-strategy, ad-compliance-check.

- Verifizierte 2026-Faktenbasis (Multi-Agent-Recherche + Fact-Check), Vendor-Zahlen markiert.
- Vollständige Creative-Format-Bibliothek (Video + Static) inkl. Style-Decoder & Diversitäts-Matrix.
- Operating-Methods (Research, Volumen, 60/30/10, ASC/Cost-Cap/CAPI/Modular-Testing, Scaling).
- Performance-Reporting (Profit/MER, Attribution 2026, Report-Architektur, Campaign-Tracker).
- 100 % kundenfrei (nur fiktive Beispielmarke „NOVA").
