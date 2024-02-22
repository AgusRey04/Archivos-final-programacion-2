class Usuario():
    def __init__(self, nombre:str, apellido:str,email:str,password:str):
        self.__nombre = nombre
        self.__apellodo = apellido
        self.__password = password
        self.__email = email
        self.__videos = []
    @property
    def nombre(self):
        return self.__nombre
    @property
    def email(self):
        return self.__email
    @property
    def password(self):
        return self.__password
    @property
    def apellodo(self):
        return self.__apellodo
    @property
    def videos(self):
        return self.__videos
    
    # def validar_credenciales(self, email, password)->bool:
    #     if (email==self.email and password==self.password):
    #         return True
    #     else:
    #         return False

    def __str__(self) -> str:
        return f"{self.nombre}\n{self.apellodo}\n{self.email}\n{self.password}"

