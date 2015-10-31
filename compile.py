#!/usr/bin/env python

import re
import subprocess
import argparse
import os

def compilefile(filename, bibtex):
    """
    Compiles your tex-file with pdflatex (and bibtex if bibtex=True)
    and writes a nicely formatted error message to the terminal.
    """
    DEVNULL = open(os.devnull, 'wb')
    if bibtex:
        try:
            proc = subprocess.Popen("pdflatex -file-line-error -interaction=nonstopmode %s" % filename, shell=True, stdout=subprocess.PIPE)
            procbib = subprocess.Popen("bibtex %s" % filename[0:-4], shell=True, stdout=DEVNULL)
        except:
            return False
    else:
        try:
            proc = subprocess.Popen("pdflatex -file-line-error -interaction=nonstopmode %s" % filename, shell=True, stdout=subprocess.PIPE)
        except:
            return False

    out, err = proc.communicate()
    out = out.splitlines()

    print " "
    print "------ERROR MESSAGE------"
    counter = 0
    next = False
    for line in out[0:-2]:
        if next:
            print line
            next = False
        else:
            l = re.findall(r'\!\s.+', line)
            if l:
                print previousline
                print l[0]
                next = True
                counter += 1
        previousline = line
    if counter == 0:
        print "Nothing"
        procnew = subprocess.Popen("pdflatex -file-line-error -interaction=nonstopmode %s" % filename, shell=True, stdout=DEVNULL)
    print "-------------------------"
    print " "
    print "-----------LOG-----------"
    print out[-2]
    print out[-1]
    print "-------------------------"
    print " "
    return True

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="the file you want to compile")
    parser.add_argument("-b", "--bibtex", help="choose this option if you are using bibtex", action="store_true")
    args = parser.parse_args()

    filename = args.filename
    bibtex = args.bibtex
    compilefile(filename, bibtex)


