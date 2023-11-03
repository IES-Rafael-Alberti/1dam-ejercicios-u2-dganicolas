numero2= 0
numero = int(input("Introduce algun numero: "))
serie= "serie => " + str(numero)
numero2+=numero
while True:
    numero = int(input("Introduce algun numero (escribe 0 para terminar): "))
    serie= serie + "+" + str(numero)
    numero2+=numero
    if numero == 0:
        break
serie= serie + "=" + str(numero2)
print(serie)