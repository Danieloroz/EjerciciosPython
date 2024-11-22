# Datos iniciales: diccionario con materias como claves y notas de parciales como valores
notas = {
    "Calculo": [3.5, 2.5, 1.5],
    "Química": [2.5, 3.0, 5.0],
    "Deporte": [2.4, 2.0, 2.2],
    "Lógica": [1.5, 4.0, 4.5]
}

# Función para calcular la nota final de cada materia (30%, 30%, 40%) y agregarla al diccionario
def c21_final():
    ponderaciones = [0.3, 0.3, 0.4]  # Porcentajes asignados a cada parcial
    for materia, parciales in notas.items():
        # Calcular la nota final como suma ponderada de los parciales
        nota_final = sum(parciales[i] * ponderaciones[i] for i in range(len(parciales)))
        notas[materia].append(round(nota_final, 2))  # Agregar la nota final redondeada
    print("Notas actualizadas con la nota final:")
    for materia, parciales in notas.items():
        print(f"{materia}: {parciales}")

# Función para calcular el promedio de las notas finales del estudiante
def c22_promedio():
    notas_finales = [parciales[-1] for parciales in notas.values()]  # Extraer las notas finales
    promedio = sum(notas_finales) / len(notas_finales)
    print(f"El promedio general del estudiante es: {promedio:.2f}")
    return promedio

# Llamar a las funciones y mostrar los resultados
c21_final()  # Agrega las notas finales al diccionario
c22_promedio()  # Calcula y muestra el promedio general