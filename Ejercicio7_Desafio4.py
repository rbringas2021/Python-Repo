lista1 = [1,2,4,6,8,9,0,44,7,11,4,40,32,18,99,101,200]
lista2 = [1,4,6,3,7,9,44,33,18,99,100,3,6,8]

lista3 = lista1 + lista2

no_repetidos = []
repetidos = []

for i in lista3:
    if(i not in no_repetidos):
        no_repetidos.append(i)
    else:
	    if(i not in repetidos):
	        repetidos.append(i)

repetidos.sort()

print(repetidos)

#__END__.