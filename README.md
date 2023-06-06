## Wassermengenwirtschaft und Klimawandel
Dieses Buch besteht aus einer Reihe von interaktiven Notebooks zum Thema Wasserwirtschaft und Klimawandel. Die Notebooks wurden ursprünglich von Dan Kovacek und Steven Weijs an der University of British Columbia erstellt. Sie sollen Studenten in die Datenanalyse mit der Open-Source-Software Python einzuführen.

## Jupyter Book und Binder

Starten Sie ein jeweiliges Notizbuch im "interaktiven Modus" mit Binder:
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/dankovacek/run_of_river_intro.git/main)

Die Dateien der Notebooks selbst werden unter [Inhalt/notebooks/](https://github.com/dankovacek/Engineering_Hydrology_Notebooks/tree/main/content/notebooks) gespeichert.

## Hinweise zum Kompilieren und Aktualisieren des Buches 

Informationen zum [Erstellen von Büchern und Hosten auf Github Pages](https://jupyterbook.org/publish/gh-pages.html)

Nach dem Aktualisieren von Inhalten, wird das Buch neu kompiliert:

`jupyter-book build content/`

Anschließend muss die GitHub Pages Seite aktualisiert werden. Hierzu kann das gh-pages Branch Update Tool verwendet werden:

`ghp-import -n -p -f content/_build/html`

[Besuchen Sie die Seite](https://gjohnen1.github.io/Wassermengenwirtschaft_und_Klimawandel/) auf Github-Pages

`https://gjohnen1.github.io/Wassermengenwirtschaft_und_Klimawandel/`
