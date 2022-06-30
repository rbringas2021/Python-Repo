
##################################################################
# Calcular nota final en base al ejercico número 3 del desafio 2 #
##################################################################
print("")
NOTA1 = input("Ingrese (Nota 1) : ")
print("-------------------------------------------------------")
print("Aclaración: Nota 1 equivalente al 15% de la nota final.")
print("-------------------------------------------------------")
print("")

PNOTA1 = float(NOTA1) * 15/100

print("\tSu nota parcial es : " + str(PNOTA1))
print("")
NOTA2 = input("Ingrese (Nota 2) : ")
print("-------------------------------------------------------")
print("Aclaración: Nota 2 equivalente al 35% de la nota final.")
print("-------------------------------------------------------")
print("")

PNOTA2 = float(NOTA2) * 35/100

print("\tSu nota parcial es : " + str(PNOTA2))
print("")

NOTA3 = input("Ingrese (Nota 3) : ")
print("-------------------------------------------------------")
print("Aclaración: Nota 3 equivalente al 50% de la nota final.")
print("-------------------------------------------------------")
print("")

PNOTA3 = float(NOTA3) * 50/100

print("\tSu nota parcial es : " + str(PNOTA3))

NFINAL = float(PNOTA1) + float(PNOTA2) + float(PNOTA3)
print("-------------------------------------------------------")
print("\t\tSU NOTA FINAL ES : " + str(NFINAL))
print("-------------------------------------------------------")
#_END_.%                                         