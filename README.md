# compile
Compiles your tex-file twice with pdflatex and writes a nicely formatted error message to the terminal.

Usage
-----

```bash
$ ./compile.py --help

usage: compile.py [-h] [-b] filename

positional arguments:
  filename      the file you want to compile

optional arguments:
  -h, --help    show this help message and exit
  -b, --bibtex  choose this option if you are using bibtex

```

Example
-------

```bash
$ ./compile.py master-thesis.tex -b
 
------ERROR MESSAGE------
Nothing
-------------------------
 
-----------LOG-----------
Output written on master-thesis.pdf (65 pages, 1258303 bytes).
Transcript written on master-thesis.log.
-------------------------

```
