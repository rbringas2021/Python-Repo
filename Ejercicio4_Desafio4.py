print("")
numeros = int(input("Cuantos números quiere introducir: "))
cantidad_numeros = []
suma_numeros = 0
print("")

for i in range(0, numeros):
    cantidad_numeros.append(i)
    suma_numeros += i

print("---------------------------------------------------------------------------------")
print(f"La lectura de números fue la siguiente: {cantidad_numeros}")
print("---------------------------------------------------------------------------------")
print("")
print(f"La suma de todos los números es : {suma_numeros}")
print("")

#__END__.