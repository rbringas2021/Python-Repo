class Perro():

    def __init__(self, nombre, raza, edad):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad

    def ladrar(self, cant):
        return "Guau" * cant

perro1 = Perro("Cachito", "Labrador", 2)

print(perro1.nombre)
print(perro1.raza)
print(perro1.edad)
print(perro1.ladrar(3))



