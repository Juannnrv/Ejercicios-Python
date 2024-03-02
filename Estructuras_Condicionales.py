palabra1 = input("Palabra 1 => ")
palabra2 = input("Palabra 2 => ")

longitud_palabra1 = len(palabra1) # len() contar caracteres
longitud_palabra2 = len(palabra2)

if longitud_palabra1 > longitud_palabra2:
    diferencia = longitud_palabra1 - longitud_palabra2
    print(f"La palabra {palabra1} tiene {diferencia} letras más que {palabra2}.")
elif longitud_palabra2 > longitud_palabra1:
    diferencia = longitud_palabra2 - longitud_palabra1
    print(f"La palabra {palabra2} tiene {diferencia} letras más que {palabra1}.")
else:
    print("Las dos palabras tienen el mismo largo.")
