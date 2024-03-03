num1 = int(input("Ingrese un número 1 => "))
num2 = int(input("Ingrese un número 2 => "))

suma_total = 0 # poder iniciar desde 0 

for i in range(num1 + 1, num2):
    suma_total += i # es como tener "suma_total = suma_total + i"

print(f"La suma es {suma_total}")
