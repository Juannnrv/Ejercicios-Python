dividiendo = int(input("Dividiendo => "))
divisor = int(input("Divisor => "))

cociente = dividiendo // divisor
residuo = dividiendo % divisor

if residuo == 0:
    print("La división es exacta")
else:
    print("La división no es exacta")

print(f"Cociente => {cociente}")
print(f"Residuo => {residuo}")