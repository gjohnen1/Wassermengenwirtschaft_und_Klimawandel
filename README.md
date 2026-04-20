# Wassermengenwirtschaft und Klimawandel

Ein interaktives Jupyter-Book mit hydrologischen Datenanalyse-Notebooks für Studierende im Bereich Wasserwirtschaft und Umweltingenieurwesen.

**Live-Version:** <https://gjohnen1.github.io/Wassermengenwirtschaft_und_Klimawandel/>

## Überblick

Das Buch besteht aus einer Reihe interaktiver Jupyter-Notebooks, die Studierende schrittweise an die systematische Datenanalyse mit *Python* und *Jupyter-Notebooks* heranführen. Der Schwerpunkt liegt auf hydrologischen Konzepten; der benötigte Code wird zum Großteil bereitgestellt. Programmier-Vorkenntnisse werden nicht vorausgesetzt.

Die Notebooks wurden ursprünglich von [Dan Kovacek](https://civil.ubc.ca/faculty/dan-kovacek/) und [Steven Weijs](https://civil.ubc.ca/faculty/steven-weijs/) an der University of British Columbia entwickelt und von [Gregor Johnen](https://www.uni-due.de/wasserbau/mitarbeiter_johnen.php) und [Johanna Schimanski](https://www.uni-due.de/wasserbau/schimanski.php) an der Universität Duisburg-Essen ins Deutsche übersetzt, angepasst und stetig erweitert.

## Zielgruppe dieses README

Dieses README richtet sich an **Lehrende, Fork-Interessierte und Entwickelnde**, die das Buch lokal bauen, auf GitHub Pages veröffentlichen oder den Inhalt anpassen möchten. Studierende finden ihre Einstiegsanleitung im [Vorwort](Inhalt/Einleitung.md) und im ersten Notebook [*Jupyter Notebooks, Python und KI-unterstütztes Programmieren*](Inhalt/Notebooks/Einleitung/Einfuehrung_Datenimport.ipynb).

## Struktur des Buches

Die Gliederung ist in [`Inhalt/_toc.yml`](Inhalt/_toc.yml) definiert:

- **Einleitung** — Einführung in Jupyter, Python und KI-unterstütztes Programmieren
- **Übung 01** — Hydrologische Zeitreihenanalyse
- **Übung 02** — Aufbauende Datenanalyse
- **RTC Blue River** — Real-Time-Control am Beispiel Blue River
- **Hausarbeit** — Abschließendes Projekt

Inhalte liegen unter [`Inhalt/Notebooks/`](Inhalt/Notebooks), Datensätze unter [`Inhalt/Notebook_Daten/`](Inhalt/Notebook_Daten) und [`Inhalt/Projekt_Daten/`](Inhalt/Projekt_Daten).

## Lokale Einrichtung

Empfohlen ist eine dedizierte Conda-Umgebung mit Python 3.10 (Abhängigkeiten werden über `pip` in diese Umgebung installiert):

```bash
conda create -n wbw python=3.10
conda activate wbw
pip install -r requirements.txt
```

Anschließend lässt sich entweder VS Code mit der Jupyter-Extension oder ein klassischer Jupyter-Server starten:

```bash
jupyter lab
# oder
jupyter notebook
```

Die Notebooks befinden sich unter `Inhalt/Notebooks/`.

> **Hinweis:** Der Umgebungsname `wbw` ist mit dem im Vorwort für Studierende konsistent. Wer bereits eine Umgebung `wasserbuch` aus älteren Versionen hat, kann diese weiter nutzen.

## Interaktive Ausführung ohne lokale Installation

Die Notebooks können mit [Binder](https://mybinder.org/) direkt im Browser ausgeführt werden — ohne Installation, aber ohne persistente Speicherung.

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/gjohnen1/Wassermengenwirtschaft_und_Klimawandel/main)

Alternativ lässt sich jedes Notebook in [Google Colab](https://colab.research.google.com/) öffnen, indem es manuell hochgeladen oder per GitHub-Importfunktion eingebunden wird.

## Buch kompilieren und veröffentlichen

Das Buch wird mit [Jupyter Book](https://jupyterbook.org/) aus dem Ordner `Inhalt/` gebaut:

```bash
jupyter-book build Inhalt/
```

Der statische HTML-Export liegt anschließend unter `Inhalt/_build/html/`. Zur Veröffentlichung auf GitHub Pages dient `ghp-import`:

```bash
ghp-import -n -p -f Inhalt/_build/html
```

Weitere Hinweise: [Jupyter-Book-Dokumentation zu GitHub Pages](https://jupyterbook.org/publish/gh-pages.html).

## Mitwirken

Korrekturen, inhaltliche Ergänzungen und Übersetzungen sind willkommen. Pull Requests bitte gegen den `main`-Branch öffnen; bei größeren Änderungen empfiehlt sich vorab ein Issue zur Abstimmung.

## Lizenz

Die Notebooks stehen unter [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/legalcode). Details: siehe [`LICENSE`](LICENSE).
