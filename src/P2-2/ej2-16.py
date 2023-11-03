numero2 = 0
while True:
    
    numero = int(input("Introduce algun numero (escribe 0 para terminar): "))
    if numero > numero2:
        numero2 = numero
    if numero == 0:
        break
print("el numero mayor es " + str(numero2))