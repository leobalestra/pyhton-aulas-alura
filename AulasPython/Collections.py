idades = [35, 36 ,37 ,38]
#list
print(type(idades))
print(len(idades))
print(idades)
print(idades[0])

idades.append(15)
print(idades)

for idade in idades:
    print(idade)

#remove o primeiro elemento, remove tudo .clear()
idades.remove(36)
print(idades)

print(15 in idades)

if 15 in idades:
    idades.remove(15)

print(15 in idades)

#inserir elemento na posição específica
idades.insert(0, 99)
print(idades)

#inserir mais de um elemento
idades.extend([1,2,3,4])
print(idades)

idades_no_ano_que_vem = [(idade +1) for idade in idades]
print(idades_no_ano_que_vem)

print([(idade) for idade in idades if idade < 10])

def proximo_ano(idade):
    return idade+1

print([proximo_ano(idade) for idade in idades if idade > 21])