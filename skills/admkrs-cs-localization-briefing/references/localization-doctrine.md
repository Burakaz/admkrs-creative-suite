# Übersetzungs-Doktrin, Glossar & Quality-Check

Das hier trennt den Skill von „einfach durch DeepL jagen". Lokalisierung heißt: das Creative wirkt in der Zielsprache wie **native geschriebene Werbe-Copy**, nicht wie eine Übersetzung.

---

## 1 - Übersetzungs-Doktrin (nicht verhandelbar)

- **Nie wörtlich. Immer sinngemäß + sprachgemäß.** Pflicht-Gate vor jeder Zeile: „Würde ein Muttersprachler das genau so sagen?" Wenn nein, neu schreiben. Das Ergebnis muss sich wie Copy lesen, die direkt in der Zielsprache entstanden ist.
- **Hooks-first & kulturelle Adaption.** Referenzen, die nicht übertragen, werden **native neu verankert** - nicht Wort für Wort. Idiome und Wortspiele werden **neu erfunden**, nie übersetzt.
  - Real: DE „Sommermärchen" (WM-2006-Nostalgie) hat in NL keine Entsprechung → Konzept auf „Oranjezomer / voetbalzomer" + „spekkikkers" (NL-Kindheitsanker) umgestellt.
  - Real: das DE-Wortspiel „Kein Märchen" wurde zum nativen Frosch-Prinz-Pun „Deze kikker kun je wel kussen!".
- **Glossar ist bindend** und **überschreibt** die freie Übersetzung. Gesperrte Begriffe (Slogans, Disclaimer, Produkt-/Claim-Wording) exakt in der Glossar-Schreibweise. Beispiel NL-Disclaimer: „T.o.v. vergelijkbare winegums met toegevoegde suiker".
- **Anrede & Register pro Markt festlegen, bevor übersetzt wird:** je/u (NL), tu/vous (FR), tu/usted (ES). Die brand-prägendste Einzelentscheidung der Lokalisierung und der häufigste Grund für Kunden-Reklamationen an Übersetzungen: aus der Brand-Voice oder per Kundenentscheid übernehmen; **fehlt die Vorgabe, flaggen statt raten** - und die Entscheidung dann konsistent durch alle Assets ziehen (Hook, Subline, CTA, VO, Disclaimer).
- **Zahlen-, Währungs- und Datumsformate folgen der Zielmarkt-Konvention** (Währungsposition, Dezimaltrennzeichen, Datumsschreibweisen wie NL „t/m 22/6") - gerade bei Offer-Statics landen sie fast immer auf dem Creative. Die **Werte selbst bleiben 1:1**, nur die Schreibweise wird lokalisiert.
- **Native-/Quality-Check ist Pflicht.** Naturalness prüfen, markieren, wo ein Muttersprachler anders formuliert. **Liegt Native-/Kunden-Feedback vor** (Frame.io-Kommentare, Doc-Edits), **gewinnt dessen Wortwahl** für Ton/Idiom: einarbeiten, Inkonsistenzen vereinheitlichen, Konflikte **intern flaggen** (ClickUp/Chat, nicht im ausgelieferten Dokument; real: Glossar sagt „Bundle", Native schreibt „bundel" → intern geflaggt + Glossar-Update zur Freigabe vorgeschlagen).
- **On-Creative-Constraints bleiben erhalten:** Claims immer mit Sternchen + Fußnote, kein Preis aufs Creative (wenn so gebrieft), Offer-Logik 1:1, **Zeichen-/Längenbudget** beachten. Die Zielsprache ist oft länger als Deutsch: **kürzen statt das Layout sprengen** (Hook/Badge/CTA müssen ins bestehende Design passen).
- **Motion: das VO muss in den bestehenden Schnitt passen.** Übersetztes VO pro Beat muss in der Original-Beat-Dauer **sprechbar** sein (Richtwert: Silbenzahl etwa auf DE-Niveau). Pflicht-Prüfung: laut gegen den bestehenden Cut lesen, im Zweifel kürzen - ein zu langes VO heißt Re-Record oder Re-Cut, der teuerste Lokalisierungs-Fehler bei Motion. Original-Beat-Dauern bei Bedarf als reine Referenz in den internen Handoff geben (keine Timecode-Spalte im Dokument).
- **Compliance je Markt flaggen.** Beispiel NL: „oranje" ist stark mit dem KNVB-Nationalteam verknüpft → nur als Farbe/Sommer-Vibe nutzen, **keine Verbands-, Team-, Spieler- oder Markenbezüge** (kein Wappen, kein gebrandeter Ball). Note ins „Adaptation & Compliance"-Feld. Im Zweifel `admkrs-cs-ad-compliance-check` für die Zielsprache anstoßen.
- **Nichts erfinden.** Zahlen/Claims/Offers bleiben 1:1, nur die Sprache ändert sich. Fehlt ein freigegebener Wert: nachfragen, sonst weglassen/Konzept zurückhalten (kein Placeholder im Dokument); ungesicherte Zielbegriffe intern flaggen (ClickUp/Chat) + Native-Review empfehlen - offene Punkte stehen nicht im ausgelieferten Dokument.
- **Hausregel: kein langer Gedankenstrich „—"** in produzierter Copy, in keiner Zielsprache. Punkt/Komma, notfalls das kurze „–".

---

## 2 - Glossar-Mechanik

- **Input flexibel:** verbundenes Google Sheet, CSV oder inline. Erwartete Spalten: `DE | <LANG…> | Note`.
- **Gematchte Begriffe = gesperrt** und werden exakt übernommen (überschreiben die freie Übersetzung).
- **Kein Glossar für eine Sprache vorhanden?** Der Skill arbeitet trotzdem, **flaggt aber jeden ungesicherten Begriff** und empfiehlt einen Native-Review, bevor es live geht.
- **Glossar darf wachsen:** wird mit dem Kunden ein neuer bindender Begriff/Slogan entschieden, schlägt der Skill ihn als **[Addition]** zur Freigabe vor (nicht heimlich) und legt ihn nach Freigabe ins Projekt-/Brand-Glossar (projektübergreifend wiederverwendbar). Der [Addition]-Marker ist ein interner Prozess-Marker (Chat/ClickUp) und erscheint **nie** im ausgelieferten Dokument.
- **Sprach-agnostisch:** die Zielsprache ist ein Parameter, kein Hardcode. Mit einem hineingegebenen Glossar baut jeder im Team ein Übersetzungs-Briefing in jeder Sprache (NL/FR/ES/IT …).

---

## 3 - Intake & Flag (bevor übersetzt wird)

Sammeln: Quell-Copy (DE, freigegeben), Zielsprache(n), Glossar (bindend), **Quell-Design-Files** (Figma/PSD der DE-Master, bei Motion das AE-/Schnitt-Projekt), **Deadline**, **Abgabeort + Export-Naming** der lokalisierten Assets (Sprach-Suffix `_NL`/`_FR` …), **Formate** (Meta-Standard oder wie DE-Master), **Anrede-Register pro Markt** (Brand-Voice/Kundenentscheid), optional Native-/Kunden-Feedback, optional Markt-Compliance-Regeln. Diese Produktions-Fakten füllen den „At a glance"-Block; fehlt einer, nachfragen, sonst Zeile weglassen.

**Widersprüchliches oder löchriges Quell-Briefing flaggen, bevor du übersetzt** - nicht raten: fehlender Disclaimer, Claim nicht freigegeben, Offer unklar, Preis auf dem Creative trotz „kein Preis"-Regel.

---

## 4 - Quality-Check (vor Übergabe, Pflicht)

- [ ] **Not-literal-Test:** Liest sich jede Zeile wie native geschriebene Copy, nicht wie Übersetzung?
- [ ] **Native-Test:** Würde ein Muttersprachler es genau so sagen? Idiome/Wortspiele neu gebaut statt übertragen?
- [ ] **Glossar-Test:** Alle gesperrten Begriffe/Disclaimer exakt in Glossar-Schreibweise? Konflikte (Glossar vs. Native) geflaggt?
- [ ] **Claim-Test:** Jeder Claim mit Sternchen + Fußnote, Zahlen/Offer 1:1, nichts erfunden?
- [ ] **Längen-Fit-Test:** Passt die Übersetzung ins bestehende Layout (Hook/Badge/CTA nicht gesprengt)?
- [ ] **Register-Test:** Anrede/Register (je/u, tu/vous, tu/usted) wie festgelegt und konsistent durch alle Assets (Hook, Subline, CTA, VO, Disclaimer)?
- [ ] **Format-Konventionen-Test:** Preise, Zahlen und Datumsangaben in Zielmarkt-Konvention, die Werte selbst 1:1?
- [ ] **VO-Timing-Test (Motion):** Jeder VO-Beat in der Original-Beat-Dauer sprechbar (laut gegen den bestehenden Cut gelesen)?
- [ ] **Compliance-Test:** Markt-Risiken (Marken/IP/kulturell) geflaggt? Ggf. `admkrs-cs-ad-compliance-check` für die Zielsprache angestoßen?
- [ ] **English-labels-Test:** Struktur/Labels/Notizen englisch, nur Copy-Zellen DE + Zielsprache?
- [ ] **Motion-2-Spalten-Test:** Genau `On-Screen Text | Voice-Over`, Hook/CTA in der On-Screen-Box gemerged, keine Timecode-Spalte?
- [ ] **Bold-Test:** Jede On-Creative-Zeile fett, mehrzeilige Zellen Zeile-für-Zeile in `<b>…</b>` (nicht ein `<b>` über `\n`)?
- [ ] **Em-Dash-Test:** Kein „—" in produzierter Copy?
- [ ] **Render-Test:** Sonderzeichen sauber (ä/é/ï/ç/„"/·/…), Tabelle kompakt, Haus-Stil wie Referenz?

Abnahme der fertig lokalisierten Creatives: `admkrs-cs-creative-verifier` (gegen dieses Briefing), dann vor Launch `admkrs-cs-ad-compliance-check` für den Zielmarkt.

---
<sub>**ADMKRS Creative Suite** · © ADMKRS GmbH, München · v1.13.0 · interner Gebrauch.</sub>
