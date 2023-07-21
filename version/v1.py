#----------------------------------------------------------------------------------------------------------------------------------


#----------------------------------------------------------------------------------------------------------------------------------
import tkinter as tk
from tkinter import messagebox
import os
from PIL import Image, ImageTk

class Alumno:
    def __init__(self, nombre, matricula, curp, contacto, correo):
        self.nombre = nombre
        self.matricula = matricula
        self.curp = curp
        self.contacto = contacto
        self.correo = correo

    def guardar_archivo(self):
        ruta_escritorio = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
        nombre_archivo = f"{self.matricula}_{self.nombre}.txt"
        ruta_archivo = os.path.join(ruta_escritorio, nombre_archivo)

        with open(ruta_archivo, 'w') as archivo:
            archivo.write(f"Nombre: {self.nombre}\n")
            archivo.write(f"Matrícula: {self.matricula}\n")
            archivo.write(f"CURP: {self.curp}\n")
            archivo.write(f"Número de contacto: {self.contacto}\n")
            archivo.write(f"Correo electrónico: {self.correo}\n")

    def guardar_datos(self):
        if not self.nombre or not self.matricula or not self.curp or not self.contacto or not self.correo:
            messagebox.showwarning("Faltan datos", "Por favor, complete todos los campos.")
            return

        self.guardar_archivo()
        messagebox.showinfo("Registro exitoso", f"Se ha registrado el alumno {self.nombre}.")

    def limpiar_campos(self):
        self.nombre = ""
        self.matricula = ""
        self.curp = ""
        self.contacto = ""
        self.correo = ""

class VentanaRegistro(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Registrar Alumno")
        self.resizable(False, False)

        self.entry_nombre = None
        self.entry_matricula = None
        self.entry_curp = None
        self.entry_contacto = None
        self.entry_correo = None

        self.configurar_interfaz()

    def configurar_interfaz(self):
        # Establecer color de fondo para el encabezado
        encabezado_frame = tk.Frame(self, bg="black")
        encabezado_frame.pack(fill="x", padx=2, pady=2, expand=True)

        # Etiqueta del encabezado
        tk.Label(encabezado_frame, text="Centro de Educación Artística", font=("Helvetica", 13), fg="white", bg="black").pack()

        # Campos de entrada para los datos del alumno
        tk.Label(self, text="Nombre:").pack()
        self.entry_nombre = tk.Entry(self)
        self.entry_nombre.pack()

        tk.Label(self, text="Matrícula:").pack()
        self.entry_matricula = tk.Entry(self)
        self.entry_matricula.pack()

        tk.Label(self, text="CURP:").pack()
        self.entry_curp = tk.Entry(self)
        self.entry_curp.pack()

        tk.Label(self, text="Número de contacto:").pack()
        self.entry_contacto = tk.Entry(self)
        self.entry_contacto.pack()

        tk.Label(self, text="Correo electrónico:").pack()
        self.entry_correo = tk.Entry(self)
        self.entry_correo.pack()

        # Botón para registrar los datos del alumno
        boton_registrar = tk.Button(self, text="Registrar", command=self.guardar_datos)
        boton_registrar.pack(side=tk.LEFT, padx=5, pady=5)

        # Botón para agregar otro alumno
        boton_agregar_alumno = tk.Button(self, text="Nuevo Alumno", command=self.agregar_alumno)
        boton_agregar_alumno.pack(side=tk.LEFT, padx=5, pady=5)

        # Espacio en blanco para el logo corporativo
        espacio_blanco_frame = tk.Frame(self, bg="white")
        espacio_blanco_frame.pack(fill="both", expand=True)
        
        tk.Label(self, text="© Jorge Mera - 2023").pack()

        # Cargar imagen y establecerla al final de la ventana
        imagen = Image.open("Image/Inbal.png")
        imagen = imagen.resize((int(imagen.width * 0.03), int(imagen.height * 0.03)))
        logo = ImageTk.PhotoImage(imagen)
        label_logo = tk.Label(espacio_blanco_frame, image=logo)
        label_logo.image = logo
        label_logo.pack(pady=10)

        # Icono de la ventana
        self.iconbitmap('Image/logo.ico')

    def agregar_alumno(self):
        self.limpiar_campos()

    def guardar_datos(self):
        nombre = self.entry_nombre.get()
        matricula = self.entry_matricula.get()
        curp = self.entry_curp.get()
        contacto = self.entry_contacto.get()
        correo = self.entry_correo.get()

        try:
            # Crear instancia de la clase Alumno y guardar datos
            alumno = Alumno(nombre, matricula, curp, contacto, correo)
            alumno.guardar_datos()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def limpiar_campos(self):
        self.entry_nombre.delete(0, tk.END)
        self.entry_matricula.delete(0, tk.END)
        self.entry_curp.delete(0, tk.END)
        self.entry_contacto.delete(0, tk.END)
        self.entry_correo.delete(0, tk.END)

if __name__ == "__version1,1__":
    ventana = VentanaRegistro()
    ventana.mainloop()