#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
##!/usr/bin/env python
import sys

k = 6
min_values = []

for line in sys.stdin:
    line = line.strip()
    _, _, value  = line.split('\t')
    value = float(value)
    
    if len(min_values) < k:
        min_values.append([line, value])
    else:
        min_values.sort(key=lambda x: x[1])
        if value < min_values[-1][1]:
            min_values[-1] = [line, value]

min_values.sort(key=lambda x: x[1])

for record in min_values:
    print(record[0])
