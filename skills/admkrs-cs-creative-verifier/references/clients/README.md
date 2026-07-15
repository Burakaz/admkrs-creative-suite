# Kundenkarten - Index

Hier liegen die kundenspezifischen Do's & Don'ts, die der Creative Verifier
(`admkrs-cs-creative-verifier`) in Schritt 3C zusätzlich zur generischen Logik anwendet.
Eine Datei pro Marke.

> **Wichtig (Datenschutz): Echte Kundenkarten liegen NICHT in diesem Repo.** Das Repo ist
> öffentlich - reale Marken-Regeln, interne Channel-/Task-IDs und Kunden-Interna gehören in die
> interne Ablage (Kunden-Drive bzw. interner Ordner) und werden dem Verifier **zur Laufzeit**
> gereicht: Karte an den Chat anhängen, Inhalt einfügen oder den internen Pfad nennen.
> Im Repo liegt nur die **fiktive Beispielkarte `nova.md`** als Struktur-Vorlage.

## Konvention

- **Dateiname = Marken-Slug:** kleingeschrieben, ohne Leerzeichen/Sonderzeichen, z.B. `nova.md`.
- **Jede Karte beginnt mit:**
  - `**Marke / Aliasse:**` - alle Schreibweisen, unter denen die Marke im ClickUp-Kunde-Feld,
    im Briefing oder auf dem Creative auftauchen kann. Darüber matcht der Verifier, nicht nur
    über den exakten Dateinamen.
  - `**Quelle:**` - woher die Regeln stammen (meist die „Do's and Don'ts"-Canvas im internen Brand-Channel).
  - `**Pflege:**` - Hinweis, dass die Quelle die Wahrheit ist und die Karte die Arbeitskopie.
- **Findings aus Karten werden im Verdict mit `[Kunde]` getaggt.**

## Karten in diesem Repo

| Marke | Datei | Zweck |
|---|---|---|
| NOVA (fiktiv) | `nova.md` | Struktur-Vorlage, keine echte Marke |

## Neue Karte anlegen (intern, nicht ins Repo)

1. Im internen Brand-Channel die „Do's and Don'ts"-Canvas finden und auslesen.
2. Inhalt in eine verify-taugliche Karte überführen - nach Severity-Logik strukturieren
   (Copy-/Brand-kritisch = Blocker; reine Stilpräferenz = niedrig), und klar trennen, was aus
   einem flachen Still prüfbar ist und was nicht. Struktur wie `nova.md`.
3. **In der internen Ablage speichern** (Kunden-Drive unter „Briefings/Verifier" oder interner
   Ordner) - nie ins öffentliche Repo committen. Beim Verifier-Lauf die Karte mitgeben.
