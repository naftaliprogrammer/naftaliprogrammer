lista_nome = []
lista_nascimento = []
qtd = int(input("Digite a quantidade de dados:"))
for i in range(qtd):
     nome = input(" Informe o seu nome por favor:")
     data_de_nascimento = input("Digite o sua data de nascimento, por favor:")
     lista_nome.append(nome)
     lista_nascimento.append(data_de_nascimento)



#print(lista_nome)
#print(lista_nascimento)

for var in range(len(lista_nascimento)):

    print("Nome:", lista_nome[var],"\nData de nascismento", lista_nascimento[var])