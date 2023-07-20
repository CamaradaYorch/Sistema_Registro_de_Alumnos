import os
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk


class Alumno:
    def __init__(self):
        self._nombre = ""
        self._fecha = ""
        self._matricula = ""
        self._curp = ""
        self._contacto = ""
        self._correo = ""

    def get_nombre(self):
        return self._nombre

    def get_fecha(self):
        return self._fecha

    def get_matricula(self):
        return self._matricula

    def get_curp(self):
        return self._curp

    def get_contacto(self):
        return self._contacto

    def get_correo(self):
        return self._correo

    def set_nombre(self, nombre):
        self._nombre = nombre

    def set_fecha(self, fecha):
        self._fecha = fecha

    def set_matricula(self, matricula):
        self._matricula = matricula

    def set_curp(self, curp):
        self._curp = curp

    def set_contacto(self, contacto):
        self._contacto = contacto

    def set_correo(self, correo):
        self._correo = correo

    def guardar_archivo(self):
        ruta_escritorio = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
        nombre_archivo = f"{self._matricula}_{self._nombre}-{self._fecha}.txt"
        ruta_archivo = os.path.join(ruta_escritorio, nombre_archivo)

        with open(ruta_archivo, 'w') as archivo:
            archivo.write(f"Nombre: {self._nombre}\n")
            archivo.write(f"Fecha de Registro: {self._fecha}\n")
            archivo.write(f"Matrícula: {self._matricula}\n")
            archivo.write(f"CURP: {self._curp}\n")
            archivo.write(f"Número de contacto: {self._contacto}\n")
            archivo.write(f"Correo electrónico: {self._correo}\n")


class VentanaRegistro(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Registrar Alumno")
        self.geometry("350x450")
        self.resizable(False, False)
        self.alumno = Alumno()
        self.configurar_interfaz()

    def configurar_interfaz(self):
        encabezado_frame = tk.Frame(self, bg="black")
        encabezado_frame.pack(fill="x", padx=2, pady=2)

        tk.Label(encabezado_frame, text="Centro de Educación Artística", font=("Montserrat", 16), fg="white", bg="black").pack()

        tk.Label(self, text="Nombre:").pack()
        self.entry_nombre = tk.Entry(self)
        self.entry_nombre.pack()

        tk.Label(self, text="Fecha de Registro:").pack()
        self.entry_fecha = tk.Entry(self)
        self.entry_fecha.pack()

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

        boton_registrar = tk.Button(self, text="Registrar", command=self.guardar_datos)
        boton_registrar.pack(pady=10)

        boton_limpiar = tk.Button(self, text="Nuevo Alumno", command=self.agregar_alumno)
        boton_limpiar.pack(pady=10)

        imagen = Image.open("Image/Inbal.png")
        imagen = imagen.resize((150, 30))
        logo = ImageTk.PhotoImage(imagen)
        label_logo = tk.Label(self, image=logo)
        label_logo.image = logo
        label_logo.pack(pady=10)

        tk.Label(self, text="© Mortem").pack()
        self.iconbitmap('Image/logo.ico')

    def agregar_alumno(self):
        self.alumno.set_nombre("")
        self.alumno.set_fecha("")
        self.alumno.set_matricula("")
        self.alumno.set_curp("")
        self.alumno.set_contacto("")
        self.alumno.set_correo("")

        self.entry_nombre.delete(0, tk.END)
        self.entry_fecha.delete(0, tk.END)
        self.entry_matricula.delete(0, tk.END)
        self.entry_curp.delete(0, tk.END)
        self.entry_contacto.delete(0, tk.END)
        self.entry_correo.delete(0, tk.END)

    def guardar_datos(self):
        nombre = self.entry_nombre.get()
        fecha = self.entry_fecha.get()
        matricula = self.entry_matricula.get()
        curp = self.entry_curp.get()
        contacto = self.entry_contacto.get()
        correo = self.entry_correo.get()

        try:
            if not nombre or not fecha or not matricula or not curp or not contacto or not correo:
                messagebox.showwarning("Faltan datos", "Por favor, complete todos los campos.")
                return

            self.alumno.set_nombre(nombre)
            self.alumno.set_fecha(fecha)
            self.alumno.set_matricula(matricula)
            self.alumno.set_curp(curp)
            self.alumno.set_contacto(contacto)
            self.alumno.set_correo(correo)

            self.alumno.guardar_archivo()
            messagebox.showinfo("Registro exitoso", f"Se ha registrado el alumno {nombre}.")

        except Exception as e:
            messagebox.showerror("Error", str(e))


if __name__ == "__main__":
    ventana = VentanaRegistro()
    ventana.mainloop()
