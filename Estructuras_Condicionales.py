operando1 = float(input("Operando 1: "))
operador = input("Operador (+, -, *, /): ")
operando2 = float(input("Operando 2: "))

if operador == "+":
    resultado = operando1 + operando2
elif operador == "-":
    resultado = operando1 - operando2
elif operador == "*":
    resultado = operando1 * operando2
elif operador == "/":
    if operando2 != 0:  # operar la división por cero
        resultado = operando1 / operando2
    else:
        print("Error: No se puede dividir por cero.")
        resultado = None
else:
    print("Error: Operador inválido.")
    resultado = None

if resultado is not None:
    print(f"Resultado: {resultado}")



