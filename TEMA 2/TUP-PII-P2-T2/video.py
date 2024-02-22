from datetime import date
from usuario import Usuario
from tag import Tag
class Video():
    def __init__(self,nombre:str,usuario:Usuario):
        self.__nombre = nombre
        self.__fecha_publicacion = date.today()
        self.__usuario = usuario
        self.__tag = []
    @property
    def nombre(self):
        return self.__nombre
    @property
    def usuario(self):
        return self.__usuario
    @property
    def tag(self):
        return self.__tag
    @property
    def fecha_publicacion(self):
        return self.__fecha_publicacion
    
    def __str__(self) -> str:
        return f"{self.nombre} [Autor: {self.usuario.nombre} - Publicado: {self.fecha_publicacion.day}/{self.fecha_publicacion.month}/{self.fecha_publicacion.year}]"
    
    def add_tag(self,tag:Tag):
        self.__tag.append(tag)
    def remove_tag(self,tag:Tag):
        self.__tag.remove(tag)
# videos = [
#     Video("POO - La guia definitiva", usuario),
#     Video("¿Como aprender programacion y no morir en el intento?", usuario),
#     Video("Programacion en Python para videojuegos", usuario)
# ]

# print (videos[0])


