print("Vamos a ver cuales son los números pares e impares")
num = int(input("Dame un número => "))
x = num % 2
if x == 0:
    print("El número que me diste es par")
else:
    print("El número que me diste es impar")