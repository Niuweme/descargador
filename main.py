while(True):
    print("Elija una opcion:")
    print("1. descargar video de YouTube")
    print("2. descargar audio de YouTube")
    print("3. decargar una playlist de YouTube")
    print("4. salir")
    opcion = input("Ingrese el numero de la opcion deseada: ")
    if opcion == "1":
        print("Descargando video...")
    elif opcion == "2":
        print("Descargando audio...")
    elif opcion == "3":
        print("Descargando playlist...")
    elif opcion == "4":
        print("Saliendo del programa...")
        break
    else:
        print("Opcion no valida, por favor intente de nuevo.")