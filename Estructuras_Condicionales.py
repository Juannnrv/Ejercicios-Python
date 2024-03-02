anno = int(input("Ingrese un año: "))

if (anno % 4 == 0 and anno % 100 != 0) or (anno % 400 == 0):
    print(f"{anno} es bisiesto")
else:
    print(f"{anno} no es bisiesto")
