caracter = input("Ingrese el caracter => ")

if caracter.isdigit(): # isdigit() => número
    print("Es un número")
    
    #isalpha() => letra
elif caracter.isalpha() and caracter.islower(): # islower() => minuscula
    print("Es una letra minúscula")
elif caracter.isalpha() and caracter.isupper(): #isupper() => mayuscula
    print("Es una letra mayúscula")
else:
    print("No es letra ni número")


