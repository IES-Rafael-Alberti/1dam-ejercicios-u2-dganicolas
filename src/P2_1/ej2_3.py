def division1 (n1,n2):
    if n2 > 0:
        n1 =n1/n2
        return n1
    else:
        return 0
def division(n1,n2):
    if n2 == 0:
        return "por 0 no se puede dividir"
    else:
        return "la division da " + str(division1(n1,n2))


def main():
    numero1=float(input("dame el numero dividendo: "))
    numero2=float(input("dame el divisor: "))
    print(division(numero1,numero2))

if __name__=="__main__":
    main()