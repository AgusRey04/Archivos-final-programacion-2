from aspirante import Aspirante
from carrera import Carrera
from datetime import date
class Inscripcion():
    prox_nro = int(0)
    def __init__(self,aspirante:Aspirante,carrera:Carrera) -> None:
        self.__carreras = carrera
        self.__aspirantes = aspirante
        self.__fecha_inscripcion = date.today()
        self.__inscripcion_activa:bool = True
        self.__nro:int = Inscripcion.get_prox_nro()

    @property
    def carreras(self):
        return self.__carreras
    
    @property
    def aspirantes(self):
        return self.__aspirantes
    
    @property
    def fecha_inscripcion(self):
        return self.__fecha_inscripcion 
    
    @property
    def inscripcion_activa(self):
        return self.__inscripcion_activa
    @inscripcion_activa.setter
    def inscripcion_activa(self,nueva_inscripcion_activa):
        self.__inscripcion_activa = nueva_inscripcion_activa
    
    @property
    def nro(self):
        return self.__nro
    
    @classmethod
    def get_prox_nro(cls):
        cls.prox_nro += 1
        return cls.prox_nro
     
    def __str__(self) -> str:
        return  f"Incripcion Nuemro: {self.inscripcion_activa}, Aspirante: {self.aspirantes.nombre} {self.aspirantes.apellido}, Carrera: {self.carreras.nombre}"