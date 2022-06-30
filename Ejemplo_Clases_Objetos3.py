class Perro():

  num_patas = 4

  def __init__(self, nom, raza, edad, num_patas):

    self.nombre = nom
    self.raza = raza
    self.edad = edad
    self.num_patas = num_patas
  
  def ladrar(self, cant):
    return 'guau' * cant

  def __str__(self):
    return f'{self.raza} de {self.edad} años'


class Persona():

  especie = "humano"
  cant_cerebros = 1

  def __init__(self, nombre, apellido, edad, meta, perro=None):

    self.nombre = nombre
    self.apellido = apellido
    self.edad = edad
    self.meta = meta
    self.perro = perro

  def saluda(self):
    return f'Hola, me llamo {self.nombre} {self.apellido}'

  def camina(self, pasos):

    if(pasos >= self.meta):
      return f'Felicidades {self.nombre}, cumpliste tu meta!'
    else:
      return 'No lograste tu meta, ponete las pilas!'

  def __str__(self):
    return f'Soy una persona que se llama {self.nombre} {self.apellido} y tengo un {self.perro}'

  def mi_perro(self):
    if self.perro:
      return f'Tengo un perro que se llama {self.perro}'