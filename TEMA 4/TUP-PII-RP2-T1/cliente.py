class Cliente():
    def __init__(self,nombre:str,apellido:str,nro_documento:str,nro_comunidad: int = None):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__nro_documento = nro_documento
        self.__nro_comunidad = nro_comunidad
    
    @property
    def nombre(self):
        return self.__nombre
    @property
    def apellido(self):
        return self.__apellido
    @property
    def nro_documento(self):
        return self.__nro_documento
    @property
    def nro_comunidad(self):
        return self.__nro_comunidad
    
    def __str__(self) -> str:
        return f"Nombre:{self.nombre}\napellido:{self.apellido}\n Numero de documento: {self.nro_documento}\n numero de comunidad: {self.nro_comunidad}"
    
# cliente1 = Cliente("Juan", "Perez", "37514256", 333)
# print(cliente1)
# cliente2 = Cliente("Marta", "Sanchez", "42514785")
# print(cliente2)