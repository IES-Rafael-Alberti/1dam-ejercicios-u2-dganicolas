def depresion (explotao):
    sueldo = 2400
    if explotao < 0.4:
        sueldo= sueldo * 1 + (sueldo*(1*explotao))
        return sueldo
    elif explotao < 0.6:
        sueldo= sueldo * 2 + (1*sueldo*explotao)
        return sueldo
    else:
        sueldo= sueldo * 3 + (1*sueldo*explotao)
        return sueldo


def explotacion_laboral (explotao):
    if explotao < 0.4:
        return "tu nivel es inaceptable y tu sueldo es " + str(depresion(explotao))
    elif explotao < 0.6:
        return "tu nivel es aceptable y tu sueldo es " + str(depresion(explotao))
    else:
        return "tu nivel es meritorio y tu sueldo es " + str(depresion(explotao))
def main():
    print("el nivel de empleado va de la siguiente manera \n\ninaceptable 0.0 - 0.3 \naceptable de 0.4 - 0.5 \nmeritorio 0.6 o mas \n \n")
    puntuacion = round(float(input("pon tu puntuacion de empleado: ")),1)
    print(explotacion_laboral(puntuacion))

if __name__=="__main__":
    main()