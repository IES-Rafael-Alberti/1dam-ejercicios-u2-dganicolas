def seguridad (contraseña):
    contaseñas = ('hola','admin','contraseña')
    while contraseña not in contaseñas :
        contraseña = input("introduce la contraseña correcta: ")
    if contraseña in contaseñas:
        return "felicidades sabes la contraseña"
contraseña = input("introduce la contraseña: ")
print(seguridad(contraseña))