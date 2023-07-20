# PROYECTO FASE II
------------------------------------------------------------------------------------
# Sistema de Registro de Alumnos

Este es un programa sencillo para registrar información de alumnos del CEDART. 
El programa utiliza una interfaz gráfica creada con Tkinter para facilitar el 
ingreso de los datos y guardarlos en un archivo de texto.

## Instalación

Asegúrate de tener Python 3.11.4 instalado en tu sistema.

```bash
pip install pillow
```

## Uso

```python
Para utilizar el sistema de registro de alumnos, sigue los siguientes pasos:
Importar el módulo en tu programa para acceder a las clases y funciones necesarias:

#-----------------------------------------------------------------------------------

import os
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import main

#-----------------------------------------------------------------------------------

# Clase Alumno y VentanaRegistro aquí

if __name__ == "__main__":
    ventana = VentanaRegistro()
    ventana.mainloop()

#-----------------------------------------------------------------------------------
Completar los campos de entrada con la información del alumno: nombre, fecha de registro, 
matrícula, CURP, número de contacto y correo electrónico.

Guardar la información del alumno haciendo clic en el botón "Registrar". 
Los datos del alumno se guardarán automáticamente en un archivo de texto
en el escritorio del usuario.

Si deseas agregar un nuevo alumno, haz clic en el botón "Nuevo Alumno" 
para limpiar los campos de entrada y poder ingresar los datos de otro alumno.

Es importante destacar que el programa utiliza la librería Tkinter 
para crear la interfaz gráfica y la librería PIL (Python Imaging Library) 
para trabajar con imágenes. Asegúrate de tener instaladas estas librerías 
antes de ejecutar el programa.

El sistema de registro de alumnos está diseñado para ser sencillo de usar
y permite guardar la información de los alumnos en un archivo de texto 
de forma organizada y fácil de leer. 


```

## Contribuir

¡Las contribuciones son bienvenidas! Si deseas realizar cambios importantes en el sistema de registro de alumnos, por favor abre un "issue" primero para discutir lo que te gustaría cambiar.


## Licencia

[MIT](https://choosealicense.com/licenses/mit/)


___________________________________________________________________________________________________

                                Jorge Mera aka Jorge Mortem

---------------------------------------------------------------------------------------------------
