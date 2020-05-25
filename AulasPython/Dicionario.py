#set -> excluir as repetições (não possui índice)

usuarios_data_science = [1, 9 ,45, 68]
usuarios_machine_learning = [7, 9, 68, 99]

enviar_email = usuarios_machine_learning.copy()
enviar_email.extend(usuarios_machine_learning)

print(enviar_email)
print(set(enviar_email))

usuarios_data_science = {1, 9 ,45, 68}
usuarios_machine_learning = {7, 9, 68, 99}

#intersecção
print(usuarios_data_science & usuarios_machine_learning)

print(usuarios_data_science - usuarios_machine_learning)



aparicoes = {
    "Leonardo" : 1,
    "Progrmador" : 5,
    "alura" : 3
}
print(aparicoes)
print(type(aparicoes))

print(aparicoes["Leonardo"])

#adicionando
aparicoes["Carlota"] = 2
print(aparicoes)

#mudando valor
aparicoes["Carlota"] = 0
print(aparicoes)

#removendo
del aparicoes["Carlota"]
print(aparicoes)

print("Leonardo" in aparicoes)
print(1 in aparicoes)

for elemento in aparicoes.keys():
    print(elemento)

for elemento in aparicoes.values():
    print(elemento)

for elemento in aparicoes.items():
    print(elemento)