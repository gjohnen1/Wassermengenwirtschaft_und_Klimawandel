# Vorwort

Dieses Jupyter-Book besteht aus einer Reihe interaktiver Jupyter-Notebooks zum Thema Wassermengenwirtschaft und Klimawandel. Es wurde ursprünglich von [Dan Kovacek](https://civil.ubc.ca/faculty/dan-kovacek/) und [Steven Weijs](https://civil.ubc.ca/faculty/steven-weijs/) an der University of British Columbia erstellt und von [Gregor Johnen](https://www.uni-due.de/wasserbau/mitarbeiter_johnen.php) und [Johanna Schimanski](https://www.uni-due.de/wasserbau/schimanski.php) ins Deutsche übersetzt, angepasst und stetig erweitert. Ziel der einzelnen Notebooks ist es, Studierenden die systematische Datenanalyse mithilfe der Open-Source-Software *Python* und *Jupyter-Notebooks* näherzubringen.

**Es wird nicht erwartet, dass Teilnehmende über Vorkenntnisse der Programmierung verfügen.** Der Schwerpunkt der Notebooks liegt auf hydrologischen Konzepten und nicht auf der Programmierung selbst, weshalb der erforderliche Code zum Großteil bereitgestellt wird. Jedes Notebook konzentriert sich auf eine bestimmte Komponente der hydrologischen Datenanalyse und -auswertung. Anschließend sollten Fragen zu den zugrunde liegenden Konzepten beantwortet werden. Dies erfordert möglicherweise das Ändern von Variablen und das erneute Ausführen von Codeblöcken, um die Ergebnisse im Anschluss zu aktualisieren.

> **Anmerkung:** Der Inhalt dieser Notebooks stellt keine vorgeschriebene bzw. normierte Kombination von Methoden für hydrologische Analysen dar. Vielmehr sollen einige grundlegende Konzepte aus dem Bereich Wassermengenwirtschaft und Klimawandelanalyse vorgestellt werden und so zum Nachdenken über Modellunsicherheiten und Sensitivitäten anregen.

## Was dieses Vorwort leistet – und was nicht

Dieses Vorwort ist die **Vorbereitung vor dem Kurs**: Ihr richtet Eure Arbeitsumgebung ein, aktiviert Euren KI-Zugang und lernt den Aufbau des Buchs kennen. Die eigentliche Einführung in Jupyter-Zellen, Python-Grundlagen und den Umgang mit KI-Assistenten findet Ihr im ersten Notebook [*Jupyter Notebooks, Python und KI-unterstütztes Programmieren*](Notebooks/Einleitung/Einfuehrung_Datenimport.ipynb). Das Notebook ist auf einen Tagesblock (2 × 1,5 h) angelegt.

Plant ca. **30 Minuten** für die hier beschriebenen Vorbereitungen ein — idealerweise vor dem ersten Termin.

## Schritt 1: Eure Arbeitsumgebung

Ihr habt drei Wege, die Notebooks auszuführen. Wir empfehlen klar Option A.

### Option A: Lokale Installation mit Anaconda + VS Code (empfohlen)

Dieser Weg ist auf Dauer der stabilste und erlaubt Euch die Nutzung von GitHub Copilot (siehe Schritt 2).

**1. Anaconda installieren.** Anaconda ist ein Paket- und Umgebungsmanager, der Python und viele wissenschaftliche Bibliotheken (u.a. `pandas`, `numpy`, `matplotlib`) in einem Schritt installiert. Ladet die [Anaconda Distribution](https://www.anaconda.com/download/success) herunter und folgt dem Installationsassistenten.

> **Anmerkung:** Anaconda hat vor einiger Zeit eine Paywall für kommerzielle Nutzung eingeführt. Für akademische Zwecke ist kein Abonnement nötig. Wer Anaconda bewusst vermeiden möchte, kann alternativ [Miniforge](https://github.com/conda-forge/miniforge) oder [Miniconda](https://www.anaconda.com/docs/getting-started/miniconda/main) mit `conda-forge` als Default-Kanal verwenden — das Ergebnis ist gleichwertig.

**2. Umgebung und Pakete einrichten.** Klont oder ladet dieses Repository herunter und installiert die benötigten Pakete in einer eigenen Conda-Umgebung. In der Anaconda Prompt (Windows) bzw. im Terminal (macOS/Linux) im Projektverzeichnis:

```bash
conda create -n wbw python=3.10
conda activate wbw
pip install -r requirements.txt
```

**3. VS Code installieren und einrichten.** Installiert [Visual Studio Code](https://code.visualstudio.com/) und darin die Extensions *Python*, *Jupyter* und *GitHub Copilot* (+ optional *GitHub Copilot Chat*). VS Code ist Eure **empfohlene Arbeitsumgebung**, weil Copilot dort nativ integriert ist und Ihr Code und Terminal parallel bedienen könnt.

**4. Installation prüfen.** In der aktivierten Umgebung:

```bash
python --version
conda --version
jupyter --version
```

Es sollten Versionsnummern angezeigt werden (Python ≥ 3.10).

**5. Kurs öffnen.** In VS Code: `Datei → Ordner öffnen` → Projektverzeichnis wählen → das Einführungsnotebook unter `Inhalt/Notebooks/Einleitung/Einfuehrung_Datenimport.ipynb` doppelklicken. Beim ersten Öffnen fragt VS Code nach einem Kernel — wählt die eben angelegte Umgebung `wbw`.

> **Alternative zu VS Code:** Wer lieber im Browser arbeitet, kann nach `conda activate wbw` im Projektverzeichnis `jupyter notebook` eingeben. Damit öffnet sich das klassische Jupyter-Interface. Copilot-Inline-Vorschläge funktionieren dort allerdings nicht nativ.

### Option B: Google Colab

[Google Colab](https://colab.research.google.com/) führt Jupyter-Notebooks im Browser aus. Ihr braucht nur einen Google-Account. Vorteile: keine Installation, optional GPU-Zugriff. Nachteile: Ihr müsst die `.ipynb`-Dateien manuell hochladen oder von GitHub öffnen, und Copilot ist dort nicht verfügbar — Google bietet mit „Gemini in Colab" ein eigenes LLM an.

### Option C: Binder (ohne lokale Installation)

Die Notebooks können „in der Cloud" mit [Binder](https://mybinder.org/) ausgeführt werden. Binder richtet die Umgebung automatisch anhand der Repository-Dateien ein. Keine lokale Installation, kein Account.

> **WICHTIG:** In Binder werden **Änderungen nicht dauerhaft gespeichert**. Wenn Ihr den Browser-Tab schließt, ist Eure Arbeit weg. Ladet wichtige Notebooks regelmäßig lokal herunter. Copilot ist in Binder nicht verfügbar.

## Schritt 2: GitHub Copilot aktivieren

In diesem Kurs arbeitet Ihr explizit mit einem KI-Assistenten. Unser Default ist **GitHub Copilot**, weil er über das kostenlose Studierendenprogramm von GitHub zugänglich ist und sich nahtlos in VS Code integriert.

1. Meldet Euch mit Eurer Uni-E-Mail-Adresse für das [GitHub Student Developer Pack](https://github.com/education/students) an. Darin ist **GitHub Copilot Pro** kostenlos enthalten, solange Ihr eingeschrieben seid. Die Freischaltung kann 1–2 Tage dauern — plant das ein.
2. Installiert in VS Code die Extensions *GitHub Copilot* und *GitHub Copilot Chat*.
3. Meldet Euch in VS Code mit Eurem GitHub-Account an: `Strg+Umschalt+P` → `GitHub: Sign in`.
4. Prüft die Freischaltung: in einer Codezelle einen Kommentar schreiben (z.B. `# Wasserstand aus CSV einlesen`) und ein paar Zeilen Platz lassen — nach kurzer Zeit sollten graue Vorschläge erscheinen.

> **Hinweis:** Wenn Ihr bereits mit einem anderen Chat-LLM vertraut seid (Claude, ChatGPT, Gemini), könnt Ihr diesen ergänzend nutzen. Der Workflow — Prompt → Vorschlag → Prüfung — ist in allen Werkzeugen derselbe und wird im Einführungsnotebook in Block D ausführlich behandelt.

## Schritt 3: Das Buch navigieren

Das Jupyter-Book ist in Kapitel und Abschnitte gegliedert, die in `_toc.yml` definiert sind. Wenn Ihr das Buch online betrachtet oder lokal baut (siehe `README.md`), erscheint am linken Rand eine Navigationsleiste.

### Projektstruktur

Für Eure Arbeit sind diese Ordner relevant:

- `Inhalt/Notebooks/` — die interaktiven Notebooks (`Einleitung/`, `Uebung_X/`, `Hausarbeit/`).
- `Inhalt/Notebook_Daten/` — Datensätze für Übungen und Hausarbeit.
- `Inhalt/Projekt_Daten/` — zusätzliche Datensätze, die in einzelnen Notebooks verwendet werden.

## Wenn es hakt

**Bei Installationsproblemen:** Im [Moodle-Kurs](https://lehre.moodle.uni-due.de/course/view.php?id=5089) gibt es ein Diskussionsforum zur Installation. Beschreibt Euer Problem möglichst genau (Betriebssystem, Fehlermeldung im Wortlaut, was Ihr bereits probiert habt). Screenshots helfen.

**Bei Fragen zu Code oder Notebook-Bedienung:** Diese Themen behandelt das [Einführungsnotebook](Notebooks/Einleitung/Einfuehrung_Datenimport.ipynb) ausführlich. Dort findet Ihr u.a. wie Ihr Zellen ausführt, was ein Kernel ist, wie Ihr Fehlermeldungen lest und wie Ihr Copilot bzw. ein Chat-LLM einsetzt, um Probleme zu lösen.

## Lernressourcen

Am Anfang kann die Vielzahl neuer Konzepte beim Erlernen einer Programmiersprache überwältigend wirken — fast jeder kennt dieses Gefühl:

![Die gute Nachricht ist, wenn diese erste Hürde überwunden ist, schwindet auch die Angst](img/wave_smash.gif)
(Quelle: [Gfycat.com](https://gfycat.com/))

Das Internet ist voll von hervorragenden Lernressourcen. Ein paar Empfehlungen:

- [Wie führt man Code in einem Notebook aus](https://nbviewer.org/github/jupyter/notebook/blob/main/docs/source/examples/Notebook/Running%20Code.ipynb) — Grundlagen der Jupyter-Bedienung.
- [Matplotlib](http://nbviewer.ipython.org/github/jrjohansson/scientific-python-lectures/blob/master/Lecture-4-Matplotlib.ipynb) — Einstieg in die meistgenutzte Plot-Bibliothek.
- [Einführung in Python](https://nbviewer.org/github/ehmatthes/intro_programming/blob/master/notebooks/index.ipynb) — kompletter Einführungskurs als Notebook.
- [Markdown-Grundlagen](markdown.md) — für die Formatierung der Textzellen in Euren eigenen Notebooks.
- Eine umfassende Liste empfehlenswerter Jupyter-Beispiele findet Ihr im [Jupyter-Wiki](https://github.com/jupyter/jupyter/wiki).

## Lizenz

Die Notebooks, aus denen dieses Jupyter-Book besteht, stehen unter der Lizenz [Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/legalcode).
