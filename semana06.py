# Clase base: Vehiculo
class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def mostrar_info(self):
        print(f'Marca: {self.marca}, Modelo: {self.modelo}')

# Clase derivada: Coche
class Coche(Vehiculo):
    def __init__(self, marca, modelo, num_puertas):
        super().__init__(marca, modelo)
        self.num_puertas = num_puertas

    def mostrar_info(self):
        super().mostrar_info()
        print(f'Número de puertas: {self.num_puertas}')

# Clase derivada: Moto
class Moto(Vehiculo):
    def __init__(self, marca, modelo, tipo):
        super().__init__(marca, modelo)
        self.tipo = tipo

    def mostrar_info(self):
        super().mostrar_info()
        print(f'Tipo de moto: {self.tipo}')
