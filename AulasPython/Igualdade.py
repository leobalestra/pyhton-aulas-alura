class ContaSalario:
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def __eq__(self, other):
        #insistence se quiser igualar tipo de contas dentro da hierarquia
        if type(other) != ContaSalario:
            return False

        return(self._codigo == other._codigo)

    def deposita(self, valor):
        self._saldo += valor

    def __str__(self):
        return (f"Código: {self._codigo} saldo: {self._saldo}")

conta1 = ContaSalario(37)
conta2 = ContaSalario(37)

print(conta1 == conta2)