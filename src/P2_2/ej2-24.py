def es_primo(n):
    if n < 2: # 0 y 1 no son primos
        return False
    for i in range(2, n): # comprobar divisibilidad desde 2 hasta n-1
        if n % i == 0: # si n es divisible por i, no es primo
            return False
    return True # si no se encontró ningún divisor, es primo

contador_primos = 0

while True:
    numero = int(input("Introduce un número mayor que 1 (o 0 para terminar): "))
    if numero == 0:
        break
    elif numero < 2:
        print("El número debe ser mayor que 1. Por favor, introduce un nuevo número.")
        continue

    if es_primo(numero):
        contador_primos += 1

print("Has introducido", contador_primos, "números primos.")
