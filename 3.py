a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))

if b != 0 and a % b == 0:
    print(f"{a} es múltiplo de {b}")
elif a != 0 and b % a == 0:
    print(f"{b} es múltiplo de {a}")
else:
    print("Ninguno es múltiplo del otro")