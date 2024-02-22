class Auto():
    def __init__(self) -> None:
        largoChasis=250
        anchoChasis=120
        ruedas=4
        enmarcha=False
    def arrancar(self):
        self.enmarcha=True
    def estado(self):
        if(self.enmarcha):
            return'El auto está en marcha'
        else:
            return 'El auto está detenido'
miAuto=Auto()
print(miAuto.estado()) # El auto está detenido
miAuto.arrancar()
print(miAuto.estado()) # El auto está en marcha