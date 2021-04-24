# forca.py
# Um jogo feito por Thiago e Papai em 24/04/2021
# numa manhã ensolarada.

import random


def boas_vindas():
    print()
    print("****************************************")
    print("* BEM VINDO AO JOGO DA FORCA           *")
    print("* UM JOGO EMOCIONANTE                  *")
    print("****************************************")
    print()


def imprimir_letras(letras):
    for letra in letras:
        print(letra, " ", end="")

    print("\n")


def mensagem_fracassou():
    print("Voce fracassou. Tente novamente com mais calma\n")


def mensagem_acertou():
    print("Parabens voce acertou. Voce é muito esperto\n")


def ler_palavras_secretas_do_arquivo(nome_do_arquivo):
    arquivo = open(nome_do_arquivo, "r")

    resultado = []

    for palavra in arquivo:
        resultado.append(palavra.strip().upper())

    arquivo.close()

    return resultado


def imprimir_boneco(tentativa):
    if tentativa_atual == 1:
        print(''' 
         O''')
    elif tentativa_atual == 2:
        print(''' 
         O
         |''')
    elif tentativa_atual == 3:
        print('''
         O
        \|/''')
    elif tentativa_atual == 4:
        print(''' 
         O
        \|/
         |''')
    elif tentativa_atual == 5:
        print(''' 
         O
        \|/
         |
         |''')
    elif tentativa_atual == 6:
        print(''' 
         O
        \|/
         |
         |
        / \\''')

    print('\n\n')


boas_vindas()

numero_maximo_tentativas = 6
palavras_secretas = ler_palavras_secretas_do_arquivo('palavras.txt')

chutes_dados=[]

palavra_secreta = palavras_secretas[random.randrange(0, len(palavras_secretas) - 1)]
letras = []

for letra in palavra_secreta:
    letras.append("_")

print("Tente acertar a palavra:\n")

tentativa_atual = 1

while True:
    if tentativa_atual > numero_maximo_tentativas:
        mensagem_fracassou()
        print(f'A palavra secreta eh {palavra_secreta}')
        break

    imprimir_letras(letras)

    if len(chutes_dados) > 0:
        print("Letras ja usadas ", chutes_dados)

    msg = f'Voce está na tentativa {tentativa_atual}. Qual o seu chute? '
    chute = input(msg).strip().upper()

    if len(chute) != 1:
        print("*** Voce deve informar somente uma letra")
        continue

    if chute in chutes_dados:
        continue
    else:
        chutes_dados.append(chute)

    index = 0

    acertou = False

    for letra in palavra_secreta:
        if chute == letra:
            letras[index] = chute
            acertou = True
        index += 1

    if not acertou:
        print('Chute errado!!!')
        imprimir_boneco(tentativa_atual)
        tentativa_atual += 1

    if "_" not in letras:
        mensagem_acertou()
        print(f'A palavra secreta eh {palavra_secreta}')
        break
