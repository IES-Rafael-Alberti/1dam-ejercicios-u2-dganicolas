def años (edad):
    eda = 0
    edad2= "has cumplido " +str(eda) + "años"
    cont=0
    while cont < edad:
        eda+=1
        edad2= edad2+"\n"+ "has cumplido " +str(eda) + "años"
        cont+=1
    return(edad2)
def main():
    AA= int(input("dime tu edad: "))
    print(años(AA))
if __name__ == "__main__":
    main()
