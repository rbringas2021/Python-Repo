class Perro():                  # Clase Perro

    #num_patas = 4               # Atributo de Clase.

    def __init__(self, nombre, raza, edad):            # Constructor de Instancia.
        self.nombre = nombre                           # Atributo de Instancia.
        self.raza = raza                               # Atributo de Instancia.
        self.edad = edad                               # Atributo de Instancia.

    def ladrar(self, cant):                         # Metodo de Instancia.
        return "Guau" * cant                        # Retorno de Metodo de Instancia.

perro1 = Perro("Cachito", "Labrador", 2)            # Instancia de Clase Perro.
perro2 = Perro("Firulais", "Dalmata", 4)            # Instancia de Clase Perro.

print(perro1.ladrar(3))                             # Llamada de Metodo de Instancia.

print(perro2.nombre)                                # Llamada de Atributo de Instancia.

