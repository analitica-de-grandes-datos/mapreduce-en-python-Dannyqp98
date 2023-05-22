#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys
header = sys.stdin.readline()
for line in sys.stdin:
    # Eliminar espacios en blanco y separar por comas
    line = line.strip()
    values = line.split(',')

    if len(values)>4:

      # Obtener los valores de las columnas 4 y 5
      tipo_destino = values[3].strip()
      monto = (values[4].strip())

      # Emitir clave-valor para el máximo
      print(f'{tipo_destino}\t{monto}')
