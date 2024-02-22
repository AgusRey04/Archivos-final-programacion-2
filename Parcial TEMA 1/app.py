from datos import *

def menu(): 
    return "\n1 - Nueva Inscripción\n2 - Ver carreras\n3 - Ver inscripciones\n4 - Salir\n"

def nueva_inscripcion():
    for i, var in enumerate(carreras):
        print(f"{i+1} - {var.nombre}")
    selec_carrera = int(input("Selecionar la carrera: "))
    ins_carrera = carreras[selec_carrera-1]
    print("Datos del aspirante...")
    ins_aspitante_nombre = input("Ingrese el nombre: ")
    ins_aspitante_apellido= input("Ingrese el apellido: ")
    ins_aspitante_email= input("Ingrese el email: ")
    ins_aspitante_telefono= input("Ingrese el telefono: ")
    print("Indicar el titudo de grado del aspirante...")
    for i, var in enumerate(titulos):
        print(f"{i+1} - {var.nombre}")
    selec_titulo = int(input("Seleccione el titulo: "))
    ins_titulo =titulos[selec_titulo-1] 
    #Aspirante("Juan", "Perez", "perezjuan@gmail.com", "+5493416214584")
    nuevo_aspirante = Aspirante(ins_aspitante_nombre,
                                ins_aspitante_apellido,
                                ins_aspitante_email,
                                ins_aspitante_telefono)
    #print(nuevo_aspirante)

    #Inscripcion(aspirante, carreras[0])
    nuevo_aspirante.add_titulo(ins_titulo)
    inscripciones.append(Inscripcion(nuevo_aspirante,ins_carrera))
    
    #print(n_inscripcion)
    
    print("se registro la inscripcion exitosamente...")


def ver_carreras():
    carrera_ordenada = sorted(carreras, key=lambda x: x.comienzo, reverse=False)
    for i,var in enumerate(carrera_ordenada,1):
        print(f"{i} - {var}")

def ver_inscripciones():
    for var in inscripciones:
        if var.inscripcion_activa:
            print(var)
    
while True:
    print(menu())
    opt = input("Ingrese la opcion seleccionada: ")
    if opt == "1":
        nueva_inscripcion()
        continue
    if opt == "2":
        ver_carreras()
        continue
    if opt == "3":
        ver_inscripciones()
        continue
    if opt == "4":
        print("Gracias por utilizar nuestro sistema.")
        break
    else:
        print("Error, Ingrese una opcion valida...")