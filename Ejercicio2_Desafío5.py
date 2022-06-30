# Se requiere calcular el área de un círculo.

import math
PI = float(math.pi)

def area_circulo(radio):
    area = PI * radio ** 2
    return area

area_circulo = area_circulo(5)

print(f'\nEl area del circulo es: {area_circulo}')

#__END__.