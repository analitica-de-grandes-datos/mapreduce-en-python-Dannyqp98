#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#

#### !/usr/bin/env python

import sys

for line in sys.stdin:
    line = line.strip()
    value, key = line.split(',')
    print(f'{key},{value}')
