import math

radio = float(input("Ingrese el radio => "))

perimetro = 2 * math.pi * radio
área = math.pi * radio ** 2

predondeado = round(perimetro, 1)
areadondeda = round(área, 1)

print(f"Perimetro =>{predondeado}")
print(f"Área =>{areadondeda}")