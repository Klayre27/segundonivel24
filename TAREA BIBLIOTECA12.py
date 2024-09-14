# Clase Libro
class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"{self.titulo} por {self.autor} (Categoría: {self.categoria}, ISBN: {self.isbn})"

# Clase Usuario
class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []

    def prestar_libro(self, libro):
        self.libros_prestados.append(libro)

    def devolver_libro(self, isbn):
        self.libros_prestados = [libro for libro in self.libros_prestados if libro.isbn != isbn]

    def listar_libros_prestados(self):
        return [str(libro) for libro in self.libros_prestados]

    def __str__(self):
        return f"Usuario: {self.nombre}, ID: {self.id_usuario}"

# Clase Biblioteca
class Biblioteca:
    def __init__(self):
        self.libros = {}  # Diccionario con ISBN como clave y objeto Libro como valor
        self.usuarios = {}  # Diccionario con ID de usuario como clave y objeto Usuario como valor
        self.isbns_prestados = set()  # Conjunto de ISBNs actualmente prestados

    # Añadir un libro
    def agregar_libro(self, libro):
        if libro.isbn not in self.libros:
            self.libros[libro.isbn] = libro
            print(f"Libro '{libro.titulo}' agregado a la biblioteca.")
        else:
            print("El libro ya existe en la biblioteca.")

    # Eliminar un libro
    def eliminar_libro(self, isbn):
        if isbn in self.libros and isbn not in self.isbns_prestados:
            del self.libros[isbn]
            print(f"Libro con ISBN {isbn} eliminado.")
        else:
            print("No se puede eliminar el libro porque está prestado o no existe.")

    # Registrar un usuario
    def registrar_usuario(self, usuario):
        if usuario.id_usuario not in self.usuarios:
            self.usuarios[usuario.id_usuario] = usuario
            print(f"Usuario '{usuario.nombre}' registrado.")
        else:
            print("El usuario ya está registrado.")

    # Dar de baja un usuario
    def eliminar_usuario(self, id_usuario):
        if id_usuario in self.usuarios:
            del self.usuarios[id_usuario]
            print(f"Usuario con ID {id_usuario} eliminado.")
        else:
            print("El usuario no existe.")

    # Prestar un libro
    def prestar_libro(self, id_usuario, isbn):
        if isbn in self.libros and id_usuario in self.usuarios and isbn not in self.isbns_prestados:
            libro = self.libros[isbn]
            self.usuarios[id_usuario].prestar_libro(libro)
            self.isbns_prestados.add(isbn)
            print(f"Libro '{libro.titulo}' prestado a {self.usuarios[id_usuario].nombre}.")
        else:
            print("No se puede prestar el libro.")

    # Devolver un libro
    def devolver_libro(self, id_usuario, isbn):
        if id_usuario in self.usuarios and isbn in self.isbns_prestados:
            self.usuarios[id_usuario].devolver_libro(isbn)
            self.isbns_prestados.remove(isbn)
            print(f"Libro con ISBN {isbn} devuelto por {self.usuarios[id_usuario].nombre}.")
        else:
            print("No se puede devolver el libro.")

    # Buscar libros por título, autor o categoría
    def buscar_libro(self, busqueda):
        resultados = []
        for libro in self.libros.values():
            if busqueda.lower() in libro.titulo.lower() or busqueda.lower() in libro.autor.lower() or busqueda.lower() in libro.categoria.lower():
                resultados.append(str(libro))
        if resultados:
            return "\n".join(resultados)
        return "No se encontraron libros."

    # Listar libros prestados de un usuario
    def listar_libros_prestados(self, id_usuario):
        if id_usuario in self.usuarios:
            return "\n".join(self.usuarios[id_usuario].listar_libros_prestados())
        return "Usuario no encontrado."

# Prueba del sistema de gestión de biblioteca digital
if __name__ == "__main__":
    # Crear la biblioteca
    biblioteca = Biblioteca()

    # Añadir libros
    libro1 = Libro("Cien Años de Soledad", "Gabriel García Márquez", "Novela", "1234567890")
    libro2 = Libro("El Quijote", "Miguel de Cervantes", "Clásico", "2345678901")
    biblioteca.agregar_libro(libro1)
    biblioteca.agregar_libro(libro2)

    # Registrar usuarios
    usuario1 = Usuario("Juan Pérez", "001")
    usuario2 = Usuario("Ana Gómez", "002")
    biblioteca.registrar_usuario(usuario1)
    biblioteca.registrar_usuario(usuario2)

    # Prestar libros
    biblioteca.prestar_libro("001", "1234567890")
    biblioteca.prestar_libro("002", "2345678901")

    # Listar libros prestados
    print("Libros prestados a Juan Pérez:")
    print(biblioteca.listar_libros_prestados("001"))

    # Devolver libro
    biblioteca.devolver_libro("001", "1234567890")

    # Buscar libros
    print("Buscar libro por autor 'Cervantes':")
    print(biblioteca.buscar_libro("Cervantes"))
