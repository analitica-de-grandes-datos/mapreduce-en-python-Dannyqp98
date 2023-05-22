#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#


import sys

for line in sys.stdin:
    line = line.strip()
    key, values = line.split('\t')
    letters = values.split(',')
    
    for letter in letters:
        print(f"{letter}\t{key}")
