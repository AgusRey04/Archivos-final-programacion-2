from datos import *

def menu(): 
    return "\n1 - Home\n2 - Nueva Lista\n3 - Ver listas\n4 - Salir\n"

def home(): 
    for var in videos:
        print (var)
def nuevaLista():
    print("creando nueva lista de reproduccion")
    nueva_lista_repro= str(input("Ingrese el nombre de la lista: "))
    listas.append(ListaReproduccion(nueva_lista_repro))
    #print(listas[len(listas)-1])
    print("Selecione al menos un video para crear la lista...")
    for i, var in enumerate(videos,1):
        print(f"{i} - {var.nombre}")
    selec_video = int(input("Selecione el vido: "))
    
    listas[len(listas)-1].add_video(selec_video)
    print("Se creo la lista existente...")
    # print(listas[len(listas)-1])
def verLista(): 
    for var in listas:
        if var.cantidad_video >0:
            print(var) 
while True:
    print(menu())
    opt = input("Ingrese la opcion seleccionada: ")
    if opt == "1":
        home()
        continue
    if opt == "2":
        nuevaLista()
        continue
    if opt == "3":
        verLista()
        continue
    if opt == "4":
        print("Gracias por utilizar nuestro sistema.")
        break
    else:
        print("Error, Ingrese una opcion valida...")