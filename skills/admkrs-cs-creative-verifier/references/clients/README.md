# Kundenkarten - Index

Hier liegen die kundenspezifischen Do's & Don'ts, die der Briefing Verifier in Schritt 3C
zusätzlich zur generischen Logik anwendet. Eine Datei pro Marke.

## Konvention

- **Dateiname = Marken-Slug:** kleingeschrieben, ohne Leerzeichen/Sonderzeichen, z.B. `nova.md`.
- **Jede Karte beginnt mit:**
  - `**Marke / Aliasse:**` - alle Schreibweisen, unter denen die Marke im ClickUp-Kunde-Feld,
    im Briefing oder auf dem Creative auftauchen kann. Darüber matcht der Verifier, nicht nur
    über den exakten Dateinamen.
  - `**Quelle:**` - woher die Regeln stammen (meist der `#<brand>_intern`-Slack-Canvas „Do's and Don'ts").
  - `**Pflege:**` - Hinweis, dass die Quelle die Wahrheit ist und die Karte die Arbeitskopie.
- **Findings aus Karten werden im Verdict mit `[Kunde]` getaggt.**

## Vorhandene Karten

| Marke | Datei | Quelle | Stand |
|---|---|---|---|
| Nova / nova | `nova.md` | Slack `#nova_intern` Canvas | 2026-02-13 |

## Neue Karte anlegen

1. Im `#<brand>_intern`-Channel die „Do's and Don'ts"-Canvas finden (Slack-Suche:
   `type:canvases in:#<brand>_intern`) und auslesen.
2. Inhalt in eine verify-taugliche Karte überführen - nach Severity-Logik strukturieren
   (Copy-/Brand-kritisch = Blocker; reine Stilpräferenz = niedrig), und klar trennen, was aus
   einem flachen Still prüfbar ist und was nicht.
3. Als `references/clients/<slug>.md` ablegen, in der Tabelle oben eintragen, Skill neu packen.
