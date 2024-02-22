from video import Video
class ListaReproduccion():
    __prox_nro = int(0)
    def __init__(self,nombre:str):
        self.__videos:list(Video)= []
        self.__nombre = nombre
        self.__nro = ListaReproduccion.get_prox_nro()
    @property
    def nombre(self):
        return self.__nombre
    @property
    def videos(self):
        return self.__videos
    @property
    def nro(self):
        return self.__nro
    @property
    def cantidad_video(self):
        return len(self.videos)
    @classmethod
    def get_prox_nro(cls)->int:
        cls.__prox_nro =+ 1
        return cls.__prox_nro
    
    def add_video(self,video:Video):
        self.videos.append(video)
    # def add_viedo(self,viedo:Video)-> None:
    #     self.__videos.append(viedo)
    # def remove_viedo(self,viedo):
    #     self.__videos.remove(viedo)
    def __str__(self) -> str:
        return f"{self.nombre} [{self.cantidad_video}]"


