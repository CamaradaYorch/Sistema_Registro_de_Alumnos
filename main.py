#------------------------------------------------------------------

# Autor: [Jorge Mera]
# Fecha: [19/07/2023]
# Descripción: [Sistema de Registro de Alumnos]
# Versión: [1.1]

#------------------------------------------------------------------


# ▼ Importar la librería tkinter para crear la interfaz gráfica
import tkinter as tk

# ▼ Importar la función messagebox de tkinter para mostrar cuadros de diálogo
from tkinter import messagebox

# ▼ Importar la librería os para trabajar con rutas y archivos del sistema
import os

# ▼ Importar las clases Image y ImageTk de la librería PIL (Python Imaging Library)
#   para trabajar con imágenes y mostrarlas en la interfaz gráfica
from PIL import Image, ImageTk


#--------------------------------------------------------------------------------------------------

# ▼ Clase Alumno para representar la información del alumno
class Alumno:
    def __init__(self):
    # ▼ Atributos privados con prefijo de guion bajo para convención de privacidad
        self._nombre = ""      # Nombre del alumno
        self._fecha = ""       # Fecha de registro del alumno
        self._matricula = ""   # Matrícula del alumno
        self._curp = ""        # CURP (Clave Única de Registro de Población
        self._contacto = ""    # Número de contacto del alumno
        self._correo = ""      # Correo electrónico del alumno


#--------------------------------------------------------------------------------------------------

    # ▼ Getters para acceder a los atributos de manera controlada
    def get_nombre(self):
        return self._nombre         # Retorna el nombre del alumno
    def get_fecha(self):
        return self._fecha          # Retorna la fecha de registro del alumno
    def get_matricula(self):
        return self._matricula      # Retorna la matrícula del alumno
    def get_curp(self):
        return self._curp           # Retorna el CURP del alumno
    def get_contacto(self):
        return self._contacto       # Retorna el número de contacto del alumno
    def get_correo(self):
        return self._correo         # Retorna el correo electrónico del alumno


#--------------------------------------------------------------------------------------------------

    # ▼ Setters para establecer los atributos de manera controlada
    def set_nombre(self, nombre):
        self._nombre = nombre           # Establece el nombre del alumno
    def set_fecha(self, fecha): 
        self._fecha = fecha             # Establece la fecha de registro del alumno
    def set_matricula(self, matricula):
        self._matricula = matricula     # Establece la matrícula del alumno
    def set_curp(self, curp):
        self._curp = curp               # Establece el CURP del alumno
    def set_contacto(self, contacto):
        self._contacto = contacto       # Establece el número de contacto del alumno
    def set_correo(self, correo):
        self._correo = correo           # Establece el correo electrónico del alumno

#--------------------------------------------------------------------------------------------------

    def guardar_archivo(self):
    # ▼ Obtener la ruta del escritorio del usuario utilizando la variable de entorno 'USERPROFILE'
        # ▼ Se construye la ruta del escritorio al combinar 'USERPROFILE' con 'Desktop'
        ruta_escritorio = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')

        # ▼ Este método guarda la información del alumno en un archivo de texto en el escritorio del usuario.
        nombre_archivo = f"{self._matricula}_{self._nombre}-{self._fecha}.txt"   # Crea el nombre del archivo usando matrícula, nombre y fecha
        ruta_archivo = os.path.join(ruta_escritorio, nombre_archivo)             # Crea la ruta completa del archivo en el escritorio del usuario

        # ▼ Abre el archivo en modo de escritura ('w') y escribe los datos del alumno en él
        with open(ruta_archivo, 'w') as archivo:
            archivo.write(f"Nombre: {self._nombre}\n")                  # Escribe el nombre del alumno en el archivo
            archivo.write(f"Fecha de Registro: {self._fecha}\n")        # Escribe la fecha de registro del alumno en el archivo
            archivo.write(f"Matrícula: {self._matricula}\n")            # Escribe la matrícula del alumno en el archivo
            archivo.write(f"CURP: {self._curp}\n")                      # Escribe el CURP del alumno en el archivo
            archivo.write(f"Número de contacto: {self._contacto}\n")    # Escribe el número de contacto del alumno en el archivo
            archivo.write(f"Correo electrónico: {self._correo}\n")      # Escribe el correo electrónico del alumno en el archivo

#--------------------------------------------------------------------------------------------------

# ▼ Clase VentanaRegistro para la interfaz gráfica del programa
class VentanaRegistro(tk.Tk):
    def __init__(self):
        super().__init__()                  # Llama al constructor de la clase padre (tk.Tk) para inicializar la ventana
        self.title("Registrar Alumno")      # Establece el título de la ventana
        self.geometry("350x450")            # Establece las dimensiones de la ventana (ancho x alto)
        self.resizable(False, False)        # Evita que la ventana se pueda redimensionar

        # ▼ Crear instancia de la clase Alumno
        self.alumno = Alumno()              # Crea una instancia de la clase Alumno para almacenar los datos del alumno
        self.configurar_interfaz()          # Llama al método "configurar_interfaz" para establecer los elementos de la interfaz gráfica

#--------------------------------------------------------------------------------------------------

    def configurar_interfaz(self):
    # ▼ Marco para la cabecera
        encabezado_frame = tk.Frame(self, bg="black")     # Creación de un marco con fondo negro para la cabecera
        encabezado_frame.pack(fill="x", padx=2, pady=2)   # Empaqueta el marco en la ventana y lo ajusta horizontalmente

    # ▼ Etiqueta del encabezado
        # Crea una etiqueta en el marco de la cabecera con texto "Centro de Educación Artística"
        # y establece la fuente, el tamaño, el color del texto (blanco) y el fondo (negro).
        tk.Label(encabezado_frame, text="Centro de Educación Artística", font=("Montserrat", 16), fg="white", bg="black").pack()

    # ▼ Campos de entrada para los datos del alumno
        tk.Label(self, text="Nombre:").pack()               # Etiqueta "Nombre:" para el campo de entrada del nombre del alumno
        self.entry_nombre = tk.Entry(self)                  # Crea un campo de entrada para el nombre y lo almacena en una variable
        self.entry_nombre.pack()                            # Empaqueta el campo de entrada en la ventana

        tk.Label(self, text="Fecha de Registro:").pack()    # Etiqueta "Fecha de Registro:" para el campo de entrada de la fecha
        self.entry_fecha = tk.Entry(self)                   # Crea un campo de entrada para la fecha y lo almacena en una variable
        self.entry_fecha.pack()                             # Empaqueta el campo de entrada en la ventana

        tk.Label(self, text="Matrícula:").pack()            # Etiqueta "Matrícula:" para el campo de entrada de la matrícula
        self.entry_matricula = tk.Entry(self)               # Crea un campo de entrada para la matrícula y lo almacena en una variable
        self.entry_matricula.pack()                         # Empaqueta el campo de entrada en la ventana

        tk.Label(self, text="CURP:").pack()                 # Etiqueta "CURP:" para el campo de entrada de la CURP
        self.entry_curp = tk.Entry(self)                    # Crea un campo de entrada para la CURP y lo almacena en una variable
        self.entry_curp.pack()                              # Empaqueta el campo de entrada en la ventana

        tk.Label(self, text="Número de contacto:").pack()   # Etiqueta "Número de contacto:" para el campo de entrada del número de contacto
        self.entry_contacto = tk.Entry(self)                # Crea un campo de entrada para el número de contacto y lo almacena en una variable
        self.entry_contacto.pack()                          # Empaqueta el campo de entrada en la ventana

        tk.Label(self, text="Correo electrónico:").pack()   # Etiqueta "Correo electrónico:" para el campo de entrada del correo electrónico
        self.entry_correo = tk.Entry(self)                  # Crea un campo de entrada para el correo electrónico y lo almacena en una variable
        self.entry_correo.pack()                            # Empaqueta el campo de entrada en la ventana


    # ▼ Botón para registrar los datos del alumno
        # ▼ Crea un botón con texto "Registrar" y vincula el método "guardar_datos" a su acción
        boton_registrar = tk.Button(self, text="Registrar", command=self.guardar_datos)
        # ▼ Empaqueta el botón en la ventana con un relleno vertical de 10 píxeles
        boton_registrar.pack(pady=10)

    # ▼ Botón para limpiar los campos
        # ▼ Crea un botón con texto "Nuevo Alumno" y vincula el método "agregar_alumno" a su acción
        boton_limpiar = tk.Button(self, text="Nuevo Alumno", command=self.agregar_alumno)
        # ▼ Empaqueta el botón en la ventana con un relleno vertical de 10 píxele
        boton_limpiar.pack(pady=10)

#--------------------------------------------------------------------------------------------------

    # ▼ Cargar imagen y establecerla al final de la ventana
        imagen = Image.open("Image/Inbal.png")
        imagen = imagen.resize((150, 30))       # Ajustar el tamaño de la imagen según lo necesario
        logo = ImageTk.PhotoImage(imagen)       # Convierte la imagen en un objeto PhotoImage para su visualización en la interfaz gráfica
        label_logo = tk.Label(self, image=logo) # Crea una etiqueta con la imagen
        label_logo.image = logo                 # ¡Importante para evitar que la imagen se borre!
        label_logo.pack(pady=10)

        # ▼ Etiqueta con la información de derechos de autor
        tk.Label(self, text="© Mortem").pack()

        # ▼ Icono de la ventana
        self.iconbitmap('Image/logo.ico')       # Establece el ícono de la ventana utilizando el archivo "logo.ico"

#--------------------------------------------------------------------------------------------------

    # ▼ Método para limpiar los campos de entrada
    def agregar_alumno(self):
        # ▼ Limpia los campos usando los setters
        self.alumno.set_nombre("")      # Establece el atributo "nombre" del objeto Alumno como una cadena vacía
        self.alumno.set_fecha("")       # Establece el atributo "fecha" del objeto Alumno como una cadena vacía
        self.alumno.set_matricula("")   # Establece el atributo "matricula" del objeto Alumno como una cadena vacía
        self.alumno.set_curp("")        # Establece el atributo "curp" del objeto Alumno como una cadena vacía
        self.alumno.set_contacto("")    # Establece el atributo "contacto" del objeto Alumno como una cadena vacía  
        self.alumno.set_correo("")      # Establece el atributo "correo" del objeto Alumno como una cadena vacía

#--------------------------------------------------------------------------------------------------

        # ▼ Borrar el contenido de los campos de entrada
        self.entry_nombre.delete(0, tk.END)    # Borra el contenido del campo de entrada "nombre"
        self.entry_fecha.delete(0, tk.END)     # Borra el contenido del campo de entrada "fecha"
        self.entry_matricula.delete(0, tk.END) # Borra el contenido del campo de entrada "matricula"
        self.entry_curp.delete(0, tk.END)      # Borra el contenido del campo de entrada "curp"
        self.entry_contacto.delete(0, tk.END)  # Borra el contenido del campo de entrada "contacto"
        self.entry_correo.delete(0, tk.END)    # Borra el contenido del campo de entrada "correo"

#--------------------------------------------------------------------------------------------------

    # ▼ Método para guardar los datos del alumno
    def guardar_datos(self):
        # ▼ Obtener los datos usando los getters
        nombre = self.entry_nombre.get()       # Obtiene el texto ingresado en el campo "nombre"
        fecha = self.entry_fecha.get()         # Obtiene el texto ingresado en el campo "fecha"
        matricula = self.entry_matricula.get() # Obtiene el texto ingresado en el campo "matricula"
        curp = self.entry_curp.get()           # Obtiene el texto ingresado en el campo "curp"
        contacto = self.entry_contacto.get()   # Obtiene el texto ingresado en el campo "contacto"
        correo = self.entry_correo.get()       # Obtiene el texto ingresado en el campo "correo"

        try:
        # ▼ Valida los campos
            # ▼ Comprueba si alguno de los campos está vacío (si el nombre, fecha, matrícula, CURP, contacto o correo están vacíos)
            if not nombre or not fecha or not matricula or not curp or not contacto or not correo:
            # ▼ Si algún campo está vacío, muestra una advertencia en forma de mensaje emergente
                messagebox.showwarning("Faltan datos", "Por favor, complete todos los campos.")
                return

#--------------------------------------------------------------------------------------------------

        # ▼ Establecer los datos usando los setters
            # ▼ Se utilizan los métodos "set_" de la clase Alumno para establecer los valores ingresados por el usuario en los atributos correspondientes.
            self.alumno.set_nombre(nombre)          # Establece el nombre del alumno
            self.alumno.set_fecha(fecha)            # Establece la fecha de registro del alumno
            self.alumno.set_matricula(matricula)    # Establece la matrícula del alumno
            self.alumno.set_curp(curp)              # Establece el CURP del alumno
            self.alumno.set_contacto(contacto)      # Establece el número de contacto del alumno
            self.alumno.set_correo(correo)          # Establece el correo electrónico del alumno

#--------------------------------------------------------------------------------------------------

        # ▼ Guardar los datos en el archivo
            # ▼ Una vez que se han establecido todos los datos del alumno utilizando los setters,
            # ▼ se llama al método "guardar_archivo()" de la clase Alumno para crear y guardar los datos del alumno en un archivo de texto.
            self.alumno.guardar_archivo()
            # ▼ Muestra una ventana emergente con el título "Registro exitoso" y un mensaje que indica que el registro del alumno
            messagebox.showinfo("Registro exitoso", f"Se ha registrado el alumno {nombre}.")

        # ▼ En caso de que ocurra alguna excepción durante el proceso de registro,
        except Exception as e:
            # ▼ Se muestra una ventana emergente con el título "Error" y el mensaje que contiene la descripción del error (obtenida de la excepción).
            messagebox.showerror("Error", str(e))

#--------------------------------------------------------------------------------------------------


    # ▼ Programa principal
if __name__ == "__main__":
        # ▼ En esta sección del código, se crea una instancia de la clase VentanaRegistro,
    ventana = VentanaRegistro()

        # ▼ Luego, se inicia el bucle principal
        # ▼ de la aplicación llamando al método "mainloop()" de la instancia de la ventana, lo que permite
        # ▼ que la interfaz gráfica esté activa y responda a las interacciones del usuario.
    ventana.mainloop()


#--------------------------------------------------------------------------------------------------

# ▼ Clase Alumno para representar la información del alumno
    # Esta clase representa los atributos y métodos asociados con un alumno, como el nombre, la fecha de registro,
    # la matrícula, el CURP, el número de contacto y el correo electrónico.

# ▼ Getters para acceder a los atributos de manera controlada
    # Estos métodos permiten obtener los valores de los atributos del alumno de manera controlada y segura.

# ▼ Setters para establecer los atributos de manera controlada
    # Estos métodos permiten establecer los valores de los atributos del alumno de manera controlada y segura.

# ▼ Método guardar_archivo(self)
    # Este método crea un archivo de texto con el nombre del alumno, su matrícula y la fecha de registro.
    # Luego, guarda en el archivo la información del alumno, incluyendo su nombre, matrícula, CURP,
    # número de contacto y correo electrónico.

# ▼ Clase VentanaRegistro para la interfaz gráfica del programa
    # Esta clase representa la ventana principal de la interfaz gráfica del programa.
    # Aquí se definen todos los widgets y elementos que formarán parte de la ventana.

# ▼ Método configurar_interfaz(self)
    # Este método configura todos los widgets y elementos de la interfaz gráfica.
    # Crea etiquetas y campos de entrada para que el usuario ingrese los datos del alumno.
    # También agrega botones para registrar los datos y limpiar los campos de entrada.

# ▼ Método agregar_alumno(self)
    # Es0te método se activa al hacer clic en el botón "Nuevo Alumno".
    # Limpia todos los campos de entrada y establece los atributos del alumno en valores vacíos.

# ▼ Método guardar_datos(self)
    # Este método se activa al hacer clic en el botón "Registrar".
    # Obtiene los datos ingresados por el usuario en los campos de entrada y valida que todos los campos estén completos.
    # Si los campos están completos, establece los atributos del alumno con los valores ingresados y guarda los datos en un archivo.

# Programa principal
    # En esta sección, se crea una instancia de la clase VentanaRegistro y se inicia el bucle principal de la aplicación
    # para que la interfaz gráfica esté activa y responda a las interacciones del usuario.

#--------------------------------------------------------------------------------------------------