qtde = int(input("Quantidade que você deseja:  "))
for numero in range(qtde):
#while True:
    try:
     numero = int(input("Digite um número: "))
    except ValueError:
            print("Erro: Entradada invalida")
    except KeyError:
            print("\n o usuario não digitou nada")

    else:
        print("Quadrado", numero ** 2)

    finally:
        print("\n Nova interação")





















