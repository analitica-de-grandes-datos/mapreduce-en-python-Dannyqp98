#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#

##!/usr/bin/env python

import sys

current_month = None
month_count = 0

for line in sys.stdin:
    line = line.strip()
    month, count = line.split('\t')

    if current_month == month:
        month_count += int(count)
    else:
        if current_month:
            print(f'{current_month}\t{month_count}')
        current_month = month
        month_count = int(count)

if current_month == month:
    print(f'{current_month}\t{month_count}')
