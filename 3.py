def mostrar_informacion(vehiculo):
    vehiculo.mostrar_info()

# Crear instancias de las clases
coche = Coche('Toyota', 'Corolla', 4)
moto = Moto('Yamaha', 'R1', 'Deportiva')

# Polimorfismo: la misma función muestra información de diferentes tipos de vehículos
mostrar_informacion(coche)
mostrar_informacion(moto)
