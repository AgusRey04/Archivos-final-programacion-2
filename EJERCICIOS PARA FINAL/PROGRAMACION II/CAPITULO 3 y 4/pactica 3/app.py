from usuario import *
from libro import *
from datetime import date
libros = [Libro("El Principito","Antoine de Saint-Exupéry",date(1943,4,6)),Libro("Juan Salvador Gaviota","Richard Bach",date(1970,1,1))]
administrador = Usuario(usuario='admin',contraseña='admin',estado=True,alta=date(2023,6,20),admin=True)
def menu_principal():
    print("1 - Ingresar como usuario")
    print("2 - Ingresar como administrador")
    print("3 - Ver libros del usuario...")
    print("4 - Ver usuario del libro...")
    print("5 - Salir")
def menu_administrador():
    print("1 - Nuevo usuario")
    print("2 - Nuevo libro")
    print("3 - Cerrar sesión")
def menu_usuario():
    print("1 - Agregar libro a mi coleccion")
    print("2 - Quitar libro de mi coleccion")
    print("3 - Cerrar sesión")
while True:
    menu_principal()
    opt = input("Ingrese una opción")
    if opt == "1":
        pass
    if opt == "2":  
        pass
    if opt == "3":
        pass
    if opt == "4":
        pass
    if opt == "5":
        print("Saludos!.")
        break