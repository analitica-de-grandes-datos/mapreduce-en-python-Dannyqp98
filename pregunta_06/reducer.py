#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
##!/usr/bin/env python

import sys

current_key = None
min_value = None
max_value = None

for line in sys.stdin:
    line = line.strip()
    key, value = line.split('\t')

    if current_key == key:
        min_value = min(min_value, value)
        max_value = max(max_value, value)
    else:
        if current_key:
            print(f'{current_key}\t{max_value}\t{min_value}')
        current_key = key
        min_value = value
        max_value = value

if current_key:
    print(f'{current_key}\t{max_value}\t{min_value}')
