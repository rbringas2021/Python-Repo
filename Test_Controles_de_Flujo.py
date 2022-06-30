nombre = input("Ingrese su nombre:  ")

if len(nombre) > 5:
    print("su nombre es muy largo")
    print("Seguro te dicen con algún diminutivo")

if nombre[0] == 'A':
    print('Tu nombre empieza con A')

if (nombre == nombre.capitalize()):    #Pasa la primera a mayúscula.
    print('Su nombre está bien escrito:', nombre)

print("Fin de la ejecución")
