try:
    a = int(input("Ingrese un numero: "))
    b = int(input("Ingrese otro numero: "))
    resultado = a / b
except ZeroDivisionError as e:
    print(f"No se puede dividir entre 0 - {e}")
except ValueError as e:
    print(f"Debes ingresar un numero - {e}")
else:
    print(resultado)