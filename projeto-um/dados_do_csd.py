import csv
with open("src/dados_do_banco.csv",  "r", encoding="utf-8") as dd:

 dados_tratados.append(linha)
dados_tratados = []
for linhas in dados_tratados[1:]:

    if float(linhas[4]) <= 400:
        print(linhas[0], linhas[1], linhas[4], "tem direito a bonus")





































































