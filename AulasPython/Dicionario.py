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