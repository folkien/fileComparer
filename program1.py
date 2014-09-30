#Otwiermy plik o argumencie 1
fin_lines = [];
fin = open('file1.txt', 'r')
for line in fin:
    fin_lines[len(fin_lines):] = line;

print fin_lines
fin.close()

#Otwiermy plik o argumencie 2
fin_lines2 = [];
fin2 = open('file2.txt', 'r')
for line in fin2:
    fin_lines2[len(fin_lines2):] = line;

print fin_lines2
fin2.close()

        
