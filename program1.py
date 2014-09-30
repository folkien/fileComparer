#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Otwiermy plik o argumencie 1
lines1 = [];
fin = open('file1.txt', 'r')
for line in fin:
    lines1[len(lines1):] = [line];

print lines1
fin.close()

#Otwiermy plik o argumencie 2
lines2 = [];
fin2 = open('file2.txt', 'r')
for line in fin2:
    lines2[len(lines2):] = [line];

print lines2
fin2.close()


#Tylko rozniace sie linijki
for line in lines1:
    if line in lines2 :
        # Usuwamy elementy z kazdej listy
        lines1.pop( lines1.index(line))
        lines2.pop( lines2.index(line))

# Printowanie na ekranie listy numer 1.
print u"Tylko różniące się linijki :"
for line in lines1:
    print line
