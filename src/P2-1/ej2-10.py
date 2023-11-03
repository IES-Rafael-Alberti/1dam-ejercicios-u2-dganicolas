def pizzeria (pizza):
    if pizza == "vegana":
        print("que ingrediente le quieres hechar a la pizza \n\npimiento   o    tofu")
        ingrediente = input("que ingredientes quieres: ")
        if ingrediente == "pimiento":
            return "tu pizza es vegana y tiene tomate, mozarella y pimiento"
        if ingrediente == "tofu":
            return "tu pizza es vegana y tiene tomate, mozarella y tofu"
        else:
            return "elige bien los ingredientes ----ERROR--- empieza de nuevo"
    if pizza == "no vegana":
        print("que ingrediente le quieres hechar a la pizza \n\nPeperoni, jamón y Salmón")
        ingrediente = input("que ingredientes quieres: ")
        if ingrediente == "jamón":
            return "tu pizza no es vegana y tiene tomate, mozarella y jamón"
        if ingrediente == "Peperoni":
            return "tu pizza no es vegana y tiene tomate, mozarella y Peperoni"
        if ingrediente == "Salmón":
            return "tu pizza no es vegana y tiene tomate, mozarella y Salmón"
        else:
            return "elige bien los ingredientes ----ERROR--- empieza de nuevo"
print("en la pizzeria tenemos dos tipos de pizaa\n veganas \n no veganas")
pizza= input("¿que pizza quieres 'vegana' o 'no vegana'?: ")
print(pizzeria(pizza))