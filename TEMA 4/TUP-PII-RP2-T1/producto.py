class Producto():
    def __init__(self,nombre:str,codigo:str,precio_unitario:float):
        self.__nombre = nombre
        self.__codigo = codigo
        self.__precio_unitario = precio_unitario
    @property
    def nombre(self):
        return self.__nombre
    @property
    def codigo(self):
        return self.__codigo
    @property
    def precio_unitario(self):
        return self.__precio_unitario

    def __str__(self) -> str:
        return f"| {self.codigo}: {self.nombre} ${self.precio_unitario} "
    def _validat_codigo(self,codigo:str)->str:
        pass
# productos = [
#     Producto("Cerveza Weisse PATAGONIA Botella 730 Cc", "5555421652", float(970.98)),
#     Producto("Vino Blanco Dulce TORO Ttb 1 Ltr", "5665422652", float(660.30)),
#     Producto("Vermouth MARTINI Extra Dry Botella 995 Cc", "9894421778", float(2258.00))
# ]
# for i,val in enumerate(productos,1):
#     print(f"{i} {val}")