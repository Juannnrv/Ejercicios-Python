numero1 = float(input("Ingrese numero: "))
numero2 = float(input("Ingrese numero: "))
numero3 = float(input("Ingrese numero: "))
numero4 = float(input("Ingrese numero: "))

numeros_ordenados = sorted([numero1, numero2, numero3, numero4]) # sorted([]) => hay que convertir en lista para ordenar

print(*numeros_ordenados)

