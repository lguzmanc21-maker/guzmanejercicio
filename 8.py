dia = int(input("Día: "))
mes = int(input("Mes: "))
anio = int(input("Año: "))

dia += 1

if dia > 30:
    dia = 1
    mes += 1

if mes > 12:
    mes = 1
    anio += 1

print(f"La fecha siguiente es: {dia}/{mes}/{anio}")