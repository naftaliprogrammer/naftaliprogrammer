import random

palavras = ["amor", "alegria", "paz", "felicidade", "saúde",
            "sucesso", "esperança", "fé", "gratidão", "inspiração",
            "motivação", "criatividade", "inovação", "conhecimento",
            "sabedoria", "inteligência", "aprendizado", "crescimento",
            "desenvolvimento"]
receber_lista = random.choice(palavras)
print("Palavra_______:".format(receber_lista))
letras_secretas = []
letras_erradas = []
tentativas = 6
def jogo_da_forca():
    digite_letra = input("Digite a letra:   ")
    print("Palavra: ______", )

    while True:
        palavras_secreta =



