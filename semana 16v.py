import tkinter as tk
from tkinter import messagebox

class TaskManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Tareas")

        # Variable para la entrada de tareas
        self.task_var = tk.StringVar()

        # Interfaz de usuario
        self.create_widgets()
        self.bind_shortcuts()

    def create_widgets(self):
        # Campo de entrada para nuevas tareas
        entry = tk.Entry(self.root, textvariable=self.task_var, width=40)
        entry.pack(pady=10)

        # Botones
        add_button = tk.Button(self.root, text="Añadir Tarea", command=self.add_task)
        add_button.pack(pady=5)

        complete_button = tk.Button(self.root, text="Marcar como Completada", command=self.complete_task)
        complete_button.pack(pady=5)

        delete_button = tk.Button(self.root, text="Eliminar Tarea", command=self.delete_task)
        delete_button.pack(pady=5)

        # Lista de tareas
        self.task_listbox = tk.Listbox(self.root, selectmode=tk.SINGLE, width=50, height=10)
        self.task_listbox.pack(pady=10)

    def bind_shortcuts(self):
        # Atajos de teclado
        self.root.bind("<Return>", lambda event: self.add_task())
        self.root.bind("<c>", lambda event: self.complete_task())
        self.root.bind("<Delete>", lambda event: self.delete_task())
        self.root.bind("<Escape>", lambda event: self.root.quit())

    def add_task(self):
        task = self.task_var.get().strip()
        if task:
            self.task_listbox.insert(tk.END, task)
            self.task_var.set("")  # Limpiar entrada
        else:
            messagebox.showwarning("Advertencia", "Por favor ingrese una tarea.")

    def complete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            task = self.task_listbox.get(selected_index)
            self.task_listbox.delete(selected_index)
            self.task_listbox.insert(selected_index, f"{task} ✔️")  # Marcar tarea como completada
        except IndexError:
            messagebox.showwarning("Advertencia", "Por favor seleccione una tarea.")

    def delete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(selected_index)
        except IndexError:
            messagebox.showwarning("Advertencia", "Por favor seleccione una tarea.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManager(root)
    root.mainloop()
