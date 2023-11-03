def explotacion_laboral (explotao):
    sueldo = 2400
    if explotao < 0.4:
        sueldo= sueldo * 1 + (sueldo*(1*explotao))
        return "tu nivel es inaceptable y tu sueldo es " + str(sueldo)
    elif explotao < 0.6:
        sueldo= sueldo * 2 + (1*sueldo*explotao)
        return "tu nivel es aceptable y tu sueldo es " + str(sueldo)
    else:
        sueldo= sueldo * 3 + (1*sueldo*explotao)
        return "tu nivel es meritorio y tu sueldo es " + str(sueldo)

print("el nivel de empleado va de la siguiente manera \n\ninaceptable 0.0 - 0.3 \naceptable de 0.4 - 0.5 \nmeritorio 0.6 o mas \n \n")
puntuacion = round(float(input("pon tu puntuacion de empleado: ")),1)
print(explotacion_laboral(puntuacion))