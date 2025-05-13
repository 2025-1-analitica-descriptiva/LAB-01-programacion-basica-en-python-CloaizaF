"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import csv

def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
    dic = {}
    with open("files/input/data.csv", "r", newline="") as archivo_csv:
        lector = csv.reader(archivo_csv, delimiter="\t")
        for fila in lector:
            letraC1 = fila[0]
            letras = fila[4].split(",")
            for letra in letras:
                clave, valor = letra.split(":")
                if letraC1 in dic:
                    dic[letraC1] += int(valor)
                else:
                    dic[letraC1] = int(valor)
    myKeys = list(dic.keys())
    myKeys.sort()
    dic = {i: dic[i] for i in myKeys}
    return dic

if __name__ == "__main__":
    print(pregunta_12())