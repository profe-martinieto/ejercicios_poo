# Python
class Cuenta:
    def __init__(self):
        self.__saldo = 0.0
    
    def depositar(self, monto):
        if monto > 0:
            self.__saldo += monto
    
    def get_saldo(self):
        return self.__saldo
