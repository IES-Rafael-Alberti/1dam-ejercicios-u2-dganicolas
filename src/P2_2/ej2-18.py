cont= 0

while True:
    numero = int(input("Introduce un numero positivo (-1 para terminar): "))
    if numero == -1:
        break
    elif numero < 0:
        print("Por favor, introduce un numero entero positivo.")
    suma = sum(int(digito) for digito in str(numero))
    print("La suma de los dígitos es:", suma)
    if numero % 2 == 0:
        cont += 1
print("Has introducido", cont, "números pares.")