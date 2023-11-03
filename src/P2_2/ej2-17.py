numero = int(input("Introduce un numero positivo: "))
suma = sum(int(digito) for digito in str(numero))
print("La suma de los digitos es:", suma)