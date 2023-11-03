# a b c d e f g h i l m n ñ o p q r s t u v w x y z
#Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. 
#El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto. 
#Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.
#grupo a hombres de ñ - z
#grupo a mujeres de a - l
def grupo(sexo,nombre):
    nombre = nombre.replace("","")[0]
    lista_a_HOMBRES = ["ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    lista_a_MUJERES = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "l"]
    if sexo == "hombre" and nombre in lista_a_HOMBRES :
        return "perteneces al grupo A"
    elif sexo == "mujer" and nombre in lista_a_MUJERES: 
        return "perteneces al grupo A"
    else:
        return "perteneces al grupo B"

nombre = input("introduce tu nombre: ")
sexo = input("introduce tu sexo(hombre/mujer): ")
print(grupo(sexo,nombre))