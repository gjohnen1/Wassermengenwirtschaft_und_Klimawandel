## Wassermengenwirtschaft und Klimawandel
Dieses Buch besteht aus einer Reihe von interaktiven Notebooks zum Thema Wassermengenwirtschaft und Klimawandel. Die Notebooks wurden ursprünglich von Dan Kovacek und Steven Weijs an der University of British Columbia erstellt und von Gregor Johnen ins Deutsche übersetzt und angepasst. Sie sollen Studenten in die Datenanalyse mit der Open-Source-Software Python einzuführen.

## Jupyter Book und Binder

Jedes der enthaltenen Notebooks kann im "interaktiven Modus" mit Binder gestartet werden:
[![Binder](https://mybinder.org/badge_logo.svg)

Die Dateien der Notebooks selbst werden unter [Inhalt/notebooks/](https://github.com/gjohnen1/Wassermengenwirtschaft_und_Klimawandel/tree/main/Inhalt/Notebooks) gespeichert.

## Hinweise zum Kompilieren und Aktualisieren des Buches 

Informationen zum [Erstellen von Büchern und Hosten auf Github Pages](https://jupyterbook.org/publish/gh-pages.html)

Nach dem Aktualisieren von Inhalten, wird das Buch neu kompiliert:

`jupyter-book build Inhalt/`

Anschließend muss die GitHub Pages Seite aktualisiert werden. Hierzu kann das gh-pages Branch Update Tool verwendet werden:

`ghp-import -n -p -f Inhalt/_build/html`

[Besuchen Sie die Seite](https://gjohnen1.github.io/Wassermengenwirtschaft_und_Klimawandel/) auf Github-Pages

`https://gjohnen1.github.io/Wassermengenwirtschaft_und_Klimawandel/`
