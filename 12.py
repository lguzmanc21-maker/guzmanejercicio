cantidad = int(input("Ingrese la cantidad de llantas: "))

if cantidad <= 0:
    print("Cantidad inválida")
else:
    if cantidad < 5:
        precio = 30000
    elif 5 <= cantidad <= 10:
        precio = 25000
    else:  # más de 10
        precio = 20000

    total = cantidad * precio

    print("Precio por llanta:", precio)
    print("Total a pagar:", total)