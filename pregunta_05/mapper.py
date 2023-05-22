#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
# #!/usr/bin/env python

import sys

for line in sys.stdin:
    line = line.strip()
    key, date_str, value = line.split()
    year, month, _ = date_str.split('-')
    print(f'{month}\t1')