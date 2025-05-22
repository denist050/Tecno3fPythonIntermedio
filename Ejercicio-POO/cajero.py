from cc import CuentaCorriente
from ca import CuentaAhorro

cuantacorrientecliente1 = CuentaCorriente("Juan Perez", "15265752", "20-06-1963", saldo = 200)
cuantadeahorrocliente1 = CuentaAhorro("Juan Perez", "15265752", "20-06-1963", saldo = 400)



def menu_principal():
    try:
        while True:
            opcion = int(input("------Cajero------\n"
                            "Seleccione la operacion:\n"
                            "1. Cuenta corriente.\n"
                            "2. Cuenta de ahorro.\n"
                            "3. Salir\n"))
            
            if opcion == 1:
                menu_cuenta_corriente()
            elif opcion == 2:
                menu_caja_ahorro()
            elif opcion == 3:
                print("Gracias por usar el cajero.\n")
                break
            else:
                print("Opcion invalida\n")
    except ValueError as e:
        print(f"Debe ingresar un numero. Error: {e}")

def menu_cuenta_corriente():
    try:
        while True:
            opcion = int(input("Cuenta Corriente:\n"
                                "1. Consultar saldo.\n"
                                "2. Depositar saldo.\n"
                                "3. Extraer saldo. \n"
                                "4. Volver al menu.\n"))
            
            if opcion == 1:
                cuantacorrientecliente1.obtener_saldo()
            elif opcion == 2:
                monto = int(input("Ingrese el monto a depositar: \n"))
                cuantacorrientecliente1.depositar(monto)
            elif opcion == 3:
                monto = int(input("Ingrese el monto a extraer: \n"))
                cuantacorrientecliente1.extraer(monto)
            elif opcion == 4:
                print("Regresando ...\n")
                menu_principal()
            else:
                print("Opcion invalida\n")
    except ValueError as e:
        print(f"Debe ingresar un numero. Error: {e}")


def menu_caja_ahorro():
    try:
        while True:
            opcion = int(input("Caja de ahorro:\n"
                                "1. Consultar saldo.\n"
                                "2. Depositar saldo.\n"
                                "3. Extraer saldo. \n"
                                "4. Volver al menu.\n"))
            
            if opcion == 1:
                cuantadeahorrocliente1.obtener_saldo()
            elif opcion == 2:
                monto = int(input("Ingrese el monto a depositar: \n"))
                cuantadeahorrocliente1.depositar(monto)            
            elif opcion == 3:
                monto = int(input("Ingrese el monto a extraer: \n"))
                cuantadeahorrocliente1.extraer(monto)            
            elif opcion == 4:
                print("Regresando ...\n")
                menu_principal()
            else:
                print("Opcion invalida\n")
    except ValueError as e:
        print(f"Debe ingresar un numero. Error: {e}")

menu_principal()