tabla = 0
numero = 0
while tabla <= 10:
    print("La tabla del " + str(tabla))
    numero = 0
    while numero <= 10:
        print(str(tabla) + " x " + str(numero) + " = " + str(tabla*numero))
        numero += 1
    tabla += 1