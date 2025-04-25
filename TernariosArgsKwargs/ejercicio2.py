try:
    palabra = input("Ingrese una palabra: ")
    palabra2 = input("Ingrese otra palabra: ")
    palabra3 = input("Ingrese otra palabra: ")
    palabra4 = input("Ingrese otra palabra: ")
except ValueError as e:
    print(f"Debes ingresar una palabra - {e}")

palabraClave = input("Ingrese la palabra a encontrar: ")


def BuscarPalabra(palabra,*args):

    respuesta = print("La palabra es: ",palabra + "y es la palabra numero "+ str(args.index(palabra)+1)) if palabra in args else print("La palabra ingresada no se encuentra")
    return respuesta

respuesta = BuscarPalabra(palabraClave, palabra, palabra2,palabra3,palabra4)
print(respuesta)