from titulo import Titulo
class Aspirante():
    def __init__(self, nombre:str,apellido:str,email:str,num_telefono:str):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__email = email
        self.__num_telefono = num_telefono
        self.titulos = []

    @property
    def nombre(self):
        return self.__nombre
    @property
    def apellido(self):
        return self.__apellido
    @property
    def email(self):
        return self.__email
    @property
    def num_telefono(self):
        return self.__num_telefono

    def add_titulo(self,titulo):#  titulo:Titulo
        self.titulos.append(titulo)
        
    def remove_titulo(self,titulo): # titulo:Titulo
        self.titulos.remove(titulo)
    def __str__(self) -> str:
        return f"#{self.nombre} {self.apellido}\n#{self.email}\n#{self.num_telefono}\n{len(self.titulos)}"
    
# titulo =   Titulo("Ingeniero Mecánico","Universidad Tecnologica Nacional")
# aspirante = Aspirante("Juan", "Perez", "perezjuan@gmail.com", "+5493416214584")
# aspirante.add_titulo(titulo) 
# print(aspirante)
# aspirante.remove_titulo(titulo)
# print(aspirante)

