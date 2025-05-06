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

## Lokale Einrichtung mit Conda

Um die Notebooks lokal auszuführen, wird empfohlen, eine dedizierte Conda-Umgebung zu verwenden:

1.  **Conda-Umgebung erstellen** (falls noch nicht geschehen):
    ```bash
    conda create -n wasserbuch python=3.9
    ```
2.  **Umgebung aktivieren**:
    ```bash
    conda activate wasserbuch
    ```
3.  **Abhängigkeiten installieren**:
    Navigieren Sie im Terminal zum Hauptverzeichnis dieses Repositorys (wo sich die `requirements.txt` befindet) und führen Sie aus:
    ```bash
    pip install -r requirements.txt
    ```
4.  **Jupyter starten**:
    Nach der Installation können Sie Jupyter Lab oder Jupyter Notebook starten:
    ```bash
    jupyter lab
    # oder
    jupyter notebook
    ```
    Navigieren Sie dann zum Ordner `Inhalt/Notebooks/`, um die Notebooks zu öffnen und auszuführen.
