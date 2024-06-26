dados = open("src/produtos.txt", "r", encoding="utf-8")

linhas = dados.readlines()
for linha in linhas:
    linhas = dados.readlines()

print(linha.strip().split()[0], end="_")
print(linha.strip().split()[1], end="-")
print(linha.strip().split()[2], end="-")
print(linha.strip().split()[3], end="-")
print(linha.strip().split()[4], end="-")
print()
