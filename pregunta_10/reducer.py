#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#

##!/usr/bin/env python

import sys

current_letter = None
keys = []

for line in sys.stdin:
    letter,key = line.strip().split('\t')
    
    if current_letter is None:
        current_letter = letter
    
    if letter != current_letter:
        print(f"{current_letter}\t{','.join(map(str,keys))}")
        current_letter = letter
        keys = []
    
    keys.append(int(key))
    keys.sort()
    

if current_letter is not None:
    keys.sort()
    print(f"{current_letter}\t{','.join(map(str,keys))}")
        