class Persona():
    def __init__(self, nombre, edad, lugar_residencia):
        self.nombre=nombre
        self.edad=edad
        self.lugar_residencia=lugar_residencia
    def descripcion(self):
        print('Nombre:', self.nombre)
        print('Edad:', self.edad)
        print('Residencia:', self.lugar_residencia)
class Empleado(Persona):
    def __init__(self, salario, antiguedad, nombre, edad, lugar_residencia):
        super().__init__(nombre,edad,lugar_residencia)
        self.salario=salario
        self.antigüedad=antiguedad
    def descripcion(self):
        super().descripcion()
        print('salario:', self.salario)
        print('antigüedad:', self.antigüedad)
Lucas=Empleado(100000, 10, 'Lucas', 25, 'Argentina')
Lucas.descripcion()