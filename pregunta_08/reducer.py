#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
##!/usr/bin/env python

import sys

current_key = None
sum_value = 0
count = 0

for line in sys.stdin:
    line = line.strip()
    key, value = line.split('\t')

    if current_key == key:
        sum_value += float(value)
        count += 1
    else:
        if current_key:
            average = sum_value / count
            print(f'{current_key}\t{sum_value}\t{average}')
        current_key = key
        sum_value = float(value)
        count = 1

if current_key:
    average = sum_value / count
    print(f'{current_key}\t{sum_value}\t{average}')
