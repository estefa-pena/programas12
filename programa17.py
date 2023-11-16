#Programa de una función para multiplicar una matriz por un escalar.
def multiplicar_por_escalar(matriz, escalar):
    return [[elemento * escalar for elemento in fila] for fila in matriz]
matriz_ejemplo = [
    [6, 2, 2],
    [3, 4, 7],
    [8, 1, 9]
]
escalar_ejemplo = 2
resultado_multiplicacion = multiplicar_por_escalar(matriz_ejemplo, escalar_ejemplo)
print(f"Matriz original:\n{matriz_ejemplo}")
print(f"Matriz multiplicada por {escalar_ejemplo}:\n{resultado_multiplicacion}")
