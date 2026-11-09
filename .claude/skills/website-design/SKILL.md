---
name: website-design
description: Design- und Arbeitsregeln für die Website von Ann-Kathrin Seidel (Hugo, PRT-Beratung und MBPM-Kurse). Vor jeder Änderung an Layouts, CSS, Fotos oder Seitentexten laden.
---

# Website Ann-Kathrin Seidel – Design-Regeln

Ausführlich mit Begründungen: `DESIGN.md` im Projektordner. Diese Datei ist die Kurzfassung zum Arbeiten.

## Für wen ich arbeite
Die Auftraggeberinnen sind Geisteswissenschaftlerinnen ohne HTML-Kenntnisse, arbeiten am Mac. Immer auf Deutsch, verständlich, Schritt für Schritt erklären. Keine Fachbegriffe ohne Erklärung.

## Arbeitsablauf (verbindlich)
1. Änderung im Projekt vornehmen, NICHT committen.
2. Seite bauen und mit `werkzeuge/vorschau.py` eine eigenständige HTML-Vorschau erzeugen; per Datei an die Nutzerin schicken (Anzeige „render“). Selbst vorher per Playwright prüfen: Schriften geladen, `scrollWidth` bei 390 px = 390, Screenshot ansehen.
3. Erst nach ausdrücklichem Okay committen und auf `main` pushen (Testseite baut automatisch, Hugo 0.169.0).
4. Bei Gestaltungsfragen 2–4 Varianten nebeneinander zeigen und eine begründete Empfehlung geben.

Bauen: `HUGO_PARAMS_TESTVERSION=true hugo --minify --gc --baseURL http://localhost:8765/website/ -d <ziel>/website`
Vorschau: `python3 werkzeuge/vorschau.py <ziel>/website <seite>/index.html <ausgabe>.html /website/`

## Feste Gestaltung
- Farben nur über die Variablen in `assets/css/main.css` (`:root`). Ton `#c9957c` und Salbei `#b6bfae` nie für Text. Jede neue Text-/Hintergrund-Kombination auf WCAG-AA-Kontrast prüfen (≥ 4,5:1).
- Schriften: Sofia Sans (Text, 400/600) und Sofia Sans Semi Condensed (Überschriften, 600), lokal in `static/fonts/`. Keine Kursiv-Wechsel in Überschriften, keine Serifen, keine Handschrift.
- Größen: Fließtext 1.125rem, nichts unter 0.875rem.
- Ecken: Flächen, Fotos, Felder immer nur an EINER Ecke stark gerundet (`var(--bogen)`), sonst `var(--ecke)` (4 px). Die runde Ecke wechselt zwischen benachbarten Elementen. Knöpfe 4 px rundum.
- Pro Abschnitt höchstens eine Farbfläche; innen mit Linien gliedern, keine Kästen in Kästen.
- Startseite, Reihenfolge und Hintergründe: Einstieg (Leinen) → Angebote (Leinen, Karten Salbei hell/Sand) → „Schmerz ist real“ mit Foto (Salbei dunkel) → Termine (Rotton hell `#e7c9b6`, Schrift Tiefgrün `#13302c`, zwei Spalten mit Linie) → Störer (Waldgrün) → Über mich (Leinen) → Fragen (Salbei hell) → Kontaktformular (Leinen).
- Anrede „du“.

## Technik – nicht verletzen
- Kein JavaScript, keine externen Ressourcen, keine Cookies/Tracking.
- CSP in `layouts/baseof.html`: `default-src 'none'; style-src 'self'; img-src 'self'; font-src 'self'; base-uri 'self'; form-action mailto:` → keine `style="…"`-Attribute, keine Inline-Skripte, keine eingebetteten Videos/Karten.
- Fotos nur über `partial "bild.html"` (WebP, mehrere Größen), immer mit `alt`. Neue Fotos vor dem Einchecken ohne Metadaten speichern (Repo ist öffentlich).
- Texte, die die Nutzerin pflegt, gehören in den Kopf (Front Matter) der Markdown-Dateien, mit deutschen Kommentaren. Kurstermine nur in `content/kurse.*.md` unter `termine:`.
- Bei Änderungen der Pflege-Abläufe `README.md` mit anpassen.

## Texte – rechtliche Grenzen (Heilmittelwerbegesetz, keine Heilerlaubnis)
- Begriffe: Beratung, Kurs, Prävention, Begleitung – nicht Therapie, Behandlung, Heilung für das eigene Angebot.
- Keine Heilversprechen, keine Studienergebnisse/Prozentzahlen als Werbung, keine Klient/innen-Erfahrungsberichte.
- Hinweis „ersetzt keine ärztliche oder psychotherapeutische Diagnose oder Behandlung“ beibehalten.
- Keine Fakten erfinden (Preise, Dauer, Gruppengröße): stattdessen `[PLATZHALTER: …]`.
