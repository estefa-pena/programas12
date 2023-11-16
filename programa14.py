#Programa para que dado el número del mes, indique el número de días del mes
numero_mes = int(input("Ingrese el número del mes (1-12): "))
dias_en_mes = 0
if 1 <= numero_mes <= 12:
    if numero_mes in [1, 3, 5, 7, 8, 10, 12]:
        dias_en_mes = 31
    elif numero_mes == 2:
        dias_en_mes = 28
    else:
        dias_en_mes = 30
    print(f"El mes {numero_mes} tiene {dias_en_mes} días.")
else:
    print("Número de mes no válido. Debe estar entre 1 y 12.")
