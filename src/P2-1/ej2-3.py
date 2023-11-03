def division(n1,n2):
    if n2 == 0:
        return "por 0 no se puede dividir"
    else:
        n1= n1/n2
        return "la division da " + str(n1)

numero1=float(input("dame el numero dividendo: "))
numero2=float(input("dame el divisor: "))
print(division(numero1,numero2))