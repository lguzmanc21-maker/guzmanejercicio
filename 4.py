a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))

if a > b:
    print(f"{a} es mayor")
elif b > a:
    print(f"{b} es mayor")
else:
    print("Son iguales")