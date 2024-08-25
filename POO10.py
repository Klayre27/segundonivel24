import os

class Producto:
    def __init__(self, codigo, nombre, cantidad, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

class Inventario:
    def __init__(self, archivo='inventario.txt'):
        self.archivo = archivo
        self.productos = {}
        self.cargar_inventario()

    def cargar_inventario(self):
        if os.path.exists(self.archivo):
            try:
                with open(self.archivo, 'r') as file:
                    for linea in file:
                        codigo, nombre, cantidad, precio = linea.strip().split(',')
                        self.productos[codigo] = Producto(codigo, nombre, int(cantidad), float(precio))
            except FileNotFoundError:
                print("El archivo de inventario no existe.")
            except PermissionError:
                print("No tienes permisos para leer el archivo de inventario.")
            except Exception as e:
                print(f"Error inesperado: {e}")

    def guardar_inventario(self):
        try:
            with open(self.archivo, 'w') as file:
                for producto in self.productos.values():
                    file.write(f"{producto.codigo},{producto.nombre},{producto.cantidad},{producto.precio}\n")
        except PermissionError:
            print("No tienes permisos para escribir en el archivo de inventario.")
        except Exception as e:
            print(f"Error inesperado: {e}")

    def agregar_producto(self, producto):
        if producto.codigo in self.productos:
            print("El producto ya existe en el inventario.")
        else:
            self.productos[producto.codigo] = producto
            self.guardar_inventario()
            print(f"Producto {producto.nombre} añadido correctamente.")

    def eliminar_producto(self, codigo):
        if codigo in self.productos:
            del self.productos[codigo]
            self.guardar_inventario()
            print(f"Producto con código {codigo} eliminado correctamente.")
        else:
            print("El producto no existe en el inventario.")
