def cuanto_dinero (pagame):
    if pagame < 4:
        return "tu entras gratis"
    elif pagame < 18:
        return "tu pagas 5€"
    else:
        return "tu pagas 10€"


def main():
    edad =int(input("dime tu edad: "))
    print(cuanto_dinero(edad))

if __name__=="__main__":
    main()