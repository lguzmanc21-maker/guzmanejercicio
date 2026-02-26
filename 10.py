compra = float(input("Ingrese el valor de la compra: "))

if compra > 300000:
    descuento = compra * 0.20
    total = compra - descuento
else:
    total = compra

print("Total a pagar:", total)