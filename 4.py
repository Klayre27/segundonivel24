if __name__ == "__main__":
    # Instancias de Vehiculo, Coche y Moto
    coche1 = Coche('Toyota', 'Corolla', 4)
    moto1 = Moto('Yamaha', 'R1', 'Deportiva')

    # Instancia de Propietario
    propietario1 = Propietario('Juan Pérez', '12345678')

    # Mostrar información de los vehículos
    coche1.mostrar_info()
    moto1.mostrar_info()

    # Mostrar información del propietario
    propietario1.mostrar_info()

    # Cambiar el nombre del propietario y mostrar la información actualizada
    propietario1.set_nombre('Carlos Gómez')
    propietario1.mostrar_info()

    # Polimorfismo
    mostrar_informacion(coche1)
    mostrar_informacion(moto1)
