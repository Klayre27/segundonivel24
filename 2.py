# Clase con encapsulación
class Propietario:
    def __init__(self, nombre, identificacion):
        self.__nombre = nombre  # atributo privado
        self.__identificacion = identificacion  # atributo privado

    # Métodos getter
    def get_nombre(self):
        return self.__nombre

    def get_identificacion(self):
        return self.__identificacion

    # Métodos setter
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_identificacion(self, identificacion):
        self.__identificacion = identificacion

    def mostrar_info(self):
        print(f'Nombre: {self.__nombre}, Identificación: {self.__identificacion}')
