a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))
c = float(input("Ingrese el tercer número: "))

numeros = [a, b, c]
numeros.sort(reverse=True)

print("Ordenados de mayor a menor:", numeros)