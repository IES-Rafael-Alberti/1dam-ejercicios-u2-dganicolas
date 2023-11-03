def edaad (edad):
    if 18 <= edad:
        return"felicidades eres mayor de edad"
    elif 18 > edad:
        return"felicidades eres menor de edad"
edad = int(input("introduce tu edad: "))
while edad < 0:
    print("ERROR, los numero negativos no son edades")
    edad = int(input("introduce tu edad: "))
print(edaad(edad))