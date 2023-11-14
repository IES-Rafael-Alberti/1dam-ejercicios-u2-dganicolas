def pedirNumero():
    numero = int(input("dame un numero positivo: "))
    while numero < 0:
        numero = int(input("dame un numero positivo: "))
    return numero
def filaDePiramide(numero):
    serie="\n"
    while numero > 0:
        serie+= "*"
        numero-=1
    #serie+= "\n"
    return serie
def  piramide (numero):
    serie2=""
    contador = 1
    while numero > 0:
        serie2 =serie2 + str(filaDePiramide(contador))
        numero-=1
        contador+=1
    return serie2

def main():
    numero1 = pedirNumero()
    print(str(piramide(numero1)))
if __name__ == "__main__":
    main()
