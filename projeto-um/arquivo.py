def leitura():
    with open("src/cliente.txt", "r") as f:
        dados = f.readline()
        for linha in dados:
            print(linha)


def escrita():
    with open("src/cliente.txt", "w") as f:
        nome = input("Nome:")
        f.write(f"\n{nome}")


def sair():
    with open("src/cliente.txt", "w") as f:
        nome = input("Nome:")
        f.write(f"\n{nome}")




while True:
    print("[1]leitura\n[2]ecrita\n[3]sair")

    opcao = int(input())

    if opcao == 1:
        leitura()
    elif opcao == 2:
        escrita()
    elif opcao == 3:
         print("O laço terminou")
         break