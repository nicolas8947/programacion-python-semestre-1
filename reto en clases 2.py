nota_lab_1 = float(input("¿cual es la nota 1 del lab?"))
nota_lab_2 = float(input("¿cual es la nota 1 del lab?"))
nombre_estudiante = input("¿cual es es nombre del estudiante?")
nombre_asignatura = input("¿cual es la asignatura?")
promedio = (nota_lab_1*0.3) + (nota_lab_2*0.7)
diccionario1 = dict()
datos_de_estudiante = {
    "Nombre de estudiante":"Roberto Gandolfini",
    "Nombre de la asignatura":"Historia",
    "Nota de laboratorio N°1":5.5,
    "Nota de laboratorio N°2":4.3,
    "promedio":round(promedio)
    }
print("Diccionario inicial:",datos_de_estudiante)
print(datos_de_estudiante["Nombre de estudiante"])
print(datos_de_estudiante["Nombre de la asignatura"])
print(datos_de_estudiante["Nota de laboratorio N°1"])
print(datos_de_estudiante["Nota de laboratorio N°2"])

