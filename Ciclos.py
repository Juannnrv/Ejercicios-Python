for i in range(1, 11): # i son filas
    
    fila = [] # imprimir en formato de lista

    for j in range(1, 11): # j son columnas
        producto = i * j
        fila.append(producto) # agrego el resultado de la multiplicación a la lista
    
    print(" ".join(f"{num: >3}" for num in fila)) # con .join dejamos un espacio entre cada número

    # ">" sangría a la derecha

