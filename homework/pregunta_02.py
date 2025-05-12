"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import csv


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

    """
    dic = {}
    lista = []
    with open("files/input/data.csv", "r", newline="") as archivo_csv:
        lector = csv.reader(archivo_csv, delimiter="\t")
        for fila in lector:
            if fila[0] in dic:
                dic[fila[0]] += 1
            else:
                dic[fila[0]] = 1

    for key in dic:
        lista.append((key, dic[key]))
    lista.sort()
    return lista
