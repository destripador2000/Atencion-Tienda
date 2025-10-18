import customtkinter as ctk
from tkinter import messagebox
from customer_queue import CustomerQueue


class CustomerApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Gestión de Clientes")
        self.geometry("500x400")
        self.resizable(False, False)

        # Crear instancia de la cola
        self.queue = CustomerQueue()

        # Configurar la ventana principal
        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("blue")

        # Frame principal
        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.pack(pady=20, padx=20, fill="both", expand=True)

        # Título
        self.title_label = ctk.CTkLabel(self.main_frame, text="Menú Principal", font=("Arial", 20, "bold"))
        self.title_label.pack(pady=10)

        # Botones del menú
        self.add_button = ctk.CTkButton(self.main_frame, text="Agregar Cliente", command=self.open_add_window)
        self.add_button.pack(pady=5)

        self.serve_button = ctk.CTkButton(self.main_frame, text="Atender Cliente", command=self.serve_customer)
        self.serve_button.pack(pady=5)

        self.show_button = ctk.CTkButton(self.main_frame, text="Mostrar Cola", command=self.open_show_window)
        self.show_button.pack(pady=5)

        self.delete_button = ctk.CTkButton(self.main_frame, text="Eliminar Cliente", command=self.open_delete_window)
        self.delete_button.pack(pady=5)

        self.exit_button = ctk.CTkButton(self.main_frame, text="Salir", fg_color="red", hover_color="#b30000", command=self.destroy)
        self.exit_button.pack(pady=10)

    # --- Ventana para agregar cliente ---
    def open_add_window(self):
        window = ctk.CTkToplevel(self)
        window.title("Agregar Cliente")
        window.geometry("350x200")

        label = ctk.CTkLabel(window, text="Ingrese el nombre del cliente:")
        label.pack(pady=10)

        entry = ctk.CTkEntry(window, placeholder_text="Nombre del cliente")
        entry.pack(pady=10)

        def add_action():
            name = entry.get().strip()
            if not name.replace(" ", "").isalpha():
                messagebox.showwarning("Error", "El nombre solo puede contener letras.")
            else:
                self.queue.add_customer(name)
                messagebox.showinfo("Éxito", f"Has agregado a {name} como cliente.")
                window.destroy()

        add_btn = ctk.CTkButton(window, text="Agregar", command=add_action)
        add_btn.pack(pady=10)

    # --- Atender cliente ---
    def serve_customer(self):
        if not self.queue.queue:
            messagebox.showinfo("Atención", "No hay clientes en espera.")
        else:
            customer = self.queue.queue.pop(0)
            messagebox.showinfo("Atención", f"Has atendido al cliente {customer.Name}.")

    # --- Ventana para mostrar la cola ---
    def open_show_window(self):
        window = ctk.CTkToplevel(self)
        window.title("Lista de Clientes en Espera")
        window.geometry("400x300")

        if not self.queue.queue:
            label = ctk.CTkLabel(window, text="No hay clientes en la cola.")
            label.pack(pady=20)
        else:
            text_box = ctk.CTkTextbox(window, width=350, height=250)
            text_box.pack(pady=10)
            text_box.configure(state="normal")
            text_box.delete("1.0", "end")
            for c in self.queue.queue:
                text_box.insert("end", f"ID: {c.ID_Customer} | Nombre: {c.Name}\n")
            text_box.configure(state="disabled")

    # --- Ventana para eliminar cliente ---
    def open_delete_window(self):
        window = ctk.CTkToplevel(self)
        window.title("Eliminar Cliente")
        window.geometry("350x200")

        label = ctk.CTkLabel(window, text="Ingrese el ID del cliente a eliminar:")
        label.pack(pady=10)

        entry = ctk.CTkEntry(window, placeholder_text="ID del cliente")
        entry.pack(pady=10)

        def delete_action():
            try:
                customer_id = int(entry.get())
                for c in self.queue.queue:
                    if c.ID_Customer == customer_id:
                        self.queue.queue.remove(c)
                        messagebox.showinfo("Eliminado", f"Has eliminado al cliente {c.Name}.")
                        window.destroy()
                        return
                messagebox.showwarning("Error", "No se encontró un cliente con ese ID.")
            except ValueError:
                messagebox.showwarning("Error", "Debes ingresar un número válido para el ID.")

        delete_btn = ctk.CTkButton(window, text="Eliminar", command=delete_action)
        delete_btn.pack(pady=10)


if __name__ == "__main__":
    app = CustomerApp()
    app.mainloop()
