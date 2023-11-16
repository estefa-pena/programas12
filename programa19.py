#Programa para una lista de números encontrar el número mayor
def encontrar_numero_mayor(lista):
    return max(lista, default=None)
lista_numeros = [7, 2, 5, 1, 8, 3]
numero_mayor = encontrar_numero_mayor(lista_numeros)
if numero_mayor is not None:
    print(f"El número mayor en la lista es {numero_mayor}.")
