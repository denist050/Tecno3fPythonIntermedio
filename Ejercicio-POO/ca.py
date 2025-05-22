import cb

class CuentaAhorro(cb.CuentaBancaria):
    def __init__(self, nombre_titular, dni_titular, fecha_nacimiento, saldo = 0, tasa_interes = 0.001,limite_extraccion = 500, intereses = 0):
        super().__init__(nombre_titular, dni_titular, fecha_nacimiento, saldo)
        self.__tasa_interes = tasa_interes
        self._li_extraccion = limite_extraccion
        self._intereses = intereses

    def obtener_saldo(self):
        saldo = super().obtener_saldo()
        print(f"El saldo de {self._nombre_titular} es {saldo}")
        self.calcular_interes()
        return saldo
        

    def depositar(self, monto):
        self._CuentaBancaria__saldo += monto
        print(f"Se ha depositado {monto} en la cuenta de {self._nombre_titular}")
        self.calcular_interes()
    
    def extraer(self, monto):
        if monto <= self.obtener_saldo() and monto <= self._li_extraccion:
            self._CuentaBancaria__saldo -= monto
            print(f"Se ha extraído {monto} de la cuenta de {self._nombre_titular}")
        else:
            if monto > self._li_extraccion:
                print(f"Usted supera el limite de extracción({self._li_extraccion})")
            else:
                print("Usted no posee saldo suficiente para realizar la operación")
        self.calcular_interes()

    def calcular_interes(self):
        self._intereses = self._CuentaBancaria__saldo * self.__tasa_interes
        self._CuentaBancaria__saldo += self._intereses 
        print(f"Intereses generados en la operacion: { self._intereses}")
    