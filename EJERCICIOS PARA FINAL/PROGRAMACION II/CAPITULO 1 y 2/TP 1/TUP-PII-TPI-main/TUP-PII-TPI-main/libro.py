# Crear un diccionario para cada libro
import cod_generator as g
libro1 = {'cod': 'CRBJsAkS', 'cant_ej_ad': 3, 'cant_ej_pr': 1, "titulo": "Cien años de soledad", "autor": "Gabriel García Márquez"}
libro2 = {'cod': 'QgfV4j3c', 'cant_ej_ad': 4, 'cant_ej_pr': 2, "titulo": "El principito", "autor": "Antoine de Saint-Exupéry"}
libro3 = {'cod': 'adOd09UE', 'cant_ej_ad': 1, 'cant_ej_pr': 0, "titulo": "El código Da Vinci", "autor": "Dan Brown"}

def nuevo_libro():
    codigo_nuevo = generar_codigo()
    while True:
        try:
            cant_ej_nuevo = int(input(" Camtidad de ejemplares:"))
            if cant_ej_nuevo <= 0:
                print("Error: tiene que ser un numero > 0 ")
            else:
                break
        except ValueError:
            print("Error: Ingrese un número válido para la cantidad de libros.")

    titulo_nuevo = str(input(" Ingresar el Titulo del libro: "))
    autor_nuevo = str(input("Ingresar el autror del libro: "))

    return {'cod': codigo_nuevo, 'cant_ej_ad': cant_ej_nuevo, 'cant_ej_pr': 0, 'titulo': titulo_nuevo, 'autor': autor_nuevo}

def generar_codigo():
    return g.generar()