print("Vamos a ver cuales números son primos")
num = int(input("Dame un número => "))
if num <= 1:
    print("El número debe ser mayor que 1.")
else:
    es_primo = True
    for i in range(2, num):
        if num % i == 0:
            es_primo = False
if es_primo:
    print(f"num es un número primo")
else:
    print(f"no es un número pirmo")
