from producto import Producto

class Inventario:
    def __init__(self):
        self.productos = []
        self.id_fijo = "7564"  # ID fijo para todos los productos

    def añadir_producto(self, nombre, cantidad, precio):
        id_producto = self.id_fijo
        producto = Producto(id_producto, nombre, cantidad, precio)
        self.productos.append(producto)
        print("Producto añadido con éxito.")

    def eliminar_producto(self, id_producto):
        for p in self.productos:
            if p.get_id() == id_producto:
                self.productos.remove(p)
                print("Producto eliminado con éxito.")
                return
        print("Error: Producto no encontrado.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        for p in self.productos:
            if p.get_id() == id_producto:
                if cantidad is not None:
                    p.set_cantidad(cantidad)
                if precio is not None:
                    p.set_precio(precio)
                print("Producto actualizado con éxito.")
                return
        print("Error: Producto no encontrado.")

    def buscar_producto(self, nombre):
        resultados = [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]
        if resultados:
            for p in resultados:
                print(p)
        else:
            print("No se encontraron productos con ese nombre.")

    def mostrar_productos(self):
        if self.productos:
            for p in self.productos:
                print(p)
        else:
            print("El inventario está vacío.")
