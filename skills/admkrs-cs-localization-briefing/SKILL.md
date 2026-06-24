---
name: admkrs-cs-localization-briefing
description: >
  Erstellt aus einem freigegebenen DE-Creative-Briefing (Statics, Carousel, Motion Ad) plus
  Glossar und Zielsprache ein Lokalisierungs-Briefing als ADMKRS-.docx für internationale
  Design-/Video-Teams. Struktur, Labels und Notizen auf Englisch; die Copy-Zellen tragen
  Original (DE) + eine sinngemäße, native Übersetzung, nie wörtlich. Sprach-agnostisch (NL, FR,
  ES, IT …). Use this skill when the user wants to translate or localize statics, carousels or
  motion ads, says "übersetzen", "Lokalisierung", "NL-Version", "FR-Version", "localize this
  briefing/asset", "adapt for the NL/FR market", "mach die holländische Variante", or feeds a
  glossary plus source briefing. Motion Ads im 2-Spalten-Format (On-Screen Text | Voice-Over).
  Nutzt die gemeinsame Builder-Engine von admkrs-cs-creative-briefing; pairs with
  admkrs-cs-ad-compliance-check (Markt-Recht) und admkrs-cs-creative-verifier (Abnahme).
---

# ADMKRS Localization Briefing

Verwandelt ein **freigegebenes deutsches Creative-Briefing** (Statics, Carousel, Motion Ad) zusammen mit einem **Glossar** und einer **Zielsprache** in ein **Lokalisierungs-Briefing als .docx**, das ein internationales Team ohne Rückfrage umsetzt. **Sibling** zu `admkrs-cs-creative-briefing`: gleiche Builder-Engine, gleicher Haus-Stil (B4 Querformat, schwarze Tabellen-Header, Arial, Zebra).

**Zwei harte Leitplanken, die das von „einfach übersetzen" trennen:**
1. **Struktur auf Englisch** (Labels, Header, Spalten, Legende, Notizen) - internationale Teams arbeiten daran. Nur die **Copy-Zellen** tragen **Original (DE)** + **Übersetzung (Zielsprache)**.
2. **Nie wörtlich.** Immer sinngemäß + sprachgemäß, geprüft auf native Sprache. Idiome, Wortspiele und Kulturreferenzen werden **neu verankert**, nicht Wort für Wort übertragen.

## Vorgehen
1. **Intake & Flag.** Quell-Copy (DE, freigegeben), Zielsprache, Glossar (bindend), optional Native-/Kunden-Feedback und Markt-Compliance-Regeln sammeln. Widersprüche/Lücken im Quell-Briefing melden, bevor übersetzt wird (fehlender Disclaimer, Claim nicht freigegeben, Offer unklar). Nicht raten.
2. **Übersetzen.** Glossar (bindend, überschreibt freie Übersetzung) anwenden, sinngemäß übertragen, Hooks/Idiome/Kulturanker **native neu** bauen. Längenbudget beachten (Zielsprache oft länger → kürzen statt Layout sprengen).
3. **Native-/Quality-Check.** Naturalness, Längen-Fit, Claims/Compliance intakt; vorhandenes Native-Feedback einarbeiten und vereinheitlichen; Konflikte (inkl. Glossar vs. Native) flaggen. Checkliste in `references/localization-doctrine.md`.
4. **Dokument bauen.** Über `../admkrs-cs-creative-briefing/assets/build_briefing.js` (englische Labels; Statics-Vergleichstabelle `Asset | Element | Original (DE) | Translation (LANG)` / Motion 2-Spalten `On-Screen Text | Voice-Over`). Muster: `examples/`. Format-Regeln: `references/document-format.md`.
5. **Render-Check.** docx → PDF → JPEG; Sonderzeichen (ä/é/ï/ç/„"/·/…) und Seiten-Fit prüfen.
6. **Als Entwurf liefern.** `present_files`, Entscheidungen + offene Flags listen. **Nichts posten/zuweisen/senden ohne explizite Freigabe.**

## Leitprinzipien (kurz - Details in `references/localization-doctrine.md`)
**Native vor wörtlich · Glossar ist bindend · Hooks und Wortspiele neu verankern statt übersetzen · Längenbudget halten · Markt-Compliance flaggen · nichts erfinden (Zahlen/Claims/Offers 1:1).** Sprach-agnostisch: die Zielsprache ist ein Parameter, kein Hardcode. Kein Glossar vorhanden → trotzdem arbeiten, aber jeden ungesicherten Begriff flaggen und Native-Review empfehlen. **Mehrzeilige On-Creative-Zellen: jede Zeile einzeln in `<b>…</b>`** (der Builder trägt Bold nicht über `\n`).

## References lesen
`references/document-format.md` (Struktur, Tabellen-Specs, Builder, Mehrzeilen-Bold-Regel) · `references/localization-doctrine.md` (Übersetzungs-Doktrin, Glossar-Mechanik, Quality-Check). Engine + Haus-Stil: `../admkrs-cs-creative-briefing/references/document-format.md`. Copy-Handwerk (Klarheit, Banned-Buzzwords, kein „—"): `../admkrs-cs-creative-briefing/references/copywriting.md`.

## Sicherheit
Nie senden/posten/zuweisen/löschen ohne explizite Freigabe; das Briefing geht **als Entwurf** an Team/Kunde. Rollen statt Namen im Dokument. Abnahme der lokalisierten Creatives durch `admkrs-cs-creative-verifier`, dann vor Launch `admkrs-cs-ad-compliance-check` für den Zielmarkt.

<sub>**ADMKRS Creative Suite** · © ADMKRS GmbH, München · v1.12.0 · interner Gebrauch · Sibling zu `admkrs-cs-creative-briefing` (gemeinsame Engine, keine Duplikate).</sub>
