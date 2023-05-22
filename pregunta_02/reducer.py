#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

maximos = {}

for line in sys.stdin:
    # Obtener la clave y el valor
    tipo_destino, monto = line.strip().split('\t')
    monto = int(monto)

    # Actualizar el máximo para cada tipo de destino
    if tipo_destino in maximos:
        maximos[tipo_destino] = max(maximos[tipo_destino], monto)
    else:
        maximos[tipo_destino] = monto

# Imprimir el resultado final
for tipo_destino, monto_maximo in maximos.items():
    print(f'{tipo_destino}\t{monto_maximo}')
