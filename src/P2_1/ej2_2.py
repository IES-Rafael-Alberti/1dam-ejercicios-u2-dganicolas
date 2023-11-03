def seguridad (contraseña):
    contaseñas = ('hola','admin','contraseña')
    if contraseña not in contaseñas :
        return "master no te la sabes"
    else:
        return "felicidades sabes la contraseña"


def main():
    contraseña = input("introduce la contraseña: ")
    print(seguridad(contraseña))


if __name__ == "__main__":
    main()