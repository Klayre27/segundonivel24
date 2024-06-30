# Programa para gestionar información de pacientes

class Paciente:
    def __init__(self, nombre, edad, condicion_medica):
        """
        Inicializa un objeto Paciente con nombre, edad y condición médica.

        Args:
        nombre (str): El nombre del paciente.
        edad (int): La edad del paciente.
        condicion_medica (str): La condición médica del paciente.
        """
        self.nombre = nombre
        self.edad = edad
        self.condicion_medica = condicion_medica

    def __str__(self):
        """
        Devuelve una representación en string del objeto Paciente.
        """
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Condición Médica: {self.condicion_medica}"


class GestionPacientes:
    def __init__(self):
        """
        Inicializa una lista vacía de pacientes.
        """
        self.pacientes = []

    def agregar_paciente(self, paciente):
        """
        Agrega un paciente a la lista de pacientes.

        Args:
        paciente (Paciente): Objeto Paciente a agregar.
        """
        self.pacientes.append(paciente)
        print(f"Paciente {paciente.nombre} agregado.")

    def mostrar_pacientes(self):
        """
        Muestra la información de todos los pacientes en la lista.
        """
        if not self.pacientes:
            print("No hay pacientes registrados.")
        else:
            print("Lista de Pacientes:")
            for paciente in self.pacientes:
                print(paciente)

    def modificar_paciente(self, nombre, nueva_condicion_medica):
        """
        Modifica la condición médica de un paciente dado su nombre.

        Args:
        nombre (str): El nombre del paciente a modificar.
        nueva_condicion_medica (str): La nueva condición médica del paciente.
        """
        paciente_encontrado = False
        for paciente in self.pacientes:
            if paciente.nombre == nombre:
                paciente.condicion_medica = nueva_condicion_medica
                paciente_encontrado = True
                print(f"Condición médica de {paciente.nombre} modificada.")
                break

        if not paciente_encontrado:
            print(f"No se encontró al paciente {nombre}.")


# Ejemplo de uso:
if __name__ == "__main__":
    # Crear una instancia de GestionPacientes
    gestion_pacientes = GestionPacientes()

    # Agregar pacientes
    paciente1 = Paciente("Juan Pérez", 35, "Diabetes")
    paciente2 = Paciente("María García", 28, "Hipertensión")
    gestion_pacientes.agregar_paciente(paciente1)
    gestion_pacientes.agregar_paciente(paciente2)

    # Mostrar la lista de pacientes
    gestion_pacientes.mostrar_pacientes()

    # Modificar la condición médica de un paciente
    gestion_pacientes.modificar_paciente("Juan Pérez", "Hipotiroidismo")

    # Mostrar la lista de pacientes actualizada
    gestion_pacientes.mostrar_pacientes()
