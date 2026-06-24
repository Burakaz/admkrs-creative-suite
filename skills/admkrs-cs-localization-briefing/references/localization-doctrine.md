# Übersetzungs-Doktrin, Glossar & Quality-Check

Das hier trennt den Skill von „einfach durch DeepL jagen". Lokalisierung heißt: das Creative wirkt in der Zielsprache wie **native geschriebene Werbe-Copy**, nicht wie eine Übersetzung.

---

## 1 - Übersetzungs-Doktrin (nicht verhandelbar)

- **Nie wörtlich. Immer sinngemäß + sprachgemäß.** Pflicht-Gate vor jeder Zeile: „Würde ein Muttersprachler das genau so sagen?" Wenn nein, neu schreiben. Das Ergebnis muss sich wie Copy lesen, die direkt in der Zielsprache entstanden ist.
- **Hooks-first & kulturelle Adaption.** Referenzen, die nicht übertragen, werden **native neu verankert** - nicht Wort für Wort. Idiome und Wortspiele werden **neu erfunden**, nie übersetzt.
  - Real: DE „Sommermärchen" (WM-2006-Nostalgie) hat in NL keine Entsprechung → Konzept auf „Oranjezomer / voetbalzomer" + „spekkikkers" (NL-Kindheitsanker) umgestellt.
  - Real: das DE-Wortspiel „Kein Märchen" wurde zum nativen Frosch-Prinz-Pun „Deze kikker kun je wel kussen!".
- **Glossar ist bindend** und **überschreibt** die freie Übersetzung. Gesperrte Begriffe (Slogans, Disclaimer, Produkt-/Claim-Wording) exakt in der Glossar-Schreibweise. Beispiel NL-Disclaimer: „T.o.v. vergelijkbare winegums met toegevoegde suiker".
- **Native-/Quality-Check ist Pflicht.** Naturalness prüfen, markieren, wo ein Muttersprachler anders formuliert. **Liegt Native-/Kunden-Feedback vor** (Frame.io-Kommentare, Doc-Edits), **gewinnt dessen Wortwahl** für Ton/Idiom: einarbeiten, Inkonsistenzen vereinheitlichen, Konflikte sichtbar flaggen (real: Glossar sagt „Bundle", Native schreibt „bundel" → flaggen + Glossar-Update vorschlagen).
- **On-Creative-Constraints bleiben erhalten:** Claims immer mit Sternchen + Fußnote, kein Preis aufs Creative (wenn so gebrieft), Offer-Logik 1:1, **Zeichen-/Längenbudget** beachten. Die Zielsprache ist oft länger als Deutsch: **kürzen statt das Layout sprengen** (Hook/Badge/CTA müssen ins bestehende Design passen).
- **Compliance je Markt flaggen.** Beispiel NL: „oranje" ist stark mit dem KNVB-Nationalteam verknüpft → nur als Farbe/Sommer-Vibe nutzen, **keine Verbands-, Team-, Spieler- oder Markenbezüge** (kein Wappen, kein gebrandeter Ball). Note ins „Adaptation & Compliance"-Feld. Im Zweifel `admkrs-cs-ad-compliance-check` für die Zielsprache anstoßen.
- **Nichts erfinden.** Zahlen/Claims/Offers bleiben 1:1, nur die Sprache ändert sich. Fehlt ein Zielbegriff: `[Placeholder: …]` inline, offener Punkt intern getrackt.
- **Hausregel: kein langer Gedankenstrich „—"** in produzierter Copy, in keiner Zielsprache. Punkt/Komma, notfalls das kurze „–".

---

## 2 - Glossar-Mechanik

- **Input flexibel:** verbundenes Google Sheet, CSV oder inline. Erwartete Spalten: `DE | <LANG…> | Note`.
- **Gematchte Begriffe = gesperrt** und werden exakt übernommen (überschreiben die freie Übersetzung).
- **Kein Glossar für eine Sprache vorhanden?** Der Skill arbeitet trotzdem, **flaggt aber jeden ungesicherten Begriff** und empfiehlt einen Native-Review, bevor es live geht.
- **Glossar darf wachsen:** wird mit dem Kunden ein neuer bindender Begriff/Slogan entschieden, schlägt der Skill ihn als **[Addition]** zur Freigabe vor (nicht heimlich) und legt ihn nach Freigabe ins Projekt-/Brand-Glossar (projektübergreifend wiederverwendbar).
- **Sprach-agnostisch:** die Zielsprache ist ein Parameter, kein Hardcode. Mit einem hineingegebenen Glossar baut jeder im Team ein Übersetzungs-Briefing in jeder Sprache (NL/FR/ES/IT …).

---

## 3 - Intake & Flag (bevor übersetzt wird)

Sammeln: Quell-Copy (DE, freigegeben), Zielsprache(n), Glossar (bindend), optional Native-/Kunden-Feedback, optional Markt-Compliance-Regeln.

**Widersprüchliches oder löchriges Quell-Briefing flaggen, bevor du übersetzt** - nicht raten: fehlender Disclaimer, Claim nicht freigegeben, Offer unklar, Preis auf dem Creative trotz „kein Preis"-Regel.

---

## 4 - Quality-Check (vor Übergabe, Pflicht)

- [ ] **Not-literal-Test:** Liest sich jede Zeile wie native geschriebene Copy, nicht wie Übersetzung?
- [ ] **Native-Test:** Würde ein Muttersprachler es genau so sagen? Idiome/Wortspiele neu gebaut statt übertragen?
- [ ] **Glossar-Test:** Alle gesperrten Begriffe/Disclaimer exakt in Glossar-Schreibweise? Konflikte (Glossar vs. Native) geflaggt?
- [ ] **Claim-Test:** Jeder Claim mit Sternchen + Fußnote, Zahlen/Offer 1:1, nichts erfunden?
- [ ] **Längen-Fit-Test:** Passt die Übersetzung ins bestehende Layout (Hook/Badge/CTA nicht gesprengt)?
- [ ] **Compliance-Test:** Markt-Risiken (Marken/IP/kulturell) geflaggt? Ggf. `admkrs-cs-ad-compliance-check` für die Zielsprache angestoßen?
- [ ] **English-labels-Test:** Struktur/Labels/Notizen englisch, nur Copy-Zellen DE + Zielsprache?
- [ ] **Motion-2-Spalten-Test:** Genau `On-Screen Text | Voice-Over`, Hook/CTA in der On-Screen-Box gemerged, keine Timecode-Spalte?
- [ ] **Bold-Test:** Jede On-Creative-Zeile fett, mehrzeilige Zellen Zeile-für-Zeile in `<b>…</b>` (nicht ein `<b>` über `\n`)?
- [ ] **Em-Dash-Test:** Kein „—" in produzierter Copy?
- [ ] **Render-Test:** Sonderzeichen sauber (ä/é/ï/ç/„"/·/…), Tabelle kompakt, Haus-Stil wie Referenz?

Abnahme der fertig lokalisierten Creatives: `admkrs-cs-creative-verifier` (gegen dieses Briefing), dann vor Launch `admkrs-cs-ad-compliance-check` für den Zielmarkt.

---
<sub>**ADMKRS Creative Suite** · © ADMKRS GmbH, München · v1.12.0 · interner Gebrauch.</sub>
