def hacienda_roba_V2 (IRPF):
    if IRPF < 10000:
        return "te quito un 5% master"
    elif IRPF >= 10000 and IRPF < 20000:
        return "te quito un 15% master"
    elif IRPF >= 20000 and IRPF < 35000:
        return "te quito un 20% master"
    elif IRPF >= 35000 and IRPF < 60000:
        return "te quito un 30% master"
    else:
        return "te quito un 45% master, y me parece poco"

sueldo = int(input("pon tu sueldo y te robo una parte: "))
print(hacienda_roba_V2(sueldo))