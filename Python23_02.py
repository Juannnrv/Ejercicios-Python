num = int(input("¿Cuantas series de Fibonacci requieres? =>"))
a, b = 0, 1
print("Serie de Fibonacci")
print(a)
for i in range(1, num):
    next_term = a + b
    print(next_term)
    a, b = b, next_term