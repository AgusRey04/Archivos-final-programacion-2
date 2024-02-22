class Auto():
    def __init__(self):
        self.largoChasis=250
        self.anchoChasis=120
        self.ruedas=4
        self.enmarcha=False
    def arrancar(self):
        self.enmarcha = True
    def estado(self):
        if(self.enmarcha):
            print("el auto arranco")
        else:
            print("el auto parado")
    def __str__(self) -> str:
        return f"el auto tiene {self.ruedas}"

miAuto=Auto()
miAuto.estado()
print(miAuto.ruedas)
miAuto2=Auto()
miAuto2.arrancar()
miAuto2.ruedas = 2
print(miAuto2.ruedas)
print(miAuto2)