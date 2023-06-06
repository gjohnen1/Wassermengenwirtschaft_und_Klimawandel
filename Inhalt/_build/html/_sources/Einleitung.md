# Vorwort

Dieses Juypter-Book besteht aus einer Reihe interaktiver Jupyter-Notebooks zum Thema Wasserwirtschaft und Klimawandel. Es wurde ursprünglich von [Dan Kovacek](https://civil.ubc.ca/faculty/dan-kovacek/) und [Steven Weijs](https://Civil.ubc.ca/faculty/steven-weijs/) an der University of British Columbia erstellt und von [Gregor Johnen](https://www.uni-due.de/wasserbau/mitarbeiter_johnen.php) ins Deutsche übersetzt und angepasst. Ziel dieser Notebooks ist es, Studierenden die systematische Datenanalyse mithilfe der Open-Source-Software *Python* und *Jupyter-Notebook* näherzubringen.

**Von euch als Studierende wird nicht erwartet, dass ihr über Vorkenntnisse in der Programmierung verfügt.** Der Schwerpunkt der Notebooks liegt auf hydrologischen Konzepten und nicht auf der Programmierung selbst, weshalb der erforderliche Code bereitgestellt wird. Jedes Notebook konzentriert sich auf eine bestimmte Komponente der hydrologischen Analyse, und ihr sollt Fragen zu den zugrunde liegenden Konzepten beantworten. Dies erfordert möglicherweise das Ändern von Variablen und das erneute Ausführen von Codeblöcken, um die Ergebnisse im Anschluss zu aktualisieren.

>**Anmerkung**: Der Inhalt dieser Notebooks stellt keine vorgeschriebene bzw. normierte Kombination von Methoden für hydrologische Analysen dar. Vielmehr sollen einige grundlegende Konzepte vorgestellt werden und so zum Nachdenken über Modellunsicherheit und Sensitivität anregen.

## Erste Schritte mit interaktiven Python-Notebooks

Die Jupyter-Notebooks in diesem Kurs können auf die folgenden Arten aufgerufen werden:

* **Auf eurem Computer**: Hier wird der Paket- und Umgebungsmanager [Anaconda](https://www.anaconda.com/) empfohlen. Die Programmierung in Python ist so vielseitig und leistungsstark, weil sie leistungsstarke Funktionen verwendet, die in anwendungsspezifischen Bibliotheken (bspw. pandas) geschrieben sind.  Anaconda ist die Software, die sicherstellt, dass bei der Nutzungen mehrerer solcher Pakete alles reibungslos läuft. Im Fokus steht dabei ein simples Management von Paketen und Entwicklungsumgebungen. Denn dank dieses Tools müsst ihr nicht jedes Paket separat installieren, sondern bei der Installation werden Python, die wichtigsten Pakete und einige der beliebtesten Entwicklungsumgebungen für euch automatisch mitinstalliert. Nach der Installation von Anaconda könnt ihr anschließend [Jupyter Lab](https://jupyter.org/) installieren.
* **In der Cloud**: Die Notebooks können alternativ auch "in der Cloud" mit [Binder](https://mybinder.org/) ausgeführt werden. Ihr könnt hierdurch über euren Webbrowser auf die Notebooks zugreifen. Binder ist hier eine super Möglichkeit, euren Code mit anderen zu teilen und eure Arbeit remote bei voller Funktionalität zu präsentieren. WICHTIG zu beachten ist, dass Dateien, auf die auf diese Weise zugegriffen wird, **nicht in der Cloud-Instanz gespeichert** werden können und dass alle vorgenommenen Änderungen lokal auf eurem Computer gespeichert oder neu geschrieben werden müssen, sobald ihr die Instanz verlasst und später neustartet.

>**Anmerkung**: Anaconda hat kürzlich eine sog. Paywall eingeführt. Dieses Abonemment ist aber grundsätzlich nicht notwendig, um die Software zu nutzen. Da die komplette Anaconda-Distribution mit allen Paketen sehr viel Speicherplatz auf eurem Rechner verbraucht, gibt es außerdem die Variante [Miniconda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/windows.html), die nur Python, Conda sowie ein paar grundlegende Pakete enthält. Diese erfordert demnach auch eine manuelle Installation der in den Jupyter-Notebooks verwendeten Pakete.  Dieser Installationsprozess ist jedoch nicht schwierig und kann wahlweise direkt im Notebook durchgeführt werden. D.h. die Installation von bspw. numpy und pandas wäre einfach eine Sache des Ausführens von `!conda install numpy pandas` in einem Codeblock&mdash; Es reicht die Pakete einmal zu installieren, es sei denn, ihr installiert miniconda neu.

### Einrichtung und Vorbereitung

Eine detaillierte Installationsanleitung findet ihr [hier](https://nbviewer.org/github/ehmatthes/intro_programming/blob/master/notebooks/programming_environment.ipynb). Bitte stellt sicher, dass ihr Python installiert habt (Version Python 3.8 oder höher) und dass ihr Jupyter öffnen und ein Notebook  starten können. Notiz: Die Installation von Geany ist hierfür nicht zwingend erforderlich.

In unserem [Moodle-Kurs](https://moodle.uni-due.de/course/view.php?id=12978) wird ein Diskussionsforum zur Installation eingerichtet.  Wenn ihr nach Durchsicht der hier bereitgestellten Materialien immer noch Schwierigkeiten bei der Installation haben solltet, stellt dort eure Fragen dort so detailliert wie möglich. Wir werden euch dann weiterhelfen.

### Lernressourcen

Es gibt eine große Vielfalt an Programmiersprachen und Paketen innerhalb einer jeweiligen Programmiersprache. Am Anfang kann die Anzahl der neuen Konzepte beim lernen einer Programmiersprace schnell überwältigend sein und es passiert (und fast jedem von uns), dass man sich nicht gut genug fühlt:

![Die gute Nachricht ist, wenn ihr erstmal die erste Hürde überwunden hast, schwindet auch die Angst](img/wave_smash.gif)  
(Quelle: [Gfycat.com](https://gfycat.com/))

Das Internet ist voll von hervorragenden Lernressourcen! Eine Investition in das Erlernen einiger grundlegender Konzepte ist Ihre Zeit wert. Im Folgenden findet Ihr einige Ressourcen, die euch den Einstieg erleichtern:

* [Wie man Code im Notebook ausführt](https://nbviewer.org/github/jupyter/notebook/blob/main/docs/source/examples/Notebook/Running%20Code.ipynb). Grundlagen der Python-Syntax und der Programmierung im Jupyter-Notebook.
* [Matplotlib](http://nbviewer.ipython.org/github/jrjohansson/scientific-python-lectures/blob/master/Lecture-4-Matplotlib.ipynb) ist eine beliebte Bibliothek zur Erstellung einer Vielzahl von Diagrammen. 
* [Einführung in Python](https://nbviewer.org/github/ehmatthes/intro_programming/blob/master/notebooks/index.ipynb).  Ein Einführungskurs, der anhand eines interaktiven Python-Notizbuchs in Jupyter unterrichtet wird.

### Eine umfassende Liste interessanter, nützlicher und leistungsfähiger Jupyter-Notebook-Beispiele findet ihr [hier](https://github.com/jupyter/jupyter/wiki).

## Weitere Informationen

### Paket-Installation

Wenn ihr beim Ausführen einer Code-Zelle in Jupyter die folgende Fehlermeldung erhaltet:

![Example Package Error](img/package_error.png)

Dies bedeutet im Allgemeinen, dass ein Paket nicht installiert wurde.  In diesem Fall handelt es sich um das Paket `Pandas`, das durch Erstellen einer neuen Zelle installiert werden kann:

![Neue Zelle erstellen](img/new_cell.png)

Gebt folgendes ein (Ihr könnt `pandas` natürlich durch den jeweiligen Namen des Pakets ersetzen, das ihr installieren möchtet)

![Befehl zur Installation eines Python-Pakets](img/package_install.png)

Führt die Zelle aus (Umschalttaste + Eingabetaste) (empfohlen), oder drückt die Schaltfläche "Ausführen".

## Lizenz

Die Notizbücher, aus denen dieses Jupyter-Buch besteht, stehen unter der Lizenz [Creative Commons Attribution 4.0 International] (https://creativecommons.org/licenses/by/4.0/legalcode).