from abc import ABC, abstractmethod
from datetime import date

class Persona(ABC):
    def __init__(self, nombre: str, apellido: str) -> None:
        self._nombre = nombre
        self._apellido = apellido
        self._fecha_nacimiento = date(1,1,1)
        
        self._edad = self.calcular_edad()

    @property
    def nombre(self) -> str:
        return self._nombre
    @nombre.setter
    def nombre(self,nuevo_estado):
        self._nombre = nuevo_estado
    @property
    def apellido(self) -> str:
        return self._apellido

    @property
    def fecha_nacimiento(self) -> date:
        return self._fecha_nacimiento

    @property
    def edad(self) -> int:
        return self._edad

    @abstractmethod
    def calcular_edad(self) -> int:
        pass
class Usuario(Persona):
    def __init__(self, nombre, apellido, fecha_nacimiento, user_name: str,email,password) -> None:
        super().__init__(nombre  , apellido)
        self.__user_name: str = user_name
        self.__estado: bool = True
        self.__email:str = email
        self.__password: str = password
        self.__fecha_alta = date.today()
        self.__fecha_baja : date = None
    @property
    def nombre(self) -> str:
        return self._nombre
    @nombre.setter
    def nombre(self,nuevo_estado):
        self._nombre = nuevo_estado

    @property
    def fecha_nacimiento(self) -> date:
        return self._fecha_nacimiento
    @fecha_nacimiento.setter
    def fecha_nacimiento(self,nuevo_fecha_nacimiento):
        self._fecha_nacimiento = nuevo_fecha_nacimiento
    @property
    def estado(self):
        return self.__estado
    
    @estado.setter
    def estado(self,nuevo_estado):
        self.__estado = nuevo_estado
    @property
    def user_name(self)-> str:
        return self.__user_name
    
    @property
    def password(self)-> str:
        return self.__password
    
    @property
    def email(self)-> str:
        return self.__email
    @property
    def fecha_alta(self)-> date:
        return self.__fecha_alta
    @property
    def fecha_baja(self):
        return self.__fecha_baja
    @property
    def edad(self) -> int:
        return self.calcular_edad()
    # @edad.setter
    # def edad(self):
    #     self.calcular_edad()
    def validar_credenciales(self, usuario: str, password: str) -> bool:
        if (usuario==self.user_name and password==self.password):
            return True
        else:
            return False

    def baja_usuario(self):
        self.estado = False
        
    def calcular_edad(self) -> int:
        # Obtener la fecha actual
        fecha_actual = date.today()

        # Calcular la diferencia entre la fecha actual y la fecha de nacimiento
        edad = fecha_actual.year - self.fecha_nacimiento.year 

        return edad
    def __str__(self) -> str:
        if self.fecha_baja == None:
            return f"Usuario:{self.user_name}\nEmail: {self.email}\nFecha de alta: {self.fecha_alta}\nNombre :{self.nombre}\nFecha de nacimiento: {self.fecha_nacimiento} sssssss{self.edad}"
        else:
            return f"Usuario:{self.user_name}\nEmail: {self.email}\nFecha de alta: {self.fecha_alta}\nFecha de baja\n Nombre:{self.nombre}"
        