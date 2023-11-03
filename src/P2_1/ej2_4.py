def parimpar (num1):
    n1 = num1 % 2
    if n1 == 0:
        return "el numero es par"
    else:
        return "el numero es impar"

def main():
    numero1=float(input("dame un numero: "))
    print(parimpar(numero1))

if __name__ == "__main__":
    main()