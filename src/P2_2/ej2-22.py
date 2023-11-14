total_pares = 0
total_impares = 0

while True:
    numero = int(input("Introduce un numero positivo (o 0 para terminar): "))
    if numero == 0:
        break
    elif numero < 0:
        print("El número no puede ser negativo. Por favor, introduce un nuevo número.")
    pares = sum(1 for digito in str(numero) if int(digito) % 2 == 0)
    impares = sum(1 for digito in str(numero) if int(digito) % 2 != 0)
    print("El numero", numero, "tiene", pares, "digitos pares y", impares, "digitos impares.")

    total_pares += pares
    total_impares += impares

print("En total, se leyeron", total_pares, "dígitos pares y", total_impares, "dígitos impares.")
