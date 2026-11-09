# Website Ann-Kathrin Seidel

**Testseite:** https://annisdl.github.io/website/
**Später:** https://www.ann-kathrin-seidel.de

Dieses Projekt enthält alle Texte und das Gerüst der Website. Bei jeder gespeicherten Änderung baut GitHub die Seite automatisch neu. Nach etwa zwei Minuten ist sie online.

---

## So ändern Sie einen Text

1. Öffnen Sie den Ordner **`content`**.
2. Klicken Sie auf die Datei, die Sie ändern möchten (siehe Übersicht unten).
3. Klicken Sie oben rechts auf das **Stift-Symbol** („Edit this file“).
4. Ändern Sie den Text.
5. Klicken Sie oben rechts auf **„Commit changes …“**. Schreiben Sie im Fenster kurz hinein, was Sie geändert haben (z. B. „Kurstermine Frühjahr“), und bestätigen Sie mit **„Commit changes“**.
6. Nach etwa zwei Minuten ist die Änderung online. Den Fortschritt sehen Sie oben im Reiter **„Actions“**: Ein grüner Haken heißt „fertig“, ein rotes Kreuz heißt „Fehler“ (dann bleibt die alte Version online, es geht nichts kaputt).

## Welche Datei ist welche Seite?

Jede Seite gibt es zweimal: `.de.md` ist Deutsch, `.en.md` ist Englisch.

| Datei | Seite |
|---|---|
| `_index.de.md` / `_index.en.md` | Startseite |
| `beratung.de.md` / `.en.md` | Beratung (PRT) |
| `kurse.de.md` / `.en.md` | Kurse (MBPM) – **hier stehen die Kurstermine** |
| `ueber-mich.de.md` / `.en.md` | Über mich |
| `kontakt.de.md` / `.en.md` | Kontakt |
| `impressum.de.md` / `.en.md` | Impressum |
| `datenschutz.de.md` / `.en.md` | Datenschutz |

## Die Schreibweise (Markdown) – das Wichtigste

| So schreiben Sie … | … so sieht es aus |
|---|---|
| `## Überschrift` | Zwischenüberschrift |
| `**fett**` | **fett** |
| `- Punkt` | Aufzählungspunkt |
| `[Linktext](/kurse)` | Link zu einer eigenen Seite (Dateiname ohne Endung) |
| `[Linktext](https://beispiel.de)` | Link zu einer fremden Seite |
| Leerzeile | neuer Absatz |
| `\` am Zeilenende | Zeilenumbruch ohne neuen Absatz |

Links zu eigenen Seiten schreiben Sie in **beiden Sprachen gleich**, z. B. `[Kurse](/kurse)`. Die Website führt automatisch zur Seite in der richtigen Sprache.

**Der Kopf jeder Datei** (zwischen den beiden `---`-Zeilen) enthält Titel, Menüeintrag und Adresse. Den Titel können Sie ändern, den Rest lassen Sie bitte, wie er ist.

## Bausteine im Text

| Baustein | Wirkung |
|---|---|
| `{{< buchen "beratung" >}}` | Knopf zur Buchung einer Beratung |
| `{{< buchen "kurs" >}}` | Knopf zur Kursbuchung |
| `{{< mail "Betreff" >}}` | E-Mail-Link mit vorausgefülltem Betreff |

Die Buchungslinks und die E-Mail-Adresse selbst stehen zentral in der Datei **`hugo.toml`** unter „IHRE ANGABEN“. Solange ein Buchungslink leer ist, erscheint statt des Knopfes ein Hinweis.

## Kurstermine aktualisieren (alle drei Monate)

In `kurse.de.md` (und `kurse.en.md`) stehen die Termine zwischen den Markierungen

```
<!-- ===== KURSTERMINE: AB HIER ÄNDERN ===== -->
<!-- ===== KURSTERMINE: BIS HIER ÄNDERN ===== -->
```

Kopieren Sie eine Terminzeile, ändern Sie Datum und Angaben, löschen Sie vergangene Termine. Die Markierungen selbst sind auf der Website unsichtbar.

## Eine frühere Fassung wiederherstellen

Jede Datei hat eine Versionsgeschichte: Datei öffnen → oben rechts **„History“**. Dort sehen Sie jede Änderung und können alte Texte herauskopieren.

## Was hier NIE hineingehört

- Passwörter und Zugangsdaten (die liegen in den „Secrets“ unter Settings)
- Kursmaterialien und PDFs für den Downloadbereich
- Daten von Klient/innen oder Kursteilnehmenden

Dieses Projekt ist während der Testphase **öffentlich einsehbar**.
