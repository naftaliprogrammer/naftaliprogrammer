while True:
    try:
        x = int(input("digite o valor do X:"))
        y = int(input("digite o valor do y:"))

        print(x//y)
        if x == 0:
            break
    except ValueError:

        print("Apenas Números Inteiros")

        continue
    except  ZeroDivisionError:
        qtd_de_erros = qtd_de_erros +1
        if qtd_de_erros == 3:
         print("Não é possivel dividir por zero")
