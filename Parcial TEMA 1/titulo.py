class Titulo():

    def __init__ (self, nombre: str, universidad: str = "Extranjera") -> None:
        self.__nombre = nombre
        self.__universidad = universidad

    @property
    def nombre(self) -> str:
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevo_nombre: str) -> None:
        self.__nombre = nuevo_nombre

    @property
    def universidad(self) -> str:
        return self.__universidad

    @universidad.setter
    def universidad(self, nueva_universidad: str) -> None:
        self.__universidad = nueva_universidad

    def __str__(self) -> str:
        return f"Titulo: {self.nombre} expedido por {self.universidad}"
    

# titulo_1  = Titulo("Ingeniero Mecánico","Universidad Tecnologica Nacional")
# titulo_2 =  Titulo("Contador Público Nacional","Universidad Nacional de Rosario")
# titulo_3  = Titulo("Ingeniería Civil Mecanica")


# print(f" {titulo_1} \n {titulo_2} \n {titulo_3}" )