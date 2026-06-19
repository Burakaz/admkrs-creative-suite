# Changelog — ADMKRS Creative Suite

## v1.10.2 — 2026-06
Fix: `admkrs-cs-creative-verifier` ließ sich in der App nicht installieren — die `description` im SKILL.md war 1122 Zeichen lang (Limit: 1024). Gekürzt auf 957 (Trigger erhalten). Hinweis: `claude plugin validate` prüft diese Grenze NICHT — nur der App-Installer. Künftig description ≤ 1024 halten.

## v1.10.1 — 2026-06
Verifier-Pre-Mortem im Briefing-Prozess.

- **Neuer Quality-Check in `admkrs-cs-creative-briefing`:** „Verifier-Pre-Mortem" — vor der Übergabe gegenprüfen, ob ein Creative, das dieses Briefing 1:1 umsetzt, den `admkrs-cs-creative-verifier` bestehen würde (Hook-Wirksamkeit, Text-Budget, Treue der gesperrten Fakten). Macht den Abnahme-Maßstab zur Schreib-Zielvorgabe und fängt schwache Hooks ab, bevor der Designer baut. Gleiche Standards (`copywriting.md`), beide Enden der Kette.

## v1.10.0 — 2026-06
Neuer 15. Skill: **`admkrs-cs-creative-verifier`** — das Abnahme-Gate, das der Suite gefehlt hat (Beitrag eines Kollegen, in die Suite eingebürgert und mit Creative-Strategy-Wissen geschärft).

**Der neue Skill:**
- **Abnahme-Gate** zwischen Produktion und Launch: prüft fertige Creatives (Stills/Videos/Carousels) gegen das Briefing + Handwerk, bevor sie raus/in den Ads Manager gehen. Vier Dimensionen, ein Lauf — **Briefing-Treue · Hook-Wirksamkeit · Designhandwerk (48-Punkte-Cheat-Sheet) · Kundenspezifik** (Kundenkarten). Opinionierter Verdict mit Severity + Tags `[Briefing] · [Wirksamkeit] · [Design] · [Kunde]`.
- **Eingebürgert:** Prefix `admkrs-cs-`, vier tote Fremd-Referenzen gemappt (`admkrs-design-check` entfällt — Design-Pass ist inline; `briefing-creator/-processor` → `creative-briefing`; `meta-ads-creative` → `creative-strategy-os`), Briefing-Input auf das Suite-Format v1.9 (liest „Auf einen Blick" + Tabelle, **Bold = On-Creative** als Brücke), Sicherheits-Hausregeln + Footer im Suite-Stil, keine Personennamen.
- **Mit unserem Wissen geschärft:** neuer **Hook-Wirksamkeits-Pass** (Kontext-frei-Test, eine-Idee, Text-Budget — diagnostisch, textet nie um, zitiert `copywriting.md`); **Visual-Job statt Visual-Match** (bei leerer Visual-Direction prüft er gegen Idee/Hook/Angle — passt zum v1.9-„Default leer"); **Hausregel-Checks** ins Cheat-Sheet (Em-Dash, Banned-Buzzwords — referenziert, nicht dupliziert); **1:1 als erwartetes Format korrigiert**; **Learned-Log-Rückfluss** (Muster zurück ins Flywheel, als Entwurf).
- **Anti-Bloat:** keine Performance-Prognose, keine Hook-Rewrites, keine Persona-Map-Bewertung, kein Score-Dashboard, keine Compliance-Vollprüfung — diagnostiziert und verweist.

**Verdrahtung in der Suite:** `creative-strategy-os` (Phase 5: Abnahme vor Launch), `creative-briefing` (neuer Schritt 9), `ad-compliance-check` (läuft NACH dem Verifier), `landing-page-cro` (Claim-Deckung vs. Message-Match abgegrenzt), die 4 Format-Türen (Abnahme-Satz). README, Website-Katalog (15. Karte) und Download-Liste ergänzt.

## v1.9.0 — 2026-06
`creative-strategy-os` für planlose Media Buyer verständlich gemacht + definitorischer Rigor (inspiriert vom Influee-5-Pillar-Framework, gegengeprüft und auf unser Phasen-Modell gemappt — kein paralleles Framework, kein Vendor-Material übernommen).

- **Neuer „START HIER"-Block** ganz oben in der SKILL.md (die Rolle stand vorher erst weit unten): der Job eines Creative Strategists in einem Absatz (vom Targeting- zum Lern-System-Betreiber), die **Creative-Map** als zentraler Output, plus eine **4-Begriffe-Box** (Persona/Pain/Angle/Awareness) mit der Leiter **Kundenzitat → Pain → Angle → Hook → Script**.
- **Pain ≠ Angle** als explizite Schicht in Phase 2 (`research-diversity-testdesign.md` §2.1b): warum schwache Ads „wie Marketing klingen", Prüfregel „klingt der Pain wie eine Headline, ist er zu hoch", High-Frequency-Anker (5+ = Hook-Struktur).
- **Persona-Disziplin** geschärft: Definition über **Lebenssituation + Beziehung zum Problem** (nicht Awareness/Mindset/Funnel/Demografie), **Konsistenz-Test** über alle Awareness-Stufen, **Sub-Persona-Split**.
- **Awareness = was das SKRIPT sagt** (nicht was der Kunde denkt): 5 Script-Jobs als Tabelle (Unaware→Most-Aware), macht Schwartz von Buzzword zu Schreib-Anweisung.
- **Ausführbarer Diversity-Check:** Andromeda **NEW/REPEAT/VARIANT** + „eine Strukturachse mutieren" (Talent/Shot/Pacing/Opener) + Konzentrations-Check (>40 % gleiches Format).
- **Durchgehender Worked Example** (eine fiktive Brand von Kundenzitat bis Concept-Matrix-Zeile + Hypothese) — die Maschine einmal komplett.
- Templates aktualisiert: Concept-Matrix mit **Coverage-Spalte** (Scaling/Testing/Not-Running) + Empty-Cell-Disziplin; Test-Plan mit **Hypothesen-Schablone**.

**Briefings — Visual-Direction radikal reduziert:**
- **Visual-Direction-Spalte: Default leer.** Die Spalte bleibt im Schema, aber wird nur gefüllt, wenn das Konzept eine visuelle Richtung zwingend braucht oder eine klare Kunden-Vorgabe existiert — sonst leer (Designer entscheidet die Optik). Keine Detail-/Stimmungs-Beschreibung, keine „clean & premium"-Floskeln, keine Formate/Farben. Faustregel: ist das Creative auch ohne Visual-Direction klar gebrieft, bleibt die Zelle leer.
- Abgrenzung: betrifft die Static-/Carousel-`Visual-Direction`-Spalte. Bei Motion/Video bleibt die Storyboard-`Visual`-Spalte die funktionale Beat-Anweisung (knapp, nur was Animation/Schnitt braucht).
- Neuer **Visual-Reduktions-Test** im Quality-Check; NOVA-Statics-Beispiel entsprechend entschlackt (3 von 5 Visual-Direction-Zellen jetzt leer).
- Bewusst NICHT übernommen: Influees Master-Prompt-Monolith, Creator-Casting-MCP (liegt bei uns in `ugc-creator-ops`/`ugc-briefing`), Production-Brief-Generator (Job des `creative-briefing`-Companions), Format-Liste, Vendor-Marker.

## v1.8.0 — 2026-06
Das schlanke Ausführer-Dokument: alles raus, was Designer/Editor/Creator nicht zum Bauen brauchen. Plus Text-Budget + CTA-Spalte (zusammengeführt aus dem unveröffentlichten v1.7.2).

**Neues Dokument-Skelett (Statics/Motion/Video) — Ausführer-Test für jeden Block:**
- **Alle Callouts vor der Arbeit gestrichen:** kein `todo` („Vor Produktion klären"), kein `anchor` („Strategischer Anker"), kein `locked` („Gesperrt 1:1"). Offene Punkte leben in ClickUp/Chat; im Dokument markiert nur `[Platzhalter: …]` **inline** die betroffene Stelle. Die Strategie-Idee wandert als **`Idee`-Zeile** in „Auf einen Blick" bzw. die Konzept-keyvalue. Gesperrte Texte stehen fett in den Zellen — eine Quelle, kein Drift.
- **3-Zeilen-Legende** ersetzt die Callouts: Fett = landet auf dem Creative · Alle Texte 1:1 übernehmen · [Platzhalter] nicht selbst füllen.
- **Auch gestrichen:** `h1 "Briefing"`, Intro-Absätze (lede/p), Family-Label, Target-Audience pro Konzept, `outro` (End-Card ist jetzt **letzte timecodierte Storyboard-Zeile**).
- **Neu in „Auf einen Blick":** **Assets-Zeile (Pflicht)** — Logo/Fonts/Packshots/Footage/Referenz-Ads-Link (der häufigste Produktionsblocker) · **Abgabe** (Lieferort + Spec) · Motion/Video zusätzlich **Deliverables-Zählung** (Konzepte × Hooks × Formate = Exporte) und **VO & Captions** (Quelle + Stil). „Wichtige Infos" nur noch, wenn konkret.
- **Hooks präziser:** je Hook-Variante eine zweite Zeile „Visual 0–2 s"; Video-Storyboards mit Clip-Referenz (Dateiname/Timecode). VO-Spine explizit als Copy-Block für die VO-Produktion (wortidentisch mit Storyboard-VO-Spalte).
- **Stand-Zeile im dek** („Stand 05.06. · freigegeben") als Freigabe-Anker statt Problemliste.
- **Rollen statt Namen (Pflicht):** keine Personennamen im Dokument — „zurück an ADMKRS", nie „[Name] fragen". Neuer **Namen-Test** im Quality-Check.

**UGC-Briefing: Creator-First**
- Neue Reihenfolge: **Dein Auftrag → Lieferung & Specs → Darf & darf nicht → Produkt & Ton → Scripts** — der Kunden-Strategie-Layer (Persona, Angles, Hypothesen) steht als **Anhang ganz hinten** (oder als separates Kunden-Doc aus derselben JSON).
- **„Darf & darf nicht"-Tabelle** ersetzt die locked-Callouts; Scripts in **Beat-Blöcken** (Hook/Problem/Demo/CTA mit Richtwert-Sekunden) statt starrem Timecode; **Scope explizit** (Stückzahl ausgerechnet, Scroll-Breaker klar als Bonus); neu im Intake: Aussprache des Markennamens, Produkt-Logistik, Upload-Ort, roh/geschnitten, Referenz-Videos.

**Text-Budget + CTA (aus v1.7.2, unveröffentlicht):**
- **Text-Budget (Pflicht):** Default ist **Hook + Subline, das reicht meistens**. USPs nur, wenn das Konzept sie braucht — dann max. 3 Stichpunkte à 2–4 Wörter oder ein kurzer Satz. Nie USP-Liste + Zusatz-Sätze + Badges stapeln.
- **Neue optionale `CTA`-Spalte:** gestaltetes On-Creative-CTA-Element (2–4 Wörter, fett, z. B. „Jetzt probieren") — öfter einsetzen, wann immer es dem Creative hilft (DR/Offer/Hero). Weiterhin: kein Meta-Ads-Manager-Button im Briefing. Schema: `[# | Static | Dateiname | Produkt | Creative Format | Hook | Subline | USPs/Badge | CTA | Disclaimer | Visual-Direction]`.
- **„Standard schlägt Vorlage":** Auch beim Fortschreiben älterer Briefings gilt immer das aktuelle Tabellen-Schema — alte Strukturen migrieren, nie kopieren.
- **Kein Angle-/Framework-Label** („Pain", „Objection") in der Designer-Tabelle — Strategie-Notation bleibt im Strategie-Pass.
- Neue Checks: **Schema-Test**, **Text-Budget-Test**, **Ausführer-Test**, **Namen-Test**, **Creator-First-Test**, **Scope-Test**; alle 3 Beispiel-Briefings (Statics/Motion/UGC) auf das neue Skelett umgebaut.

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
