import random
def jogo_da_forca():
    # Palavra a ser adivinhada (você pode alterar para outras palavras)
    palavras = ["amor", "alegria", "paz", "felicidade", "saúde",
                "sucesso", "esperança", "fé", "gratidão", "inspiração",
                "motivação", "criatividade", "inovação", "conhecimento",
                "sabedoria", "inteligência", "aprendizado", "crescimento",
                "desenvolvimento"]
    palavra = random.choice(palavras)


    # Inicialização das listas
    oportunidades = 8
    letras_certas = []
    letras_erradas = []

    # Número total de tentativas
    tentativas = 6

    while True:
        # Exibe a palavra oculta com as letras corretas adivinhadas
        #
        palavra_mostrada = ""
        for letra in palavra:
            if letra in letras_certas:

                palavra_mostrada += letra

            else:
                palavra_mostrada += "_ "


        print(f"Palavra: {palavra_mostrada}")

        # Exibe as letras erradas adivinhadas
        print(f"Letras erradas: {', '.join(letras_erradas)}")
        print(f"Letras certas:{','.join(letras_certas)}")
        print(f"Tentativas {tentativas}")
        # Solicita ao jogador para digitar uma letra

        letra_digitada = input("Digite uma letra: ")

        # Verifica se a letra está correta ou incorreta
        if letra_digitada in palavra:
            letras_certas.append(letra_digitada)


        else:
            palavra_mostrada += '_'
            letras_erradas.append(letra_digitada)
            tentativas -= 1

        # Verifica se o jogador venceu ou perdeu
        if all(letra in letras_certas for letra in palavra):
            print("Parabéns! Você venceu!")
            break
        elif tentativas == 0:
            print(f"Fim de jogo! A palavra era '{palavra}'.")
            break

jogo_da_forca()