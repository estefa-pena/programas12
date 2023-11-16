#Programa para ingresar cualquier caracter y verifique si es vocal o consonante
caracter = input("Ingresa un caracter: "
if caracter in "aeiouAEIOU":
    print(f"{caracter} es una vocal.")
else:
    print(f"{caracter} es una consonante.")
