#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
##!/usr/bin/env python

import sys

for line in sys.stdin:
    line = line.strip()
    key, _, value = line.split()
    print(f'{key}\t{value}')