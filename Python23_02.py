lista = int(input("Ingrese la cantidad de números que desea promediar => "))
numeros = []
for i in range(lista):
    numero = float(input(f"Ingrese el número {i+1} => "))
    numeros.append(numero)

suma_total = sum(numeros)
promedio = suma_total / lista
print ("El promedio de los números ingresados es:", promedio)