print("")
print("********************************************************************************")
print("")
numero = int(input("Ingrese un número impar límite: "))
numeros_impares = []
suma_num_impares = 0
print("")

for i in range(0, numero + 1):
    if(i % 2 == 1):
        numeros_impares.append(i)
        suma_num_impares += i

print("---------------------------------------------------------------------------------")
print(f"Los números impares contenidos en el número límite ({numero}) son: {numeros_impares}")
print("---------------------------------------------------------------------------------")
print("")
print(f"La suma de todos los números impares es : {suma_num_impares}")
print("")
print("********************************************************************************")

#__END__.