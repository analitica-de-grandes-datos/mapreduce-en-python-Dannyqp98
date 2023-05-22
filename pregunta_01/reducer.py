#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

current_column = None
count = 0

for line in sys.stdin:
    # Obtener la clave y el valor
    column, value = line.strip().split('\t')

    # Si la clave cambia, imprimir el resultado parcial
    if current_column is not None and current_column != column:
        print(f'{current_column}\t{count}')
        count = 0

    # Actualizar la clave actual y el recuento
    current_column = column
    count += int(value)

# Imprimir el resultado final
if current_column is not None:
    print(f'{current_column}\t{count}')
