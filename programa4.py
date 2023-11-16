#programa para verificar si el triángulo es equilatero, isósceles o escaleno
lado1 = float(input("Longitud del primer lado: "))
lado2 = float(input("Longitud del segundo lado: "))
lado3 = float(input("Longitud del tercer lado: "))
if lado1 == lado2 == lado3:
    print("Equilátero.")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("Isósceles.")
else:
    print("Escaleno.")
