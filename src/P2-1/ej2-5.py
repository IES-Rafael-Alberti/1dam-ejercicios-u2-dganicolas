def hacienda (edad,dinero):
    if edad >= 16 and dinero >= 1000:
        return "tienes que pagar el impuesto"
    else:
        return "no tienes que pagar el impuesto"
edad = int(input("dime tu edad: "))
dinero = int(input("dime tus ingresos: "))
print(hacienda(edad,dinero))