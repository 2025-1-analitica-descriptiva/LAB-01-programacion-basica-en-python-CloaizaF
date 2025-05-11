"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import csv


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
    dic = {}
    lista = []
    with open("files/input/data.csv", "r", newline="") as archivo_csv:
        lector = csv.reader(archivo_csv)
        for fila in lector:
            listaExtraida = fila[0].split("\t")
            if listaExtraida[0] in dic:
                dic[listaExtraida[0]].append(int(listaExtraida[1]))
            else:
                dic[listaExtraida[0]] = [int(listaExtraida[1]), int(listaExtraida[1])]
    for key in dic:
        lista.append((key, max(dic[key]), min(dic[key])))
    lista.sort()
    return lista
