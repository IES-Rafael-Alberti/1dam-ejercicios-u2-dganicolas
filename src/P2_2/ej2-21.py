total = 0

while True:
    monton = float(input("Introduce el monto de la compra (o 0 para terminar): "))
    if monton < 0:
        print("El numero no puede ser negativo.")
    elif monton == 0:
        break
    else:
        total += monton
if total > 1000:
    total *= 0.9 
print("El total a pagar es:", round(total, 2))