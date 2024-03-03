
estatura = float(input("Ingrese su estatura en metros: "))
peso = float(input("Ingrese su peso en kilogramos: "))
edad = int(input("Ingrese su edad en años: "))

imc = peso / (estatura * estatura)

if edad < 45:
    if imc < 22.0:
        riesgo = "bajo"
    else:
        riesgo = "medio"
else:
    if imc < 22.0:
        riesgo = "medio"
    else:
        riesgo = "alto"

print("Su condición de riesgo es:", riesgo)






