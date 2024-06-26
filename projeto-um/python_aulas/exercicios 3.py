try:

    produtos =["maça", "abacate", "melacia" , "pera "]
    estoque = [10,14,22,0]

    indice = int(input("Digite o indice:  "))

    print(produtos[indice])
    print(f"nós temos {estoque[indice]} de {produtos[indice]}")

except IndexError:
    print("Item não achado,existe apenas 4 produtos.")















