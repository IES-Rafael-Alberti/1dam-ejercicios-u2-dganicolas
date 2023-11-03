numero2= 0
while True:
    numero = int(input("Introduce algun numero (escribe 0 para terminar): "))
    numero2+=numero
    if numero == 0:
        break

print("la suma total es " + str(numero2))