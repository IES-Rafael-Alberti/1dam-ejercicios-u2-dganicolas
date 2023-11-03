lineas = 0
digitos = 0

while True:
    titulo = input("Introduce el título de un libro (o '*' para terminar, '/' para nueva línea): ")
    if titulo == '*':
        break
    elif titulo == '/':
        print("La línea actual contiene", digitos, "dígitos numéricos.")
        digitos = 0
        lineas += 1
    else:
        digitos += sum(1 for caracter in titulo if caracter.isdigit())

if digitos > 0:
    print("La línea actual contiene", digitos, "dígitos numéricos.")
    lineas += 1

print("Se ingresaron", lineas, "líneas completas.")
