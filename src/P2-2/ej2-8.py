def triangulo(n):
    for i in range(1, n+1, 2):
        for j in range(i, 0, -2):
            print(j, end=' ')
        print()

num = int(input("Introduce un número entero: "))
triangulo(num)