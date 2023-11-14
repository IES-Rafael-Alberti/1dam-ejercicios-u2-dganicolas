while True:
    print("\nMenú:")
    print("1 Comenzar programa")
    print("2 Imprimir listado")
    print("3 Finalizar programa")
    opcion = int(input("Elige una opcion: "))
    if opcion == 1:
        print("comenzar el programa")
    elif opcion == 2:
        print("imprimir el listado")
    elif opcion == 3:
        print("finalizar el programa")
        break
    else:
        print("Opción incorrecta. Por favor, elige una opción válida.")