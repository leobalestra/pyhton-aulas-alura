class ContaCorente:

    def __init__(self, codigo):
        self.codigo = codigo
        self.saldo = 0

    def deposita(self, valor):
        self.saldo += valor

    def __str__(self):
        return (f"Código: {self.codigo} saldo: {self.saldo}")



conta_leo = ContaCorente(292)
conta_lari = ContaCorente(666)
conta_lari.deposita(1000)

contas = [conta_leo, conta_lari]

for conta in contas:
    print(conta)

print("\n***Salário de 100 pila caiu***")

def deposita_todas_contas(contas):
    for conta in contas:
        conta.deposita(100)

contas = [conta_leo, conta_lari]
deposita_todas_contas(contas)
for conta in contas:
    print(conta)

#tuplas: imutáveis
leonardo = ('Leonardo', 21, 1998)
daniele = ('Daniele', 18, 2001)

#lista de tuplas
usuarios = [leonardo, daniele]
print(usuarios)

usuarios.append(('Paulo', 20, 2000))
print(usuarios)