#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
##!/usr/bin/env python

import sys

for line in sys.stdin:
    line = line.strip()
    key, date, value = line.split()
    print(f'{key}\t{date}\t{value}')
