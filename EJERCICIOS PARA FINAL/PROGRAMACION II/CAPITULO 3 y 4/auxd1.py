from abc import ABC, abstractmethod
from datetime import date

class Persona(ABC):
    def __init__(self, nombre: str, apellido: str, fecha_nacimiento: date) -> None:
        self._nombre = nombre
        self._apellido = apellido
        self._fecha_nacimiento = fecha_nacimiento
        
    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def apellido(self) -> str:
        return self._apellido

    @property
    def fecha_nacimiento(self) -> date:
        return self._fecha_nacimiento

    @property
    def edad(self) -> int:
        return self.calcular_edad()

    @abstractmethod
    def calcular_edad(self) -> int:
        pass

class Usuario(Persona):
    def __init__(self, nombre: str, apellido: str, fecha_nacimiento: date, username: str) -> None:
        super().__init__(nombre, apellido, fecha_nacimiento)
        self.__username = username

    @property
    def username(self) -> str:
        return self.__username

    def calcular_edad(self) -> int:
        # Obtener la fecha actual
        fecha_actual = date.today()

        # Calcular la diferencia entre la fecha actual y la fecha de nacimiento
        edad = fecha_actual.year - self.fecha_nacimiento.year - ((fecha_actual.month, fecha_actual.day) < (self.fecha_nacimiento.month, self.fecha_nacimiento.day))

        return edad
