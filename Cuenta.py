# Python
class Cuenta:
    def __init__(self):
        self.__saldo = 0.0
    
    def depositar(self, monto):
        if monto > 0:
            self.__saldo += monto
    
    def get_saldo(self):
        return self.__saldo

# Ejemplo de uso
mi_cuenta = Cuenta()
mi_cuenta.depositar(10000)
mi_cuenta.depositar(7000)
print("Saldo actual:", mi_cuenta.get_saldo())
