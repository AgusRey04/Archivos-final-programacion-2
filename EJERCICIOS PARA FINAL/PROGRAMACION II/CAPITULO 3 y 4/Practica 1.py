from datetime import date
x = date.today()

class Usuario():
    def __init__(self,user_name,email,password) -> None:
        self.__user_name: str = user_name
        self.__estado: bool = True
        self.__email:str = email
        self.__password: str = password
        self.__nombre: str = ""
        self.__apellido: str
        self.__fecha_alta = date.today()
        self.__fecha_baja : date = None
    

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
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self,nuevo_nombre):
        self.__nombre = nuevo_nombre

    @nombre.deleter
    def nombre(self):
        self.__nombre ="aaaa"
    
    @property
    def apellido(self):
        return self.__apellido
    @apellido.setter
    def apellido(self,nuevo_apellido):
        self.__apellido = nuevo_apellido
        
    def validar_credenciales(self, usuario: str, password: str) -> bool:
        if (usuario==self.user_name and password==self.password):
            return True
        else:
            return False

    def baja_usuario(self):
        self.estado = False
        
    def __str__(self) -> str:
        if self.fecha_baja == None:
            return f"Usuario:{self.user_name}\nEmail: {self.email}\nFecha de alta: {self.fecha_alta}\n Nombre:{self.nombre}"
        else:
            return f"Usuario:{self.user_name}\nEmail: {self.email}\nFecha de alta: {self.fecha_alta}\nFecha de baja\n Nombre:{self.nombre}"
#-----------------------------------   App   ---------------------------------------
print("####   Crear un usuario   ####")

user_name = str(input("ingrese su nombre de usuario: ")) 
email = str(input("ingrese su Email: "))
password=str(input("Ingrese su password: "))
nuevo_usuario = Usuario(user_name,email,password)
print(nuevo_usuario.estado)
nuevo_usuario.nombre = "Agustin"
nuevo_usuario.apellido = "Reymundez"
print(nuevo_usuario)
nuevo_usuario.baja_usuario()
print(nuevo_usuario.estado)
print("------------------------------------------------------")
usuario = str(input("INGRESAR USUARIO: "))
password = str(input("INGRESAR PASSWORD: "))
print(nuevo_usuario.validar_credenciales(usuario,password))

# print(nuevo_usuario)
# nuevo_usuario.nombre ="Agustin"
# print(nuevo_usuario)
# del nuevo_usuario.nombre
# print(nuevo_usuario)
