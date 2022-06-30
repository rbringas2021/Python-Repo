# Se requiere calcular la relación entre dos números.

def relacion(a, b):
    if a > b:
        return 1
    elif a < b:
        return -1
    elif a == b:
        return 0

print(relacion(5, 10))
print(relacion(10, 5))
print(relacion(5, 5))

#__END__.