from math import trunc

contador = 0

def ingresarNumero():
    return int(input("Ingrese un numero: "))

def sumar(a, b):
    return trunc(a + b)

b = ""
if __name__ == "__main__":
    while isinstance(b, str) or contador < 3:
        try:
            b = ingresarNumero()
        except ValueError as e:
            print(f"No se puede ingresar un valor string - {e}")
            contador += 1
            if contador == 3:
                print("No se puede ingresar mas de 3 veces")
                break
        else:
            print(sumar(10, b))
            break


