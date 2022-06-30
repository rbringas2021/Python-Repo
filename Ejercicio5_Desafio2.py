##############################################################
# Calculo de Matriz agregando cuarto elemento como sumatoria #
#                   de los primeros tres.                    #
##############################################################

# Imprimo la matriz de Partida.

a = [1, 5, 1]
b = [2, 1, 2]
c = [3, 0, 1]
d = [1, 4, 4]

# Imprimo la matriz de Partida.

print("Matriz de partida :")
print("")
print("matriz = [")

print("  ",(a))
print("  ",(b))
print("  ",(c))
print("  ",(d))
print("]")

# Obtengo la suma de todos los elementos de cada lista.

a1 = sum(a)
b1 = sum(b)
c1 = sum(c)
d1 = sum(d)

# Agrego el resultado para dar forma a la matriz final.

a.append(a1)
b.append(b1)
c.append(c1)
d.append(d1)

# Imprimo el resultado de la matriz Final.

print("")
print("Matriz Final :")
print("")
print("matriz = [")
print("  ",(a))
print("  ",(b))
print("  ",(c))
print("  ",(d))
print("]")

#__END__.