from cliente import Cliente
from producto import Producto
from datetime import date
from descuento import *
from compra import Compra

#inicializo lista vacía
compras = []

#genero 2 clientes
cliente1 = Cliente("Juan", "Perez", "37514256", 333)
cliente2 = Cliente("Marta", "Sanchez", "42514785")

print(cliente1)
#genero productos
productos = [
    Producto("Cerveza Weisse PATAGONIA Botella 730 Cc", "5555421652", float(970.98)),
    Producto("Vino Blanco Dulce TORO Ttb 1 Ltr", "5665422652", float(660.30)),
    Producto("Vermouth MARTINI Extra Dry Botella 995 Cc", "9894421778", float(2258.00))
]
print(productos[0])
#genero compras
compras.append(Compra(cliente1))
compras.append(Compra(cliente2))
#print(compras[0])
#agrego productos da las compras
compras[0].add_producto(productos[0])
compras[0].add_producto(productos[0])
compras[0].add_producto(productos[0])
compras[0].add_producto(productos[0])
compras[0].add_producto(productos[0])
compras[0].add_producto(productos[0])

compras[1].add_producto(productos[1])
compras[1].add_producto(productos[1])
compras[1].add_producto(productos[2])

#facturar compras
compras[0].facturar_compra()
compras[1].facturar_compra()
print(compras[0])
print("sin problemas")

###########################