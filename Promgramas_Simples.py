nota_certamen1 = float(input("Ingrese nota certamen 1: "))
nota_certamen2 = float(input("Ingrese nota certamen 2: "))
nota_laboratorio = float(input("Ingrese nota laboratorio: "))

promedio_certamenes = (nota_certamen1 + nota_certamen2) / 2

nota_necesaria_certamen3 = (60 * 3 - promedio_certamenes * 0.7 - nota_laboratorio * 0.3)

print("Necesita nota", nota_necesaria_certamen3, "en el certamen 3")
