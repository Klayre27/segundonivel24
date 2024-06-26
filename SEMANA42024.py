# Clase para representar un libro en la biblioteca
class Libro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = True

    def prestar(self):
        if self.disponible:
            self.disponible = False
            print(f'El libro "{self.titulo}" ha sido prestado.')
        else:
            print(f'El libro "{self.titulo}" no está disponible.')

    def devolver(self):
        if not self.disponible:
            self.disponible = True
            print(f'El libro "{self.titulo}" ha sido devuelto.')
        else:
            print(f'El libro "{self.titulo}" ya está en la biblioteca.')

# Clase para gestionar la biblioteca
class Biblioteca:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)
        print(f'Libro "{libro.titulo}" agregado a la biblioteca {self.nombre}.')

    def mostrar_libros_disponibles(self):
        print(f'Libros disponibles en la biblioteca {self.nombre}:')
        for libro in self.libros:
            if libro.disponible:
                print(f'Título: {libro.titulo}, Autor: {libro.autor}, ISBN: {libro.isbn}')

# Crear instancias y utilizar las clases
biblioteca = Biblioteca('Biblioteca Central')

libro1 = Libro('1984', 'George Orwell', '1234567890')
libro2 = Libro('Cien Años de Soledad', 'Gabriel García Márquez', '0987654321')

biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)

biblioteca.mostrar_libros_disponibles()

libro1.prestar()
biblioteca.mostrar_libros_disponibles()

libro1.devolver()
biblioteca.mostrar_libros_disponibles()
