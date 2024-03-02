from time import localtime

print ("Ingrese su fecha de nacimiento")
dia_nacimiento = int(input("Día => "))
mes_nacimiento = int(input("Mes => "))
anno_nacimiento = int(input("Año => "))

# Obtener la fecha actual
fecha_actual = localtime()

# Obtener el día, mes y año actuales
dia_actual = fecha_actual.tm_mday
mes_actual = fecha_actual.tm_mon
anno_actual = fecha_actual.tm_year

edad = anno_actual - anno_nacimiento

if mes_actual < mes_nacimiento or (mes_actual == mes_nacimiento and dia_actual < dia_nacimiento):
    edad -= 1

print("Usted tiene", edad, "años.")




