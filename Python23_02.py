num =int(input("¿Qué tabla de multiplicar quieres generar? =>"))
for t in range(1, 11):
    tabla = num * t
    print(f"{num} * {t} = {tabla}")