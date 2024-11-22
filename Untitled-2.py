# Datos iniciales: nombre de la materia y las notas de los parciales
notas = [
    ["Calculo", 3.5, 2.5, 1.5],
    ["Química", 2.5, 3.0, 5.0],
    ["Deporte", 2.4, 2.0, 2.2],
    ["Lógica", 1.5, 4.0, 4.5]
]

# Función para calcular la nota final de cada materia (ponderación: 30%, 30%, 40%)
def c11_final():
    ponderaciones = [0.3, 0.3, 0.4]  # Porcentajes asignados a cada parcial
    for fila in notas:
        # Calcular la nota final como suma ponderada de los parciales
        nota_final = sum(fila[i + 1] * ponderaciones[i] for i in range(3))
        fila.append(round(nota_final, 2))  # Agregar la nota final redondeada
    print("Notas actualizadas con la nota final:")
    for fila in notas:
        print(fila)

# Función para calcular el promedio de las notas finales del estudiante
def c12_promedio():
    notas_finales = [fila[-1] for fila in notas]  # Extraer las notas finales
    promedio = sum(notas_finales) / len(notas_finales)
    print(f"El promedio general del estudiante es: {promedio:.2f}")
    return promedio

# Llamar a las funciones y mostrar los resultados
c11_final()  # Agrega las notas finales a la matriz
c12_promedio()  # Calcula y muestra el promedio general