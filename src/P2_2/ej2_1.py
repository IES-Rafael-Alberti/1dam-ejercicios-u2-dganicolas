def palabr(palabra):
    cont= 0
    palabra2=""
    while cont < 10:
        cont= cont + 1
        palabra2=palabra+"\n"+palabra2
    return palabra2
def main():
    palabra= input("dame una palabra: ")
    print(palabr(palabra))
if __name__ == "__main__":
    main()