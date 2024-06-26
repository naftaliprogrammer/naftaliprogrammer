{while True:
    try:

        valor_frete = float(input("Digite o valor do frete, por favor:"))
        peso_kg = float(input("Digite o valor do Peso favor:"))
        print(valor_frete//peso_kg)
        if peso_kg or valor_frete == 0.0:
            break
    except ZeroDivisionError:
        print("Peso invalido, tente novamente")
        continue


































