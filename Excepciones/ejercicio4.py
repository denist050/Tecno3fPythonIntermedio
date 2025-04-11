import os

ruta = "archivo.txt"
try:
    with open("archivo.txt", "r") as archivo:
        archivo = archivo.read()
except FileNotFoundError:
    print("El archivo no existe")
    try:
        with(open(ruta, "w")) as archivo:
            archivo.write("Archivo creado")
        print(f"Archivo '{ruta}' ha sido creado en: {os.getcwd()}")
    except Exception as e:
        print(f"Hubo un error al intentar crear el archivo: {e}")
else:
    with open(ruta, "r") as archivo:
        archivo = archivo.read()
        print(archivo)
