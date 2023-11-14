def dinero(amount, interest, años):
    cont= 0
    año= 1
    serie2=""
    while años > cont:
        amount *= 1 + interest / 100
        serie= "el año " + str(año) + " has conseguido esto " + str(round(amount,2)) + " €"
        serie2 = serie2 + serie +"\n"
        cont +=1
        año +=1
    return serie2
def main():
    amount= int(input("cantidad a invertir: "))
    interest= float(input("Interes porcentual anual: "))
    años= int(input("cuantos años: "))
    print(dinero(amount,interest,años))
if __name__ == "__main__":
    main()