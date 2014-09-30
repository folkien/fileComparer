#!/usr/bin/env python
# -*- coding: utf-8 -*-

# systemowy skrypt python'a
import sys, argparse

# Parsowanie parametrów wejściowych
parser = argparse.ArgumentParser()
parser.add_argument("-i1", "--input1", type=str,  required=True)
parser.add_argument("-i2", "--input2", type=str,  required=True)
args = parser.parse_args()

#Otwiermy plik o argumencie 1
lines1 = [];
fin = open(args.input1, 'r')
i = 0
for line in fin:
    #lines1[len(lines1):] = [str(i) + ':' + line];
    lines1[len(lines1):] = [line];
    i+=1

fin.close()

#Otwiermy plik o argumencie 2
lines2 = [];
fin2 = open(args.input2, 'r')
for line in fin2:
    lines2[len(lines2):] = [line];

fin2.close()


#Tylko rozniace sie linijki
for line in lines1:
    if line in lines2 :
        # Usuwamy elementy z kazdej listy
        lines1.pop( lines1.index(line))
        lines2.pop( lines2.index(line))

# Printowanie na ekranie listy numer 1.
print "Tylko różniące się linijki :"
for line in lines1:
    print line
