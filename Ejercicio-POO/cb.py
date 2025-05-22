from abc import ABC, abstractmethod

class CuentaBancaria:
    def __init__(self, nombre_titular, dni_titular, fecha_nacimiento, saldo = 0):
        self._nombre_titular = nombre_titular #el guion bajo ("_") me indica que es privado
        self._dni_titular = dni_titular
        self._fecha_nacimiento = fecha_nacimiento
        self.__saldo = saldo
        
    def mostrar_nombre(self):
        return self._nombre_titular
    
    def cambiar_nombre(self, n):
        self._nombre_titular = n
    
    def obtener_saldo(self):
        return self.__saldo
    
    @classmethod
    @abstractmethod
    def depositar(self,monto):
        pass
    
    @classmethod
    @abstractmethod
    def extraer(self,monto):
        pass