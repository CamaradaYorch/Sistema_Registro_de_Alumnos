if __name__ == "__version1,0__":
    alumno = {
        "nombre": "",
        "matricula": "",
        "curp": "",
        "generacion": ""
    }

# Se crea un diccionario llamado "alumno" con las claves "nombre", "matricula", "curp" y "generacion"
# Inicialmente, los valores están vacíos

    print(alumno)

# Se muestra el diccionario vacío

    nombre = input("Ingresa nombre")
    matricula = input("Ingresa matricula")
    curp = input("Ingresa CURP")
    generacion = input("Ingresa generacion:")

# Se solicita al usuario que ingrese los datos del alumno

    alumno["curp"] = curp
    alumno["generacion"] = generacion
    alumno["nombre"] = nombre
    alumno["matricula"] = matricula

# Se actualizan los valores del diccionario "alumno" con los datos ingresados

    print(alumno)

# Se muestra el diccionario con los datos del alumno

    materias = ["Materia 1", "Materia 2", "Materia 3", "Materia 4", "Materia 5","Materia 6", "Materia 7","Materia 8", "Materia 9","Materia 10"]

# Se define una lista de materias

    for materia in materias:
        calficacion_materia = float(input("Califcacion"))
        alumno.update({materia: calficacion_materia})
        if calficacion_materia < 5:
            alumno["generacion"] = input("Ingresa la nueva generacion")

# Se solicita al usuario ingresar la calificación de cada materia y se actualiza el diccionario

    print(alumno)

# Se muestra el diccionario actualizado con las calificaciones y generación del alumno