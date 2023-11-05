def impar (numero):
    while numero < 0:
        numero = int(input("dame un numero positivo: "))
    cont = 0
    serie = "impar => 0"
    num = 1
    while cont < numero:
        divisor = num%2
        if divisor == 1:
            serie= serie + "," + str(num)
        cont+=1
        num+=1
    return serie
def main():
    numero = int(input("dame un numero positivo"))
    print(impar(numero))
if __name__ == "__main__":
    main()
