# Clase que representa un recurso ficticio
class Recurso:
    # Constructor
    def __init__(self, nombre):
        """
        Inicializa el recurso con un nombre y un estado inicial.
        El método __init__ se llama automáticamente al crear una nueva instancia de la clase.
        """
        self.nombre = nombre
        self.estado = "inicializado"
        print(f"Recurso {self.nombre} ha sido {self.estado}.")

    # Destructor
    def __del__(self):
        """
        Libera el recurso cambiando su estado.
        El método __del__ se llama automáticamente al eliminar una instancia de la clase.
        """
        self.estado = "liberado"
        print(f"Recurso {self.nombre} ha sido {self.estado}.")

# Clase que utiliza el recurso
class UsuarioDeRecurso:
    # Constructor
    def __init__(self, nombre):
        """
        Crea una instancia de UsuarioDeRecurso y una instancia de Recurso asociada.
        """
        self.nombre = nombre
        self.recurso = Recurso(nombre)
        print(f"UsuarioDeRecurso {self.nombre} ha sido creado.")

    # Destructor
    def __del__(self):
        """
        Elimina el recurso asociado antes de destruir la instancia de UsuarioDeRecurso.
        """
        print(f"UsuarioDeRecurso {self.nombre} va a ser eliminado.")
        del self.recurso

# Función principal para demostrar el uso de constructores y destructores
def main():
    usuario1 = UsuarioDeRecurso("Recurso1")
    usuario2 = UsuarioDeRecurso("Recurso2")

    print("Trabajando con recursos...")

    # Al finalizar la función, los objetos usuario1 y usuario2 serán eliminados automáticamente,
    # lo que activará sus destructores y los destructores de los recursos asociados.

if __name__ == "__main__":
    main()
