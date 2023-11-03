def es_primo(n):
    if n < 2: # 0 y 1 no son primos
        return False
    for i in range(2, n): # comprobar divisibilidad desde 2 hasta n-1
        if n % i == 0: # si n es divisible por i, no es primo
            return False
    return True # si no se encontró ningún divisor, es primo

num = int(input("Introduce un número entero: "))
if es_primo(num):
    print(num, "es un número primo.")
else:
    print(num, "no es un número primo.")