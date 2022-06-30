
print("##################################################################")
print("#                                                                #")
print("#                Desafío entregable 3 (Clase 5)                  #")
print("#                     \"Control de Flujo\"                         #")
print("##################################################################")
print("#                                                                #")
print("#  1. Mostrar una suma de los dos números.                       #")
print("#  2. Mostrar una resta de los dos números (el 1ro - el 2do).    #")
print("#  3. Mostrar una multiplicación de los dos números.             #")
print("#  4. Si elige esta opción se interrumpirá la impresión del menú #")
print("#     y el programa finalizará.                                  #")
print("#                                                                #")
print("##################################################################")

opcion_ingresada = int(input("Ingrese una opción: "))

while opcion_ingresada <= 4:
    if(opcion_ingresada == 1):
        numero1 = int((input("Ingrese 1er número: ")))

        if(isinstance(numero1, int)):
            numero2 = (int(input("Ingrese 2do número: ")))

            if(isinstance(numero2, int)):
                suma = int(numero1) + int(numero2)

                print("La suma de ambos números es: " + str(suma))
                break
            else:
                print("*** Debe ingresar un número ***")
                continue
        else:
            print("*** Debe ingresar un número ***")
            continue

    elif(opcion_ingresada == 2):
        numero1 = int((input("Ingrese 1er número: ")))

        if(isinstance(numero1, int)):
            numero2 = (int(input("Ingrese 2do número: ")))

            if(isinstance(numero2, int)):
                resta = int(numero1) - int(numero2)

                print("La resta de ambos números es: " + str(resta))
                break
            else:
                print("*** Debe ingresar un número ***")
                continue
        else:
            print("*** Debe ingresar un número ***")
            continue
    elif(opcion_ingresada == 3):
        numero1 = int((input("Ingrese 1er número: ")))

        if(isinstance(numero1, int)):
            numero2 = (int(input("Ingrese 2do número: ")))

            if(isinstance(numero2, int)):
                multiplicacion = int(numero1) * int(numero2)

                print("La multiplicacion de ambos números es: " + str(multiplicacion))
                break
            else:
                print("*** Debe ingresar un número ***")
                continue
        else:
            print("*** Debe ingresar un número ***")
            continue
    elif(opcion_ingresada == 4):
        break

else:
    print("*** La opción no es válida ***")
