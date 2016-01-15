# ltx
Compiles your tex-file twice with pdflatex and writes a nicely formatted error message to the terminal. It also runs auxiliary programs like biber automatically.

Usage
-----

Clone the project and save ltx.py to the same folder as your .tex-file.

```bash
$ ./ltx.py --help

usage: ltx.py [-h] [-b] [-bl] filename

positional arguments:
  filename         the file you want to compile

optional arguments:
  -h, --help       show this help message and exit
  -b, --bibtex     choose this option if you are using bibtex
  -bl, --biblatex  choose this option if you are using biblatex
```

If you are not able to run the program by using using the `./`-prefix, try

```bash
$ chmod +x ltx.py
```

Example
-------

```bash
$ ./ltx.py master-thesis.tex -b
 
------ERROR MESSAGE------
Nothing
-------------------------
 
-----------LOG-----------
Output written on master-thesis.pdf (65 pages, 1258303 bytes).
Transcript written on master-thesis.log.
-------------------------

```
