num = int(input("Ingrese un número de tres cifras: "))

num_abs = abs(num)  # por si es negativo

if 100 <= num_abs <= 999:
    centenas = num_abs // 100
    unidades = num_abs % 10

    if centenas == unidades:
        print("Es capicúa")
    else:
        print("No es capicúa")
else:
    print("No es un número de tres cifras")