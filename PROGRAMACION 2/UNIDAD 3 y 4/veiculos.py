class Vehiculos():
    def __init__(self, marca, modelo):
        self.marca=marca
        self.modelo=modelo
        self.enmarcha=False
        self.acelera=False
        self.frena=False
    def arrancar(self):
        self.enmarcha=True
    def acelerar(self):
        self.acelera=True
    def frenar(self):
        self.frena=True
    def estado(self):
        print('Marca:', self.marca, 'y Modelo:', self.modelo)

class Moto(Vehiculos):
    hwheelie = ''
    def wheelie(self):
        self.hwheelie = 'Haciendo Wheelie'
    def estado(self):
        print('Marca: ', self.marca, 'y Modelo: ',self.modelo)
        print(self.hwheelie)

miMoto = Moto('Honda', 'CBR')
miMoto.estado()
miMoto.wheelie()
miMoto.estado()
miMoto.arrancar()
print(miMoto.enmarcha)