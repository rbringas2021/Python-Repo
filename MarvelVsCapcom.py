nombre = input("Cual es tu nombre?: ")
preferencia = input("Cual es tu preferencia (M o C):? ")

nombre = nombre.capitalize()

if nombre[0] <= "M":
    if preferencia == "M" or "C":
        print("Perteneces al Grupo A")
    else:
        print("Perteneces al Grupo B")
else:
    if preferencia == "C":
        print("Perteneces al Grupo A")
    else:
        print("Perteneces al Grupo B")

#__END__.