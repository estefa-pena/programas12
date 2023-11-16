#Programa de una función que indique las dimensiones de una matriz
def obtener_dimensiones(matriz):
    filas = len(matriz)
    columnas = len(matriz[0]) if filas > 0 else 0
    return filas, columnas
matriz_ejemplo = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
dimensiones = obtener_dimensiones(matriz_ejemplo)
print(f"La matriz tiene {dimensiones[0]} filas y {dimensiones[1]} columnas.")
