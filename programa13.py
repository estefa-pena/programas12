#Programa para verificar si un caracter está en mayúsculas o en minúscula.
caracter = input("Ingrese un caracter: ")
if caracter.isupper():
    print(f"{caracter} está en mayúsculas.")
elif caracter.islower():
    print(f"{caracter} está en minúsculas.")
else:
    print(f"{caracter} no es una letra."
