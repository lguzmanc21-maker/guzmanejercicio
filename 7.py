dia = int(input("Día: "))
mes = int(input("Mes: "))
anio = int(input("Año: "))

if mes < 1 or mes > 12:
    print("Fecha incorrecta")
else:
    if mes in [1,3,5,7,8,10,12]:
        if 1 <= dia <= 31:
            print("Fecha correcta")
        else:
            print("Fecha incorrecta")
    elif mes in [4,6,9,11]:
        if 1 <= dia <= 30:
            print("Fecha correcta")
        else:
            print("Fecha incorrecta")
    elif mes == 2:
        if 1 <= dia <= 28:
            print("Fecha correcta")
        else:
            print("Fecha incorrecta")