class Usuario():

    def __init__(self, nombre:str, apellido:str, email:str, password:str) -> None:
        self.__nombre = nombre
        self.__apellido = apellido
        self.__email = email
        self.__password = password

    @property
    def nombre(self) -> str:
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevo_nombre) -> None:
        self.__nombre = nuevo_nombre

    @property
    def apellido(self) -> str:
        return self.__apellido

    @apellido.setter
    def apellido(self, nuevo_apellido) -> None:
        self.__apellido = nuevo_apellido

    @property
    def email(self) -> str:
        return self.__email

    @email.setter
    def email(self, nuevo_email) -> None:
        self.__email = nuevo_email

    @property
    def password(self) -> str:
        return self.__password

    @password.setter
    def password(self, nuevo_password) -> None:
        self.__password = nuevo_password

    def __str__(self) -> str:
        return f"{self.apellido}, {self.nombre}"

    def validar_credenciales(self, email:str, password:str) -> bool:
        return self.email == email and self.password == password

