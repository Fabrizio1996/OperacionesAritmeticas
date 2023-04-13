while True:
    try:
        # Se muestra el menu y se selecciona una opcion
        print("Seleccione la operación deseada:")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Salir")

        opcion = int(input("Ingresar una opcion: "))

        # Si el usuario selecciona la opcion 5 se cierra el programa
        if opcion == 5:
            print("Muchas gracias. Adios!")
            break

        # El usuario ingresa los datos
        num1 = int(input("Ingresar el primer numero: "))
        num2 = int(input("Ingresar el segundo número: "))

        # Realizar la operación deseada y mostrar el resultado
        if opcion == 1:
            resultado = num1 + num2
            print(f"La suma es: {resultado}")
        elif opcion == 2:
            resultado = num1 - num2
            print(f"La resta es: {resultado}")
        elif opcion == 3:
            resultado = num1 * num2
            print(f"La multiplicación es: {resultado}")
        elif opcion == 4:
            if num2 == 0:
                raise ValueError("Error: no se puede dividir entre cero.")
            else:
                resultado = num1 / num2
                print(f"La división es: {resultado}")
        else:
            raise ValueError("Error: opción no válida.")

    except ValueError as error:
        print(error)