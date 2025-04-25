

arg1 = input("Ingrese un valor: ")
arg2 = input("Ingrese otro valor: ")
arg3 = input("Ingrese otro valor: ")
arg4 = input("Ingrese otro valor: ")

def ingresarArgumentos(*args):
    try:
        if len(args) < 2:
            raise ValueError("Debes ingresar al menos dos argumentos")
        print("\nTodos los argumentos son:", args)

    except ValueError as e:
        print(f" \nError: {e}")


opcion = 0
while(opcion != 5):
    print("\nIngresar argumentos. Seleccione opcion: ")
    print("1. Ingresar 1 argumento")
    print("2. Ingresar 2 argumentos")
    print("3. Ingresar 3 argumentos")
    print("4. Ingresar 4 argumentos")
    print("5. Salir")
    try:
        opcion = int(input("\nIngrese una opción: "))
        if opcion == 1:
            ingresarArgumentos(arg1)
        elif opcion == 2:
            ingresarArgumentos(arg1, arg2)
        elif opcion == 3:
            ingresarArgumentos(arg1, arg2, arg3)
        elif opcion == 4:
            ingresarArgumentos(arg1, arg2, arg3, arg4)
        elif opcion == 5:
            print("Saliendo...")
        else:
            print("Opción no válida.")
    except ValueError:
        print("Por favor, ingrese un número válido.")
