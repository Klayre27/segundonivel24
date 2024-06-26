# Programación Tradicional

# Función para ingresar datos diarios de temperatura
def ingresar_temperaturas_diarias():
    temperaturas = []
    for i in range(7):
        temperatura = float(input(f"Ingrese la temperatura del día {i + 1}: "))
        temperaturas.append(temperatura)
    return temperaturas

# Función para calcular el promedio semanal de temperaturas
def calcular_promedio_semanal(temperaturas):
    if len(temperaturas) < 7:
        print("No hay suficientes datos para calcular el promedio semanal.")
        return None
    promedio = sum(temperaturas) / len(temperaturas)
    return promedio

# Programa principal
def main_tradicional():
    print("Programación Tradicional")
    temperaturas = ingresar_temperaturas_diarias()
    promedio = calcular_promedio_semanal(temperaturas)
    if promedio:
        print(f"El promedio semanal de temperaturas es: {promedio}")

if __name__ == "__main__":
    main_tradicional()
