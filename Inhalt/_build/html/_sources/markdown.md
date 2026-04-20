# Markdown-Grundlagen (MyST)

Ob Ihr Inhalte in Jupyter Notebooks (`.ipynb`) oder in regulären Markdown-Dateien (`.md`) schreibt — gemeinsam ist die *MyST*-Variante von Markdown ("Markedly Structured Text"), eine kleine Erweiterung von [CommonMark](https://commonmark.org/) für die Sphinx-/Jupyter-Book-Welt.

Diese Seite ist eine Mini-Referenz mit den Bausteinen, die Ihr in Übungen, Hausarbeit und eigenen Notizen am häufigsten braucht.

## Rollen und Direktiven

Die zwei zentralen Werkzeuge in MyST sind **Rollen** (eine Zeile) und **Direktiven** (mehrere Zeilen). Beide sind benannte „Funktionen", deren Verhalten vom Namen abhängt.

### Direktiven (mehrzeilig)

Allgemeine Form:

````
```{name}
Inhalt der Direktive
```
````

Konkretes Beispiel — eine Hinweis-Box:

````
```{note}
Hier steht ein Hinweis.
```
````

Ergebnis:

```{note}
Hier steht ein Hinweis.
```

Weitere häufig nützliche Direktiven: `warning`, `tip`, `important`, `seealso`, `figure`, `table`, `code-block`, `math`. Eine vollständige Liste findet Ihr in der [MyST-Dokumentation](https://myst-parser.readthedocs.io/en/latest/syntax/roles-and-directives.html).

### Rollen (einzeilig)

Allgemeine Form:

```
Hier ein Beispieltext mit {rollenname}`Inhalt der Rolle`.
```

Beispiel — die `doc`-Rolle erzeugt einen Querverweis auf eine andere Seite des Buches:

```
Siehe auch: {doc}`Notebooks/Einleitung/Einfuehrung_Datenimport`
```

Weitere häufige Rollen: `kbd` (Tastatur-Shortcut), `code`, `math`, `download`, `term`.

## Mathematik

Inline-Mathematik mit einfachen Dollarzeichen, abgesetzte Formeln mit doppelten:

```
Inline: $E = mc^2$

Block:
$$
F(x) = \int_{-\infty}^{x} f(t)\,dt
$$
```

Inline: $E = mc^2$

Block:

$$
F(x) = \int_{-\infty}^{x} f(t)\,dt
$$

## Codeblöcke mit Syntaxhervorhebung

````
```python
def manning_v(R, S, n):
    return R**(2/3) * S**0.5 / n
```
````

```python
def manning_v(R, S, n):
    return R**(2/3) * S**0.5 / n
```

## Tabellen

```
| Variable | Einheit  | Beschreibung |
|---|---|---|
| Q  | m³/s    | Abfluss |
| A  | km²     | Einzugsgebiet |
| n  | s/m^(1/3) | Rauhigkeit |
```

| Variable | Einheit  | Beschreibung |
|---|---|---|
| Q  | m³/s    | Abfluss |
| A  | km²     | Einzugsgebiet |
| n  | s/m^(1/3) | Rauhigkeit |

## Bilder

```
![Beschreibung](relativer/Pfad/bild.png)
```

oder als Direktive mit Optionen:

````
```{figure} relativer/Pfad/bild.png
:width: 400px
:align: center

Bildunterschrift mit *Markdown*-Formatierung.
```
````

## Code in Markdown-Dateien ausführen

Mit MyST-NB lassen sich Codezellen direkt in `.md`-Dateien ausführen — vorausgesetzt die Datei trägt Jupytext-Metadaten. Setup einmalig:

```
jupyter-book myst init markdown.md
```

Danach lassen sich `{code-cell}`-Direktiven nutzen:

````
```{code-cell}
print("Hier wird Code beim Buch-Build ausgeführt")
```
````

Beim Bauen werden diese Zellen mit dem konfigurierten Jupyter-Kernel ausgeführt; Ausgaben erscheinen direkt in der gerenderten Seite.

## Weiterführend

* [MyST Markdown — Syntax-Referenz](https://myst-parser.readthedocs.io/en/latest/syntax/syntax.html)
* [Jupyter Book — Inhaltskonzepte](https://jupyterbook.org/en/stable/content/index.html)
* [MyST-NB — Code in Markdown ausführen](https://myst-nb.readthedocs.io/)
