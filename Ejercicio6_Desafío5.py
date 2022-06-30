# Se requiere armar una función que devuelva dos listas ordenables con los números pares y los impares.

def separar(lista):
    
    lista_pares = []
    lista_impares = []

    for i in lista:
        if i % 2 == 0:
            lista_pares.append(i)
        else:
            lista_impares.append(i)
            
    lista_pares.sort()
    lista_impares.sort()
    return lista_pares, lista_impares

lista = [6,5,2,1,7]
pares, impares = separar(lista)
print("Pares", pares)
print("Impares", impares)

#__END__.