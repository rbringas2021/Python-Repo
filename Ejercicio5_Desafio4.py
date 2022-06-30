n = 0

while n == 0:

    opcion_ingresada = int(input("\nIngrese un número entero del 0 al 9: "))
    if(opcion_ingresada <= 9):
        print("El número elegido es correcto.")
        num = opcion_ingresada
        break
    else:
        print("El número elegido no es correcto!!!.") 

lista = range(10)

for i in lista:
    if(i == num):
        print("El número elegido se encuentra en la lista y vale:", num)
        break

#__END__.