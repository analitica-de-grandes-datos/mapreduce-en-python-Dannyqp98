#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#

### !/usr/bin/env python

import sys
for line in sys.stdin:
    line = line.strip()
    list_line=line.split(',')
    if len(list_line)>1:
        key,value = list_line
        print(f'{value},{key}')

