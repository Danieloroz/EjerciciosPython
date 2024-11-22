# Datos iniciales: diccionario de diccionarios con parciales como claves
notas = {
    "Calculo": {"pp": 3.5, "sp": 2.5, "tp": 1.5},
    "Química": {"pp": 2.5, "sp": 3.0, "tp": 5.0},
    "Deporte": {"pp": 2.4, "sp": 2.0, "tp": 2.2},
    "Lógica": {"pp": 1.5, "sp": 4.0, "tp": 4.5}
}

# Función para calcular la nota final de cada materia (30%, 30%, 40%) y agregarla al diccionario
def c31_final():
    ponderaciones = {"pp": 0.3, "sp": 0.3, "tp": 0.4}  # Porcentajes asignados a cada parcial
    for materia, parciales in notas.items():
        # Calcular la nota final como suma ponderada de los parciales
        nota_final = sum(parciales[parcial] * ponderacion for parcial, ponderacion in ponderaciones.items())
        notas[materia]["final"] = round(nota_final, 2)  # Agregar la nota final redondeada
    print("Notas actualizadas con la nota final:")
    for materia, parciales in notas.items():
        print(f"{materia}: {parciales}")

# Función para calcular el promedio de las notas finales del estudiante
def c32_promedio():
    notas_finales = [parciales["final"] for parciales in notas.values()]  # Extraer las notas finales
    promedio = sum(notas_finales) / len(notas_finales)
    print(f"El promedio general del estudiante es: {promedio:.2f}")
    return promedio

# Llamar a las funciones y mostrar los resultados
c31_final()  # Agrega las notas finales al diccionario
c32_promedio()  # Calcula y muestra el promedio general