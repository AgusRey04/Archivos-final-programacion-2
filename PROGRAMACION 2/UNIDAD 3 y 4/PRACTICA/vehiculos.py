class Vehiculo:
  def __init__(self, color, ruedas, velocidad, cilindrada=None):
    self.color = color
    self.ruedas = ruedas
    self.velocidad = velocidad
    self.cilindrada = cilindrada

  def mostrar_datos(self):
    if self.cilindrada is None:
      return f'Color: {self.color}; Ruedas: {self.ruedas}; Velocidad: {self.velocidad};'
    else:
      return f'Color: {self.color}; Ruedas: {self.ruedas}; Velocidad: {self.velocidad}; Cc: {self.cilindrada};'

class Coche(Vehiculo):
  def __init__(self, velocidad, cilindrada, color, ruedas):
    super().__init__(color, ruedas, velocidad, cilindrada)

class Bicicleta(Vehiculo):
  def __init__(self, tipo, color, ruedas, velocidad, cilindrada=None):
    super().__init__(color, ruedas, velocidad, cilindrada)
    self.tipo = tipo

  def mostrar_datos(self):
    return f'{super().mostrar_datos()} Tipo: {self.tipo};'

class Camioneta(Coche):
  def __init__(self, carga, velocidad, cilindrada, color, ruedas):
    super().__init__(velocidad, cilindrada, color, ruedas)
    self.carga = carga

  def mostrar_datos(self):
    return f'{super().mostrar_datos()} Carga: {self.carga} kg'

class Motocicleta(Bicicleta):
  def __init__(self, velocidad, cilindrada, tipo, color, ruedas):
    super().__init__(tipo, color, ruedas, velocidad, cilindrada)

v1 = Vehiculo("rojo", 4, 120, 1000)
c1 = Coche(3, 1500, "azul", 4)
b1 = Bicicleta("urbana", "verde", 2, 40)
ca1 = Camioneta(300, 3, 1500, "azul", 4)
m1 = Motocicleta(150, 250, "deportiva", "rosa", 2)

vehiculos = [v1, c1, b1, ca1, m1]

def catalogar(vehiculos, ruedas=None):

  if ruedas is not None:
    vehiculos = [v for v in vehiculos if v.ruedas == ruedas]
    print(f"Se han encontrado {len(vehiculos)} vehículos con {ruedas} ruedas:")

  for v in vehiculos:
    print(v.mostrar_datos())
    print(f'Type class: {type(v).__name__}')
    print()
  print("-"*30)

catalogar(vehiculos, 0)
catalogar(vehiculos, 2)
catalogar(vehiculos, 4)