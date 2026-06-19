# Styles-Katalog-Generator

Generiert `docs/styles.html` (animierter Ad-Style-Katalog, 184 Styles, NOVA-Previews in 9:16).

- `styles_data.json` - die 184 Styles (Name, Erkennung, Wofür, Aufbau) je Gruppe. Quelle: `creative-formats.md`.
- `specs.json` - pro Style das Preview-Spec (Archetyp, Animation, Farbwelt, NOVA-Copy).
- `catalog_head.html` / `catalog_foot.html` - Seiten-Gerüst inkl. Preview-CSS und Filter-JS.
- `build_styles_catalog.py` - baut alles zusammen (Pfade im Script anpassen, dann `python3 build_styles_catalog.py`).

Neuer Style: Eintrag in `styles_data.json` + Spec in `specs.json` ergänzen, Script laufen lassen.
