# LP-Brief-Blueprint - Seitenaufbau je Seitentyp + Brief-Skelett

Ein LP-Brief ist eine **Bau-Anweisung** für den Ausführer (Designer, Dev, Copywriter), kein Strategie-Essay. Es gelten dieselben Prinzipien wie im Haus-Briefing-Standard: nur rein, was zum Bauen gebraucht wird; fehlende Werte im Intake aktiv nachfragen, sonst Zeile weglassen (keine Platzhalter im ausgelieferten Brief); Rollen statt Personennamen; offene Punkte leben in ClickUp/Chat, nicht im Dokument.

**Subtraktions-Test für jede Sektion:** Hat sie einen eigenen Job, den keine andere Sektion schon macht? Nein → fliegt. Eine kurze LP mit klarem Job pro Sektion schlägt eine lange mit Füllmaterial.

---

## 1 - Dedizierte LP (Cold-Paid-Standard)

Sektions-Reihenfolge mit Job pro Sektion. Reihenfolge ist der Default, kein Gesetz - aber jede Abweichung braucht einen Grund.

| # | Sektion | Job |
| --- | --- | --- |
| 1 | **Hero (above the fold)** | Message-Match einlösen: Headline spiegelt den Ad-Hook, Visual = gleiche Szene/gleiches Produkt wie die Ad. Dazu Value-Prop und EIN tappbarer Primär-CTA. Keine Navigation, keine Exits außer Conversion. |
| 2 | **Proof-Leiste** | Sofort-Glaubwürdigkeit in einer Zeile direkt unter dem Hero: Bewertungsschnitt, Kundenzahl, Presse/Badges. Konkret und quantifiziert, keine Floskel-Badges. |
| 3 | **Problem / Mechanismus** | Das Warum hinter dem Versprechen: Problem benennen, dann den Mechanismus erklären, der das Produkt anders macht. Keine Feature-Liste. |
| 4 | **Benefits konkret** | Was ändert sich für die Person: 3-5 Benefits, je ein konkreter, freigegebener Fakt statt Floskel. |
| 5 | **Social Proof im Detail** | Einwände über Dritte entkräften: spezifische, quantifizierte Testimonials (Name, konkretes Ergebnis, Foto), UGC-Bilder nahe CTA. |
| 6 | **Offer-Stack + Risk-Reversal** | Kaufentscheidung leicht machen: was ist drin, Gesamtpreis inkl. Versand früh und transparent, Garantie/Geld-zurück. |
| 7 | **FAQ** | Die letzten echten Einwände (Lieferzeit, Rückgabe, Anwendung, Kompatibilität): 4-6 Fragen, aus Reviews/Support-Tickets gezogen, nicht ausgedacht. |
| 8 | **Sticky-CTA (mobil)** | Conversion jederzeit erreichbar: erscheint nach dem Hero-Scroll, verdeckt weder Inhalt noch Consent-Banner. |

**Copy-Hierarchie (von oben nach unten gewichtet):**
- **Hero-Headline** - Spiegel des Ad-Hooks, wichtigste Zeile der Seite.
- **Sektions-Headlines** - müssen allein gelesen die Kurzgeschichte der Seite erzählen (Skim-Test: nur Headlines lesen, versteht man Angebot + Warum?).
- **Body-Copy** - kurz, zeilenweise, ein Gedanke pro Absatz.
- **Microcopy am CTA** - was passiert nach dem Klick (nimmt Unsicherheit, z. B. Versandinfo, Guest-Checkout-Hinweis).

## 2 - Advertorial (redaktionelle Pre-Sell-Seite)

Für High-Consideration, Supplements, skeptische Audiences. Redaktioneller Ton, kein Sales-Layout.

| # | Sektion | Job |
| --- | --- | --- |
| 1 | **Headline** | Redaktionell, neugier- oder problemgetrieben, spiegelt den Ad-Hook. Liest sich wie ein Artikel, nicht wie eine Anzeige. |
| 2 | **Story-Einstieg** | Das Problem erlebbar machen, Ich- oder Fall-Perspektive. Die ersten 2-3 Absätze entscheiden, ob gelesen wird. |
| 3 | **Mechanismus / Entdeckung** | Der Aha-Moment: warum bisherige Lösungen scheitern und was hier anders ist. Herzstück des Advertorials. |
| 4 | **Produkt-Reveal** | Das Produkt als logische Konsequenz der Story: erst hier wird es namentlich zentral. Zu früher Reveal zerstört den redaktionellen Frame. |
| 5 | **Proof** | Testimonials, Ergebnisse, Experten-Einordnung, im redaktionellen Ton weitererzählt. |
| 6 | **Offer + CTA** | Überleitung zur LP/PDP oder direkter CTA, plus Risk-Reversal. |

**Pflicht-Hinweise:** Werbekennzeichnung beachten (Advertorial ist Werbung und muss als solche erkennbar sein) und Claims sind hier genauso compliance-pflichtig wie in der Ad → `admkrs-cs-ad-compliance-check` vor Livegang.

## 3 - PDP-Optimierung (warm / Intent)

Die Sektions-Reihenfolge gibt meist das Shop-Template vor, deshalb Hebel-Liste statt Anatomie:
- Gallery above the fold: UGC-/Kontext-Bild ergänzen, nicht nur Freisteller.
- Kern-Benefits als kurze Bullets ÜBER dem Kaufblock (nicht in der ausklappbaren Beschreibung vergraben).
- Reviews mit Fotos prominent und früh erreichbar.
- Versandkosten/Lieferzeit direkt am Preis, nicht erst im Checkout.
- Express-Wallets (Apple Pay, Shop Pay, PayPal Express) am Kaufblock.
- FAQ-Modul für die Top-Einwände ins Template.

---

## Brief-Skelett (schlank, Ausführer-Dokument)

Struktur für den ausgelieferten LP-Brief. Nur Zeilen mit echter Info aufnehmen; was nach Rückfrage offen bleibt, wird weggelassen und intern getrackt.

**Kopf:** Titel (Brand, Produkt, Kampagne) + Stand-Zeile (Datum, Freigabe-Status).

**Auf einen Blick:**
- **Ziel** - 1 Zeile (z. B. Cold-Paid Prospecting, CVR-Fokus).
- **Zielgruppe** - 1 Zeile, konkret (die Person, kein Demografie-Salat).
- **Zur Ad** - Hook-Wortlaut + Ad-Name, den die LP spiegeln muss (Message-Match-Quelle).
- **Seitentyp** - dedizierte LP / Advertorial / PDP, mit 1 Zeile Begründung.
- **Offer** - exakter Wortlaut, Preis, Code (Source of Truth gegen Tippfehler).
- **Assets** - Link zu Brand-Assets, Produktbildern, UGC, Reviews (im Intake aktiv erfragen, häufigster Produktionsblocker).
- **Tech** - Shop/Pagebuilder, Tracking-Anforderungen (Pixel/CAPI-Events auf LP-View, ATC, Purchase).
- **Deadline + Abgabe** - Datum, Lieferort.

**Sektionsplan** (das Herzstück, je Sektion eine Zeile bzw. Tabellenzeile):
- Spalten: **Sektion, Job, Copy (Headline + Kernaussagen, zeilenweise), Visual/Asset.**
- Reihenfolge nach der Anatomie oben (je Seitentyp); Sektionen ohne eigenen Job streichen.
- Gesperrte Claims, Zahlen und Disclaimer im exakten Wortlaut in die Copy-Zelle, nichts erfinden.

**Muss-Elemente (Abnahme-Kriterien):**
- Gesamtkosten-Transparenz: Versand/Steuern früh sichtbar.
- Mobile-Abnahme: Freigabe am Phone, Test im Meta-In-App-Browser.
- CWV-Ziele: LCP ≤2,5 s, INP ≤200 ms, CLS ≤0,1 (Felddaten mobil, siehe SKILL.md Sektion 3 und 7).

---
<sub>**ADMKRS Creative Suite** · © ADMKRS GmbH, München · v1.13.0 · interner Gebrauch · erstellt von ADMKRS. Quellen am jeweiligen Skill-Ende; Specs/Policies an Primärquellen prüfen.</sub>
