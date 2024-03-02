actual = int(input("Hora actual => "))
cantidad = int(input("Cantidad de horas => "))

futura = (actual + cantidad) % 12

print(f"En {cantidad} horas, el reloj marcará las {futura}")
