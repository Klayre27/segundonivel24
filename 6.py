# Clase base que representa un vehículo genérico
class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def mostrar_info(self):
        print(f'Marca: {self.marca}, Modelo: {self.modelo}')

# Clase derivada que representa un coche, heredando de Vehiculo
class Coche(Vehiculo):
    def __init__(self, marca, modelo, num_puertas):
        super().__init__(marca, modelo)
        self.num_puertas = num_puertas

    def mostrar_info(self):
        super().mostrar_info()
        print(f'Número de puertas: {self.num_puertas}')

# Clase derivada que representa una moto, heredando de Vehiculo
class Moto(Vehiculo):
    def __init__(self, marca, modelo, tipo):
        super().__init__(marca, modelo)
        self.tipo = tipo

    def mostrar_info(self):
        super().mostrar_info()
        print(f'Tipo de moto: {self.tipo}')

# Clase que representa un propietario con encapsulación de atributos
class Propietario:
    def __init__(self, nombre, identificacion):
        self.__nombre = nombre  # atributo privado
        self.__identificacion = identificacion  # atributo privado

    # Métodos getter para acceder a los atributos privados
    def get_nombre(self):
        return self.__nombre

    def get_identificacion(self):
        return self.__identificacion

    # Métodos setter para modificar los atributos privados
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_identificacion(self, identificacion):
        self.__identificacion = identificacion

    def mostrar_info(self):
        print(f'Nombre: {self.__nombre}, Identificación: {self.__identificacion}')

# Función que demuestra polimorfismo al aceptar cualquier tipo de Vehiculo
def mostrar_informacion(vehiculo):
    vehiculo.mostrar_info()

if __name__ == "__main__":
    # Crear instancias de las clases
    coche1 = Coche('Toyota', 'Corolla', 4)
    moto1 = Moto('Yamaha', 'R1', 'Deportiva')
    propietario1 = Propietario('Juan Pérez', '12345678')

    # Mostrar información de los vehículos
    coche1.mostrar_info()
    moto1.mostrar_info()

    # Mostrar información del propietario
    propietario1.mostrar_info()

    # Modificar y mostrar información actualizada del propietario
    propietario1.set_nombre('Carlos Gómez')
    propietario1.mostrar_info()

    # Demostrar polimorfismo
    mostrar_informacion(coche1)
    mostrar_informacion(moto1)
