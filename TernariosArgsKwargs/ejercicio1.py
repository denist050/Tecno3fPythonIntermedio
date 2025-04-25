num1 = 0
num2 = 0

def calcularNumeroMayor(num1, num2):
    return num1 if num1 > num2 else num2

num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese otro numero: "))
print(f"El numero mayor es: {calcularNumeroMayor(num1, num2)}")

