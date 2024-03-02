numero1 = input("Dame un primer número => ")
numero2 = input("Dame un segundo número => ")
numero3 = input("Dame un tercer número => ")
if numero1 > numero2 and numero1 > numero3:
    print("el numero 1 es el mayor")
elif numero2 > numero1 and numero2 > numero3:
    print("el numero 2 es el mayor")
elif numero3 > numero1 and numero3 > numero2:
    print("el numero 3 es el mayor")
else:
    print("no te entiendo")