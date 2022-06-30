# Se requiere recortar un número calculando su límite inferior y superior.

def recortar(num1, num2, num3):
  
    if num1 < num2:
        print(f"\nEl número es menor que el límite inferior, devuelvo límite inferior : {num2}." "\n")
        return num2
    elif num1 > num3:
        print(f"\nEl número es mayor que el límite superior, devuelvo límite superior : {num3}." "\n")
        return num3
    else:
        print(f"\nEl número no supera ningún límite, devuelvo el número sin cambios : {num1}." "\n")
        return num1

recuerda = recortar(15, 0, 10)

print(recuerda)

 #__END__.