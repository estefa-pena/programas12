#Programa para calcular el producto punto
def producto_punto(vector1, vector2):
    return sum(a * b for a, b in zip(vector1, vector2))
# Ejemplo de uso
vector1 = [2, 3]
vector2 = [4, -1]
resultado = producto_punto(vector1, vector2)
print(f"El producto punto de los vectores {vector1} y {vector2} es: {resultado}")
