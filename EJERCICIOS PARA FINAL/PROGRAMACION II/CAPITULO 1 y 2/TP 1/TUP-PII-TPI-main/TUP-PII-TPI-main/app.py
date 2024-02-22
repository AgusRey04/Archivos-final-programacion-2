# Trabajo Práctico I - Programación II

import libro as l
import os
import bibloteca as bi
import cod_generator as g
print("Bienvenido!")
respuesta = ''

def menu():
    print("1 - Gestionar Prestamo")
    print("2 - Gestionar Devolucion")
    print("3 - Registrar nuevo libro")
    print("4 - Elimiar ejemplar")
    print("5 - Mostrar ejemplares perstados")
    print("6 - Salir")

while respuesta != "salir":
    menu()
    opt = input("\n Ingrese la opción de menú: ")
    os.system ("cls") #Limpiar pantalla
    if opt.isnumeric():
        if int(opt) == 1:
            print("|||| GESTIONAR PRESTAMO ||||")
            bi.prestar_ejemplar_libro()
        elif int(opt) == 2:
            print("|||| GESTIONAR DEVOLUCION ||||")
            bi.devolver_ejemplar_libro()
        elif int(opt) == 3:
            print("|||| REGISTRAR NUEVO LIBRO ||||")
            bi.registrar_nuevo_libro()
        elif int(opt) == 4:
            print("|||| ELIMINAR EJEMPLAR ||||")
            bi.eliminar_ejemplar_libro()
        elif int(opt) == 5:
            print("|||| EJEMPLARES PRESTADOS ||||")
            bi.ejemplares_prestados()
        elif int(opt) == 6:
            respuesta = "salir"
        else: print("Ingrese una opción válida")
    else: 
        print("Ingrese una opción numérica")
    
    input("Presione cualquier tecla para continuar....") # Pausa

print("Hasta luego!.")