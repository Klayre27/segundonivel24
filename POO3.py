# Programación Orientada a Objetos (POO)

class RegistroClima:
    def __init__(self):
        self.temperaturas_diarias = []

    def ingresar_temperaturas_diarias(self):
        for i in range(7):
            temperatura = float(input(f"Ingrese la temperatura del día {i + 1}: "))
            self.temperaturas_diarias.append(temperatura)

    def calcular_promedio_semanal(self):
        if len(self.temperaturas_diarias) < 7:
            print("No hay suficientes datos para calcular el promedio semanal.")
            return None
        promedio = sum(self.temperaturas_diarias) / len(self.temperaturas_diarias)
        return promedio

# Programa principal
def main_poo():
    print("Programación Orientada a Objetos (POO)")
    registro_clima = RegistroClima()
    registro_clima.ingresar_temperaturas_diarias()
    promedio = registro_clima.calcular_promedio_semanal()
    if promedio:
        print(f"El promedio semanal de temperaturas es: {promedio}")

if __name__ == "__main__":
    main_poo()
