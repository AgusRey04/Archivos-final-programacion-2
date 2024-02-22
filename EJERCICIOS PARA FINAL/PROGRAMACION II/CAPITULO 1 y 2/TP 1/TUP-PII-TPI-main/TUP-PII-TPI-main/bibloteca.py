import libro as l

# Crear una lista vacía para almacenar los libros
libros = []

# Añadir los diccionarios a la lista
libros.append(l.libro1)
libros.append(l.libro2)
libros.append(l.libro3)
#--------------------------------
def validar_codigo(ing_codigo,libros):
    for i in libros:
        if  ing_codigo==i["cod"]:
            return i
    return False
#---------------------------------
def ejemplares_prestados():
    print("#######################################################################################################")
    for i in libros:
        print(f"  Codigo del libro: {i["cod"]}\n  Titulo:{i["titulo"]}\n  Autor: {i["autor"]}")
        if i['cant_ej_pr'] >0:
            print(f"  Camtidad de ejemplares prestados: {i['cant_ej_pr']}")
        else:
            print("  NO tiene ejemplares prestados")
        print("#######################################################################################################")
    return None

def registrar_nuevo_libro():
    nuevo_libro = l.nuevo_libro()
    libros.append(nuevo_libro)
    print("---------------------------------------")
    mostrar_nuevo_libro()
    print("---------------------------------------")
    return None

def eliminar_ejemplar_libro():
    ing_codigo = str(input("Ingresar Codigo:"))
    codigo_validado = validar_codigo(ing_codigo,libros)
    if codigo_validado != False:
        print(f"    Titulo:{codigo_validado["titulo"]} \n    Autor: {codigo_validado["autor"]}")
        if codigo_validado["cant_ej_ad"] > 0:
            print(f"    Camtidad de ejemplares prestados: {codigo_validado["cant_ej_ad"]}")
            confirmar_prestamo = str(input(f"Confirmar eliminacion del ejemplar si o no? S/N "))
            if (confirmar_prestamo=="S" or confirmar_prestamo=="s"):
                codigo_validado["cant_ej_ad"] -= 1 
                #print(f"Camtidad de ejemplares prestados: {codigo_validado['cant_ej_pr']}")
                print(f"Se a confirmado la eliminacion del ejemplar ")
            else:
                print(f"NO se confirmo la eliminacion del ejemplar")
        else:
            print(f"    Camtidad de ejemplares : NO QUEDAN EJEMPLARES")
    else:
        print("----------- ERROR---------------- \n NO se a encoontrado el codigo...")
    return None

def prestar_ejemplar_libro():
    ing_codigo = str(input("Ingresar Codigo:"))
    codigo_validado = validar_codigo(ing_codigo,libros)
    if codigo_validado != False:
        print(f"    Titulo:{codigo_validado["titulo"]} \n    Autor: {codigo_validado["autor"]}")
        if codigo_validado["cant_ej_ad"] > 0:
            print(f"    Camtidad de ejemplares: {codigo_validado["cant_ej_ad"]}")
            confirmar_prestamo = str(input(f"Confirmar prestamo si o no? S/N "))
            if (confirmar_prestamo=="S" or confirmar_prestamo=="s"):
                codigo_validado["cant_ej_ad"] -= 1 
                codigo_validado['cant_ej_pr'] += 1
                #print(f"Camtidad de ejemplares prestados: {codigo_validado['cant_ej_pr']}")
                print(f"Se a confirmado el prestamo ")
            else:
                print(f"NO se confirmo el presamo")
        else:
            print(f"    Camtidad de ejemplares: NO QUEDAN EJEMPLARES")
    else:
        print("----------- ERROR---------------- \n NO se a encoontrado el codigo...")
    return None

def devolver_ejemplar_libro():
    ing_codigo = str(input("Ingresar Codigo:"))
    codigo_validado = validar_codigo(ing_codigo,libros)
    if codigo_validado != False:
        print(f"    Titulo:{codigo_validado["titulo"]} \n    Autor: {codigo_validado["autor"]}")
        if codigo_validado["cant_ej_pr"] > 0:
            print(f"    Camtidad de ejemplares prestados: {codigo_validado["cant_ej_pr"]}")
            confirmar_prestamo = str(input(f"Confirmar prestamo si o no? S/N "))
            if (confirmar_prestamo=="S" or confirmar_prestamo=="s"):
                codigo_validado["cant_ej_ad"] += 1 
                codigo_validado['cant_ej_pr'] -= 1
                #print(f"Camtidad de ejemplares prestados: {codigo_validado['cant_ej_pr']}")
                print(f"Se a confirmado la devolución ")
            else:
                print(f"NO se confirmo la devolución")
        else:
            print(f"    Camtidad de ejemplares pretados: NO QUEDAN EJEMPLARES PRESTADOS")
    else:
        print("----------- ERROR---------------- \n NO se a encoontrado el codigo...")
    return None


#---------------------------------
def mostrar_nuevo_libro():
    ultimo_libro = libros[len(libros)-1]
    print(f"  Codigo del libro: {ultimo_libro["cod"]}\n  Camtidad de ejemplares:{ultimo_libro["cant_ej_ad"]}\n  Camtidad de ejemplares prestados: {ultimo_libro["cant_ej_pr"]}\n  Titulo:{ultimo_libro["titulo"]}\nAutor: {ultimo_libro["autor"]}")
    return None
#--------------------------------