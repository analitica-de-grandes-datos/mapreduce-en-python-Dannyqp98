#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
##!/usr/bin/env python

import sys

previous_key = None
sorted_records = []

for line in sys.stdin:
    line = line.strip()
    record = line.split(',')
    letter=record[0]

    if previous_key and previous_key != letter:
        sorted_records.sort(key=lambda x: str(x[0])+ str(x[1]).zfill(3))
        for sorted_record in sorted_records:
            print(sorted_record[-1])

        sorted_records = []

    sorted_records.append(record)
    previous_key = letter

if previous_key:
    sorted_records.sort(key=lambda x: str(x[0])+ str(x[1]).zfill(3))
    for sorted_record in sorted_records:
        print(sorted_record[-1])
6
