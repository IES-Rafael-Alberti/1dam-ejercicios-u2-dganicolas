frase = input("Introduce una frase: ")
letra = input("Introduce una letra: ")

for i in range(len(frase)):
    if frase[i] == letra:
        print("hay coincidencia ", i)
    else:
        print("No hay coincidencia ", i)