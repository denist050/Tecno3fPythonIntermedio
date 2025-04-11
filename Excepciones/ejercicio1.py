resultado = 0

def dividir(a, b):
    try:
        resultado = a / b
    except ZeroDivisionError as e:
        print(f"No se puede dividir entre 0 - {e}")
    else:
        print(resultado)


dividir(10, 0)

