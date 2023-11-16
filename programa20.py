#Programa de una función para encontrar la suma de cada fila y columna de una matriz.
def sumar_filas_columnas(matriz):
    if not matriz or not matriz[0]:
        print("La matriz está vacía.")
        return None, None
    filas = [sum(fila) for fila in matriz]
    columnas = [sum(columna) for columna in zip(*matriz)]
    return filas, columnas
matriz_ejemplo = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
sumas_filas, sumas_columnas = sumar_filas_columnas(matriz_ejemplo)
if sumas_filas is not None and sumas_columnas is not None:
    print(f"Sumas de filas: {sumas_filas}")
    print(f"Sumas de columnas: {sumas_columnas}")
