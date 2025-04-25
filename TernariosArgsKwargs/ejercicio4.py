try:
    print("Calculo de promedio: ")
    num1 = int(input("Ingrese un numero: "))
    num2 = int(input("Ingrese otro numero: "))
    num3 = int(input("Ingrese otro numero: "))
    num4 = int(input("Ingrese otro numero: "))
    num5 = int(input("Ingrese otro numero: "))
except ValueError:
    print("Debes ingresar solo numeros")

def calcularPromedio(*args):
    return print(sum(args) / len(args)) if len(args) > 0 else print("No se puede calcular el promedio")

calcularPromedio(num1, num2, num3, num4, num5)