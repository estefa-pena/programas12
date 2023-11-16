#Programa para ingresar ángulos de un triángulo y verifique si es válido o no.
angulo1 = float(input("Ingrese el primer ángulo: "))
angulo2 = float(input("Ingrese el segundo ángulo: "))
angulo3 = float(input("Ingrese el tercer ángulo: "))
if angulo1 + angulo2 + angulo3 == 180:
    print("Los ángulos ingresados forman un triángulo válido.")
else:
    print("Los ángulos ingresados no forman un triángulo válido.")
