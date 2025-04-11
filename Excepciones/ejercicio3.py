diccionario = {"nombre" : "Juan", "apellido" : "Perez"}

try:
    print(diccionario["edad"])
except KeyError:
    print("No existe la clave edad")