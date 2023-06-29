# Archivos [Python]
# Ejemplos de clase

# Autor: Inove Coding School
# Version: 2.2

import csv


def altura_promedio(genero):
    print("¡Ejemplo integrador!")
    # Esta función recibe el género del cual
    # se debe calcular la altura promedio
    # puede ser --> femenino o masculino

    # Utilizar el archivo CSV "alturas",
    # el cual posee dos columnas:
    # - genero
    # - altura

    # Profe:
    # - Leer el archivo CSV
    # - Recorrer todas las filas del archivo CSV
    # - En cada iteración obtenga la altura del genero objetivo
    # - Acumule el valor y la cantidad para realizar
    #   el promedio al terminar el bucle

    # --- Comience aquí a desarrollar su código ---
    total_altura = 0
    cant_personas = 0
    with open("alturas.csv") as csvfile:
        alturas = list(csv.DictReader(csvfile))

    for i in range(len(alturas)):
        if alturas[i].get("genero") == genero:
            total_altura += float(alturas[i].get("altura"))
            cant_personas += 1
    if cant_personas > 0:
        promedio = total_altura / cant_personas
        print("Total Altura: ", total_altura)
        print(f"Cant. Personas del genero {genero} es: {cant_personas} ")
        print("Promedio es: ", promedio)
    else:
        print("Algo paso...")






if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    genero = str(input("Ingresa el genero: ")).lower()
    altura_promedio(genero)
