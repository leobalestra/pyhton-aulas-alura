class Conta:

    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def deposita(self, valor):
        self._saldo += valor

    def __str__(self):
        return (f"Código: {self._codigo} saldo: {self._saldo}")

#herança
class Corrente(Conta):
    def passa_um_mes(self):
        self._saldo -= 2

class Poupanca(Conta):
    def passa_um_mes(self):
        self._saldo *= 1.01
        self._saldo -= 3

conta1 = Corrente(1)
conta1.deposita(1000)
conta1.passa_um_mes()
print(conta1)

conta2 = Poupanca(2)
conta2.deposita(1000)
conta2.passa_um_mes()
print(conta2)

conta1 = Corrente(1)
conta1.deposita(1000)
conta1.passa_um_mes()
print(conta1)

conta2 = Poupanca(2)
conta2.deposita(1000)
conta2.passa_um_mes()