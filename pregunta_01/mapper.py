#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

for line in sys.stdin:
    # Eliminar espacios en blanco y separar por comas
    line = line.strip()
    values = line.split(',')

    if len(values)>2: 
        # Obtener el valor de la tercera columna
        column = values[2].strip()

        # Convertir a mayúsculas
        column = column.lower()

        # Emitir clave-valor para el recuento
        print(f'{column}\t1')