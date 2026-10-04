
# listas
lsita_nove = []
nomes =["Pedro", "Fernanda", "Renato", "Luciano"]
print(nomes[0]) # primeiro item da lista
# print(nomes)

nomes.append("Maria")
print(nomes)


# dicionario

# dicionario = {chave: valor, chave: valor}
idades = {"Pedro": 18, "Fernanda": 43, "Renato": 61, "Luciano": 48}
print(idades["Pedro"]) # pega informação no dicionario -> dicionario [chave]
idades["Maria"] = 16 # adicionando uma informação
idades["Pedro"] = 17 # editando
print(idades)

# role = quem é o usuario
# content = conteudo da mensagem
mensagem1 = {"role": "assistant", "content": "Bora aprender Python"}
mensagem2 = {"role": "user", "content": "Bora sim, bora aprender"}
mensagem3 = {"role": "assistant", "content": "Então vamos comeãr a aula"}

lista_mensagens = [mensagem1, mensagem2, mensagem3]

nova_mensagem = {"role": "user", "content": "Opa, agora bora botar Python pro jogo"}
lista_mensagens.append(nova_mensagem)

print(lista_mensagens)