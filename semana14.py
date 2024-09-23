import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
from tkcalendar import DateEntry  # Asegúrate de instalar tkcalendar

class AgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal")

        # Frame para la lista de eventos
        self.frame_eventos = tk.Frame(self.root)
        self.frame_eventos.pack(pady=10)

        # Treeview para mostrar eventos
        self.tree = ttk.Treeview(self.frame_eventos, columns=("Fecha", "Hora", "Descripción"), show='headings')
        self.tree.heading("Fecha", text="Fecha")
        self.tree.heading("Hora", text="Hora")
        self.tree.heading("Descripción", text="Descripción")
        self.tree.pack()

        # Frame para entrada de datos
        self.frame_entrada = tk.Frame(self.root)
        self.frame_entrada.pack(pady=10)

        # Campos de entrada
        tk.Label(self.frame_entrada, text="Fecha:").grid(row=0, column=0)
        self.fecha_entry = DateEntry(self.frame_entrada, width=12, background='darkblue', foreground='white', borderwidth=2)
        self.fecha_entry.grid(row=0, column=1)

        tk.Label(self.frame_entrada, text="Hora:").grid(row=1, column=0)
        self.hora_entry = tk.Entry(self.frame_entrada)
        self.hora_entry.grid(row=1, column=1)

        tk.Label(self.frame_entrada, text="Descripción:").grid(row=2, column=0)
        self.desc_entry = tk.Entry(self.frame_entrada)
        self.desc_entry.grid(row=2, column=1)

        # Botones
        self.agregar_btn = tk.Button(self.root, text="Agregar Evento", command=self.agregar_evento)
        self.agregar_btn.pack(pady=5)

        self.eliminar_btn = tk.Button(self.root, text="Eliminar Evento Seleccionado", command=self.eliminar_evento)
        self.eliminar_btn.pack(pady=5)

        self.salir_btn = tk.Button(self.root, text="Salir", command=self.root.quit)
        self.salir_btn.pack(pady=5)

    def agregar_evento(self):
        fecha = self.fecha_entry.get()
        hora = self.hora_entry.get()
        descripcion = self.desc_entry.get()

        if fecha and hora and descripcion:
            try:
                datetime.strptime(f"{fecha} {hora}", "%Y-%m-%d %H:%M")  # Validar fecha y hora
                self.tree.insert("", "end", values=(fecha, hora, descripcion))
                self.hora_entry.delete(0, tk.END)
                self.desc_entry.delete(0, tk.END)
            except ValueError:
                messagebox.showerror("Error", "Formato de fecha y hora no válido.")
        else:
            messagebox.showwarning("Advertencia", "Por favor, complete todos los campos.")

    def eliminar_evento(self):
        selected_item = self.tree.selection()
        if selected_item:
            confirm = messagebox.askyesno("Confirmar", "¿Estás seguro de que deseas eliminar este evento?")
            if confirm:
                self.tree.delete(selected_item)
        else:
            messagebox.showwarning("Advertencia", "Seleccione un evento para eliminar.")

if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaApp(root)
    root.mainloop()
