juegos_ganados_A = int(input("Juegos ganados por A: "))
juegos_ganados_B = int(input("Juegos ganados por B: "))

# Es valido ?
if juegos_ganados_A < 0 or juegos_ganados_B < 0 or abs(juegos_ganados_A - juegos_ganados_B) > 2:
    print("Invalido")
else:
    # Ha terminado el set ?
    if juegos_ganados_A < 6 and juegos_ganados_B < 6:
        print("Aun no termina")
    
    elif juegos_ganados_A >= 6 and juegos_ganados_A - juegos_ganados_B >= 2:
        print("Gano A")
    elif juegos_ganados_B >= 6 and juegos_ganados_B - juegos_ganados_A >= 2:
        print("Gano B")
    
    elif juegos_ganados_A == 6 and juegos_ganados_B == 6:
        print("Aun no termina")
    
    elif juegos_ganados_A == 5 and juegos_ganados_B == 5:
        print("Aun no termina")
        
    # Se define en un ultimo juego ?
    elif juegos_ganados_A == 7 and juegos_ganados_B == 6:
        print("Gano A")
    elif juegos_ganados_B == 7 and juegos_ganados_A == 6:
        print("Gano B")
    else:
        print("Invalido")





