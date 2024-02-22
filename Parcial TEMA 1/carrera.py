from datetime import date
class Carrera():
    def __init__(self,nombre:str,cominezo:date):
        self.__nombre = nombre
        self.__comienzo = cominezo
        self.titulos = []

    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def comienzo(self):
        return self.__comienzo
    @property
    def cantidad_titulos_requeridos(self):
        return len(self.titulos)
    
    def add_titulo_requerido(self,titulo):
        self.titulos.append(titulo)

    def remove_titulo_requerido(self,titulo):
        self.titulos.remove(titulo)

    def __str__(self) -> str:
        return f" {self.nombre}  Comienzo: {self.comienzo.month}/{self.comienzo.year}  TR: [{self.cantidad_titulos_requeridos}]"
            


# x = Carrera("Maestria en Ciencia de los Materiales",date(2024,4,2))
# titulos = [
#     Titulo("Ingeniero Mecánico","Universidad Tecnologica Nacional"),
#     Titulo("Contador Público Nacional","Universidad Nacional de Rosario"),
#     Titulo("Ingeniería Civil Mecanica")
# ]

# x.add_titulo_requerido(titulos[0])
# x.add_titulo_requerido(titulos[1])
# print(x)