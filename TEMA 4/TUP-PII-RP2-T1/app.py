from datos import *

def menu(): 
    return "\n1 - Nueva Compra\n2 - Resumen Compras\n3 - Salir\n"

def menu_compra():
    return "\n1 - Agregar Producto\n2 - Finalizar Compra\n"

def cliente_loggeado():
    '''
        dummy function
        retorna cliente loggeado
    '''
    return cliente1

while True:
    print(menu())
    opt = input("Ingrese la opcion seleccionada: ")
    if opt == "1":
        nueva_compra = Compra(cliente_loggeado()) #se genera una nueva compra con el cliente loggeado
        compras.append(nueva_compra)
        nueva_compra.compra_facturado = False 
        nueva_compra.monto_facturado = 0
        while True:
            print(menu_compra())
            opt = input("Ingrese la opcion seleccionada: ")
            if opt == "1":
                for i,val in enumerate(productos,1):
                    print(f"{i} {val}")
                selec_producto = int(input("Ingrese un producto: "))
                nueva_compra.add_producto(productos[selec_producto-1])
            elif opt == "2" :
                nueva_compra.facturar_compra()
                break
            else:
                print("Error, Ingrese una opcion valida...")
    elif opt == "2":
        for var in compras:
            print(var)
    elif opt == "3":
        print("Gracias por utilizar nuestro sistema.")
        break
    else:
        print("Error, Ingrese una opcion valida...")