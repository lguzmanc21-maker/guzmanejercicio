nota = int(input("Ingrese una nota entre 0 y 10: "))

notas = ["cero", "uno", "dos", "tres", "cuatro",
         "cinco", "seis", "siete", "ocho", "nueve", "diez"]

if 0 <= nota <= 10:
    print(notas[nota])
else:
    print("Nota inválida")