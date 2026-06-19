# ADMKRS Designfehler Cheat-Sheet — Prüfraster

7 Kategorien, 48 Prüfpunkte. Dies ist das Raster für den **Design-/Handwerks-Pass**
des Creative Verifiers (Schritt 3B). Dieser Pass ist Pflicht und läuft bei jedem
Durchlauf — auch wenn die Briefing-Treue top ist. Ein perfekt gebrieftes Still mit
Tippfehler, Clipping oder verzerrtem Logo ist trotzdem tot.

**So nutzt du es:** Diagnostisch, nicht als Häkchenliste. Geh pro Creative die 7
Kategorien durch und flagge nur **echte** Fehler — nicht jeden theoretisch denkbaren
Punkt. 48 Punkte heißt nicht 48 Findings. Einen Punkt, den du aus dem Bild nicht
sicher beurteilen kannst, schreibst du unter „Was ich nicht prüfen kann", nicht in die
Findings. Jedes Design-Finding kriegt eine Severity (siehe Severity-Map unten) und das
Tag **[Design]**, damit Handwerk von Briefing-Treue unterscheidbar bleibt.

## Inhalt

- [1. Inhalt (7)](#1-inhalt-7)
- [2. Typografie & Text (9)](#2-typografie--text-9)
- [3. Bilder & Assets (8)](#3-bilder--assets-8)
- [4. Layout & Abstände (7)](#4-layout--abstände-7)
- [5. Farbe & Kontraste (4)](#5-farbe--kontraste-4)
- [6. Logo (7)](#6-logo-7)
- [7. Formate & Artboards (6)](#7-formate--artboards-6)
- [Severity-Map](#severity-map-design-findings)
- [Nicht aus dem Screenshot prüfbar](#nicht-aus-dem-screenshot-prüfbar)

---

## 1. Inhalt (7)

1. **Klar, um was es geht?** Botschaft sofort erkennbar, ohne Entschlüsseln.
2. **Keine Health Claims.** Keine unzulässigen Gesundheitsversprechen. (rechtlich → hoch; Vollprüfung → `admkrs-cs-ad-compliance-check`)
3. **Produkte richtig dargestellt.** Richtiges Produkt, Variante, realistische Größe.
4. **Klarer Angle / Pain Point.** Konkreter Pain der Zielgruppe, nicht generisch.
5. **Klarer CTA.** Eindeutiger nächster Schritt, sichtbar platziert.
6. **Brief & Pflichtangaben.** Claims, Disclaimer, Mandatories vollständig.
7. **Keine Banned-Buzzwords (ADMKRS-Hausregel).** Keine Generic-AI-Floskeln auf dem Creative („game-changer", „elevate your", „unlock the power of", „revolutionary", „in today's fast-paced world" …). Treffer = mittel. **Liste ist Autorität in `admkrs-cs-creative-briefing/references/copywriting.md`** — dort prüfen, nicht hier parallel pflegen.

## 2. Typografie & Text (9)

1. **Rechtschreibung.** Vor Abgabe Korrektur lesen. Tippfehler in Live-Copy = Blocker. (→ hoch)
2. **Groß-/Kleinschreibung.** Konsistent bei Headlines, Labels, CTAs.
3. **ß → SS in Versalien.** In Caps wird ß zu SS.
4. **Anführungszeichen.** Typografische „…" statt gerader Zeichen.
5. **Brand-Font.** Nur Brand-Fonts, kein Stock-Sans als Fallback.
6. **Schriftgröße (Mobile).** Fließtext ≥ 16 px, UI-Labels ≥ 14 px.
7. **Doppelte Leerzeichen.** Nach Copy-Paste prüfen. (→ niedrig)
8. **Konsistente Schnitte.** Bold/Regular/Light nicht willkürlich mischen.
9. **Kein langer Gedankenstrich „—" (Em-Dash) in On-Creative-Copy (ADMKRS-Hausregel).** Reine String-Prüfung über Hook/Subline/USPs/CTA/Disclaimer. Treffer = mittel. Stattdessen Punkt/Komma, notfalls das kurze „–". (Quelle: `admkrs-cs-creative-briefing/references/copywriting.md` §8.)

## 3. Bilder & Assets (8)

1. **Kein weißer Rand zur Kante.** Bild füllt die Fläche voll.
2. **Bleed/Beschnitt.** Vollflächen bis an/über den Rand. (oft nicht aus Flat-Render prüfbar)
3. **Wirkt KI-generiert?** Artefakte: Hände, Details, generische Optik.
4. **Gradient ohne harte Kante.** Verläufe weich — harte Kanten wirken fehlerhaft.
5. **Nicht verzerrt.** Seitenverhältnis gesperrt, nicht gestreckt. (→ hoch)
6. **Auflösung.** Nicht pixelig, v.a. auf Großflächen.
7. **Freisteller ohne Halo.** Sauberer Rand ums Motiv.
8. **Keine Placeholder.** Kein Stock-/Lorem-Platzhalter im finalen File. (→ hoch)

## 4. Layout & Abstände (7)

1. **Am Grid.** Snap to Grid, nichts frei platziert.
2. **CTA-Text zentriert.** Padding gleich, Text v. & h. zentriert.
3. **Alignment geprüft.** Alles zueinander ausgerichtet, auch mehrsprachig.
4. **Keine ungewollten Überschneidungen.** Nach Verschieben prüfen.
5. **Kein Clipping.** Text nicht abgeschnitten (dynamische Rahmen prüfen). (→ hoch)
6. **Störer-Neigung.** 5–15° und immer ins Bild hinein geneigt.
7. **Ausrichtung.** Fast-ausgerichtete Objekte wirken schlampig.

## 5. Farbe & Kontraste (4)

1. **Kontrast.** Lesbarkeit, WCAG AA. (wenn Lesbarkeit kippt → hoch)
2. **Farben aus dem System.** Nur Brand-Set.
3. **Hex statt Transparenz.** Transparenz verschiebt Farben. (meist nicht aus dem Bild prüfbar)
4. **Keine unbeabsichtigte Kontur.** Bei Formen Kontur deaktivieren, wenn ungewollt.

## 6. Logo (7)

1. **Richtige Logo-Version.** Nur freigegebene Version aus dem Brand-Ordner.
2. **Nicht gestreckt/verzerrt.** Nur proportional skalieren. (→ hoch)
3. **Geeigneter Hintergrund.** Genug Kontrast, kein unruhiges Motiv.
4. **Schutzzone.** Clear Space gemäß Guidelines.
5. **Größe/Platzierung.** Mindestgröße, keine Überschneidung.
6. **Farbvariante.** Hell/Dunkel je nach Hintergrund.
7. **Nie geneigt / nur als Einheit.** Logo nicht neigen, nicht mit Schrift verbasteln.

## 7. Formate & Artboards (6)

1. **Social-Formate (Meta-Standard).** **4:5 (1080×1350) + 9:16 (1080×1920) — kein 1:1** (im Suite-Briefing-Standard v1.9 abgeschafft). Ein geliefertes 1:1 ohne Sonderformat-Briefing = Finding, kein erwartetes Format. Sonderformate (andere Plattformen) nur, wenn der Brief sie mit Plattform + Pixeln ausweist.
2. **Kanalspezifische Formate.** Amazon, Criteo, Display laut Brief.
3. **Artboard-Benennung.** Schema „Social_Story_v1". (nicht aus dem Bild prüfbar)
4. **Exportformat.** JPG Foto · PNG Transp. · SVG Vektor · PDF Print. (nicht aus dem Bild prüfbar)
5. **Drive-Link freigegeben.** Für alle Beteiligten. (nicht aus dem Bild prüfbar)
6. **Sprachanpassung.** Buttons, Disclaimer, Overlays übersetzt?

---

## Severity-Map (Design-Findings)

Mappt Cheat-Sheet-Treffer in die 3-Stufen-Leiter des Verifiers. Severity ist
kontextabhängig — ein Tippfehler im Fließtext-Disclaimer wiegt weniger als einer in
der Headline. Nutze Urteilsvermögen, nicht die Tabelle stur.

- **hoch (Blocker, muss zurück):** Rechtschreibfehler in Live-Copy; Health Claim;
  Logo falsch / verzerrt / falsche Version; Bild verzerrt; Placeholder im finalen File;
  Text-Clipping; Kontrast so niedrig, dass Lesbarkeit kippt; weißer Rand / fehlender
  Bleed bei Vollflächen-Format.
- **mittel (sollte zurück):** ß→SS-Fehler; gerade statt typografische Anführungszeichen;
  inkonsistente Schnitte; harte Gradient-Kante; Freisteller-Halo; Störer falsch geneigt
  (Winkel/Richtung); Alignment-/Grid-Abweichungen; Farbe außerhalb Brand-Set;
  Logo-Schutzzone verletzt; sichtbare KI-Artefakte; **Em-Dash „—" in On-Creative-Copy**;
  **Banned-Buzzword auf dem Creative**; geliefertes 1:1 ohne Sonderformat-Briefing.
- **niedrig (erwähnen, nicht blockierend):** doppelte Leerzeichen; minimale
  Grid-Abweichung; sehr feine stilistische Themen.

## Nicht aus dem Screenshot prüfbar

Diese Punkte brauchen das Arbeitsfile / Drive / Brand-Ordner, nicht den gerenderten
Still — gehören per Default in „Was ich nicht prüfen kann":

- Bleed/Beschnitt über die Artboard-Kante hinaus (3.2)
- Transparenz vs. Hex (5.3)
- Artboard-Benennung (7.3)
- Exportformat (7.4)
- Drive-Link-Freigabe (7.5)
- Exakte Brand-Font-Datei (2.5 — Stock-Sans erkennt man, die genaue Font-Identität oft nicht)
