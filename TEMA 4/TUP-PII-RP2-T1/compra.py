from datetime import date, datetime
from producto import Producto
class Compra():
    def __init__(self,cliente:object):
        self.__cliente = cliente
        self.__cliente_facturar: bool
        self.__monto_facturado: float
        self.__fecha_hora = datetime.now()  #date.today() 
        self.__productos:list(Producto) = []
    @property
    def cliente(self):
        return self.__cliente
    @property
    def fecha_hora(self):
        return self.__fecha_hora
    @property
    def monto_facturado(self):
        return self.__monto_facturado
    @monto_facturado.setter
    def monto_facturado(self,nuevo):
        self.__monto_facturado = nuevo
    @property
    def compra_facturado(self):
        return self.__cliente_facturar
    @compra_facturado.setter
    def compra_facturado(self,nuevo):
        self.__cliente_facturar = nuevo
    @property
    def productos(self):
        return self.__productos
    @property
    def cantidad_productos(self):
        return len(self.__productos)
    @property
    def monto_total(self):
        sum = 0 
        for var in self.__productos:
            sum += var.precio_unitario
        return sum
        
        
    def facturar_compra(self):
        self.monto_facturado = self.monto_total
        self.compra_facturado = True

    def add_producto(self,producto:Producto):
        self.__productos.append(producto)

    def __str__(self) -> str:
        return datetime.strftime(self.fecha_hora,"%d/%m/%Y %H:%M") + f" Monto: {self.monto_facturado} Productos:[{self.cantidad_productos}] Cliente: {self.cliente.nro_documento}"
        