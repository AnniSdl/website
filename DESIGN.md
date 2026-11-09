# Design der Website – Übergabe

Dieses Dokument hält alle Design-Entscheidungen fest, die bisher getroffen wurden (Stand: November 2026).
Es ist für alle gedacht, die später an der Website weiterarbeiten – Menschen wie Claude.
Für Claude gibt es zusätzlich den Skill `.claude/skills/website-design/SKILL.md` mit denselben Regeln in Kurzform.

---

## 1 · Grundhaltung

- **Zielgruppe:** Menschen mit chronischen Schmerzen. Die Seite soll ruhig, vertrauenswürdig, gut lesbar und barrierearm sein.
- **Zwischen den Vorbildern:** embracecorazon.com war „zu viel“ (kräftige Farben, Illustrationen), praxis-heringhaus.de „zu wenig Individuelles“. Ziel ist die Mitte: ruhig und aufgeräumt, aber mit eigener Handschrift (Farben, eine runde Ecke, feine Linien, eigene Fotos).
- **Grundlage:** der eigene Design-Prototyp (HTML) und die beiden eigenen Flyer.
- **Anrede:** „du“ (wie Prototyp und Flyer). Impressum und Datenschutz sind davon ausgenommen.

## 2 · Farben

Alle Farben stehen als Variablen oben in `assets/css/main.css`. Kontraste sind nach WCAG AA geprüft.

| Name | Wert | Verwendung |
|---|---|---|
| Waldgrün | `#183f3b` | Knöpfe, Überschriften, Störer „Ein erster Schritt“ |
| Tinte | `#263c34` | Fließtext |
| Text weich | `#3f5148` | Einleitungstexte |
| Moos | `#52645a` | leise Texte, Überzeilen (nur auf hellen Flächen) |
| Leinen | `#f7f4ee` | Grundfläche |
| Papier | `#fffdf8` | helle Schrift auf Grün, Formularfläche |
| Sand | `#eee5d3` | Fläche Kurse (MBPM), Notiz am Startfoto |
| Salbei hell | `#e3e9de` | Fläche Beratung (PRT), Fläche „Häufige Fragen“ |
| Salbei dunkel | `#d7dccb` | Fläche „Schmerz ist real“ |
| Rotton hell | `#e7c9b6` | Fläche „Termine“ (heller Ton aus der Prototyp-Kurskarte) |
| Tiefgrün | `#13302c` | Schrift auf der Termin-Fläche |
| Salbei | `#b6bfae` | **nur** Linien und Formen, nie Text |
| Ton | `#c9957c` | **nur** Linien und Formen (z. B. Farbklecks, Menü-Unterstrich), nie Text |
| Fokus | `#a04729` | Rahmen bei Tastaturbedienung |

**Regel:** Nie zwei kräftige Kästen übereinander. Pro Abschnitt höchstens eine Farbfläche; darin Inhalte mit Linien gliedern statt mit weiteren Kästen.

## 3 · Schriften

- **Sofia Sans** (normale Breite) für Fließtext, 400 und 600.
- **Sofia Sans Semi Condensed** (schmal) für Überschriften, 600.
- Begründung: serifenlos, nicht handgezeichnet, gut lesbar; Überschriften mit enger Laufweite. Fließtext bewusst *nicht* schmal (Lesbarkeit bei Müdigkeit und Schmerzen).
- **Kein** Wechsel zwischen kursiv und gerade in Überschriften.
- Dateien liegen lokal in `static/fonts/` (Lizenz: SIL Open Font License, liegt daneben). Keine Google-Fonts-Links.
- Mindestgrößen: Fließtext 18 px, kleine Texte 16 px, Überzeilen 14 px in Großbuchstaben.

Verworfen: Buchschriften mit Serifen (Newsreader, Cormorant, Fraunces), Flyer-Handschrift (Sue Ellen Francisco) und Poppins.

## 4 · Formen

- **Flächen, Fotos und Felder sind immer nur an EINER Ecke stark gerundet** (`--bogen`, 72 px; auf dem Handy 48 px), alle anderen Ecken nur leicht (`--ecke`, 4 px).
- Die runde Ecke wechselt von Element zu Element: Startfoto oben links, PRT-Karte oben rechts, MBPM-Karte unten rechts, Foto „Schmerz ist real“ unten rechts, Porträt unten links, Kontaktformular oben links.
- Knöpfe: 4 px Rundung rundum (wie im Prototyp), keine Pillenform.
- Schmuck: ein dezenter Farbklecks in Ton oben links auf der Startseite und eine feine Linie in Salbei am Startfoto. Sparsam einsetzen.
- Logo-Zeichen (vorläufig): eine geschwungene Linie mit Ton-Punkt neben dem Namen (Inline-SVG in `layouts/_partials/header.html`).

## 5 · Aufbau der Seiten

**Menü:** Start · Beratung (PRT) · Kurse (MBPM) · Über mich · „English“ · Knopf „Termin buchen“ (Link in `hugo.toml` → `buchung.allgemein`; leer = springt zu den Terminen auf der Startseite). Keine eigene Kontaktseite.

**Startseite** (lange Seite, Texte im Kopf von `content/_index.de.md` / `.en.md`):

| # | Abschnitt | Hintergrund |
|---|---|---|
| 1 | Einstieg: Überzeile, Titel, Text, zwei Knöpfe, Startfoto mit Notiz | Leinen |
| 2 | Die zwei Angebote mit Links zu den Unterseiten | Leinen (Karten Salbei hell / Sand) |
| 3 | „Schmerz ist real“ mit Querformat-Foto (Hände) | Salbei dunkel |
| 4 | Termine: Überschrift nur „Termine“; links Kurse (großes Datum + Zeilen), rechts Einzelberatung; getrennt durch feine Linie, **keine Kästen** | Rotton hell |
| 5 | Störer „Ein erster Schritt darf klein sein.“ | Waldgrün |
| 6 | Über mich (kurz, mit Porträt) | Leinen |
| 7 | Häufige Fragen (aufklappbar, ohne JavaScript) | Salbei hell |
| 8 | Kontaktformular (mailto) | Leinen, Formular auf Papier |

**Unterseiten:** Titel links, Foto rechts (eine runde Ecke oben rechts), darunter Text in einer Spalte (max. 42rem). Erster Absatz als größere Einleitung.

**Kurstermine** stehen nur an einer Stelle: im Kopf von `content/kurse.de.md` / `.en.md` unter `termine:`. Sie erscheinen auf der Kursseite (Baustein `{{< termine >}}`) und auf der Startseite.

## 6 · Fotos

Alle Fotos sind eigene Fotos, liegen in `assets/bilder/` (ohne Kamera-Metadaten gespeichert) und werden von Hugo automatisch als WebP in mehreren Größen ausgeliefert (`layouts/_partials/bild.html`). Jedes Foto braucht einen Alternativtext (`alt:`).

| Datei | Verwendung |
|---|---|
| `barfuss-wiese.jpg` | Startseite, Einstieg |
| `haende-licht.jpg` | Startseite, „Schmerz ist real“ |
| `portraet-himmel.jpg` | Startseite, Über mich |
| `hand-wasser.jpg` | Unterseite Beratung |
| `haende-see.jpg` | Unterseite Kurse |
| `portraet-wiese.jpg` | Unterseite Über mich |
| `hand-graeser.jpg`, `fuesse-bewegung.jpg`, `portraet-graeser.jpg` | Reserve (z. B. Teilnehmerbereich) |

Nicht verwenden: das Foto der meditierenden Frau aus dem Flyer (andere Person, Stockfoto) und das Waldweg-Foto aus dem Prototyp (nicht eigenes Foto).

## 7 · Technische Leitplanken (nicht verhandelbar)

- Kein JavaScript, keine Frameworks, keine externen Ressourcen, keine Cookies, kein Tracking.
- Content-Security-Policy im `<head>` (`layouts/baseof.html`): nur eigene Dateien; Formulare dürfen nur `mailto:` (für das Kontaktformular).
- Deshalb auch **keine `style="…"`-Attribute** im HTML – alles in `assets/css/main.css`.
- Kontaktformular: zwei Felder, `name="subject"` (Auswahl „Worum geht es?“) und `name="body"` (Nachricht), `method="get"`. Die E-Mail-Adresse steht zusätzlich sichtbar darunter.
- Barrierearm: Tastaturbedienung mit sichtbarem Fokusrahmen, Sprunglink, große Klickflächen, nichts scrollt auf dem Handy seitwärts.

## 8 · Rechtliche Leitplanken für Texte

- Keine Heilerlaubnis → Angebote heißen **Beratung**, **Kurs**, **Prävention**, **Begleitung** – nicht Therapie/Behandlung/Heilung.
- Keine Heilversprechen, keine Wirksamkeitszahlen aus Studien, keine Formulierungen wie „hilft nachweislich“ (Heilmittelwerbegesetz).
- Keine Erfahrungsberichte oder Zitate von Klient/innen.
- Hinweis „ersetzt keine ärztliche oder psychotherapeutische Diagnose oder Behandlung“ auf Beratung, Kurse und in den Fragen.
- ME/CFS: nur mit Hinweis auf Pacing und individuelle Grenzen; MBPM/PRT nicht als Heilung anbieten.

## 9 · Arbeitsweise

1. Jede Änderung zuerst als **HTML-Vorschau** zeigen (eine Datei mit eingebetteten Schriften und Bildern, erzeugt mit `werkzeuge/vorschau.py`).
2. Erst nach dem Okay speichern und zu GitHub schicken → die Testseite baut sich automatisch neu.
3. Bei Varianten: 2–4 Möglichkeiten nebeneinander bzw. untereinander zeigen und eine Empfehlung mit Begründung geben.

Vorschau erzeugen (im Projektordner):

```
HUGO_PARAMS_TESTVERSION=true hugo --minify --baseURL http://localhost/website/ -d /tmp/vorschau/website
python3 werkzeuge/vorschau.py /tmp/vorschau/website index.html vorschau-startseite.html /website/
```

## 10 · Offene Punkte

- Logo und Favicon (nächster Schritt)
- pretix-Links in `hugo.toml` eintragen
- Platzhalter: Über mich, Preise und Dauer der Beratung, Gruppengröße, Voraussetzungen Kurs
- Impressum und Datenschutz (Datenschutz: Abschnitt zum Kontaktformular ergänzen – es werden keine Daten über die Website übertragen)
- Passwortgeschützter Downloadbereich (später bei All-inkl.)
