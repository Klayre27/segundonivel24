# calcular_area_rectangulo.py
# Este programa calcula el área de un rectángulo dado su ancho y su alto.

def calcular_area(ancho, alto):
    """
    Calcula el área de un rectángulo.

    :param ancho: El ancho del rectángulo.
    :param alto: El alto del rectángulo.
    :return: El área del rectángulo.
    """
    return ancho * alto


def main():
    # Solicitamos al usuario que ingrese el ancho y el alto del rectángulo
    ancho = float(input("Introduce el ancho del rectángulo: "))
    alto = float(input("Introduce el alto del rectángulo: "))

    # Calculamos el área utilizando la función calcular_area
    area = calcular_area(ancho, alto)

    # Mostramos el resultado al usuario
    print(f"El área del rectángulo es: {area}")


if __name__ == "__main__":
    main()
