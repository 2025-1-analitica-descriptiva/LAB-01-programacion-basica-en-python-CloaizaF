"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import csv


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """
    dic = {}
    lista = []
    with open("files/input/data.csv", "r", newline="") as archivo_csv:
        lector = csv.reader(archivo_csv, delimiter='\t')
        for fila in lector:
            letras = fila[4].split(",")
            for letra in letras:
                    clave, valor = letra.split(":")
                    if clave in dic:
                        dic[clave].append(int(valor))
                    else:
                        dic[clave] = [int(valor)]
    for key in dic:
        lista.append((key, min(dic[key]), max(dic[key])))
    lista.sort()
    return lista
