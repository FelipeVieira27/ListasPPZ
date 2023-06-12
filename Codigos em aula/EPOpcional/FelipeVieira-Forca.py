#Felipe Gabriel Vieira

import random as ran
import requests
url = 'https://www.ime.usp.br/~pf/dicios/br-sem-acentos.txt'
opcoes = requests.get(url).text.lower().split()

#opcoes = ["felipe", "fatec"]

desenhos = {0: '''

  +--------+
  |        |
           |
           |
           |
           |
           |
=============

''', 1: '''

  +--------+
  |        |
  O        |
           |
           |
           |
           |
=============

''', 2: '''

  +--------+
  |        |
  O        |
  |        |
           |
           |
           |
=============

''', 3: '''

  +--------+
  |        |
  O        |
 /|        |
           |
           |
           |
=============

''', 4: '''

  +--------+
  |        |
  O        |
 /|\       |
           |
           |
           |
=============

''', 5: '''

  +--------+
  |        |
  O        |
 /|\       |
 /         |
           |
           |
=============

''', 6: '''

  +--------+
  |        |
  O        |
 /|\       |
 / \       |
           |
           |
=============

'''}

continuar = ["sim", "s", "nao", "não", "n"]
jogando = True
vitoria = 0
rodada = 1
hist = "- - - - - "
print ("Bem-vindo ao Jogo da Forca!")
while jogando:
    erros = 0
    descoberto = []
    tentativas = ""
    resposta = ran.choice(opcoes)
    for y in resposta:
        descoberto.append("_")
    jogada = True
    print(f"Rodada {rodada}")
    while jogada:    
        print (desenhos[erros])
        for x in descoberto:
            print(x, end=" ")
        print (f"Tentativas: {tentativas}")
        chute = input("Insira seu palpite: ")
        chute = chute.lower()
        cont = 0
        if chute in resposta:
            for x in range(len(resposta)):
                for y in range(len(chute)):   
                    if chute[y] == resposta[x]:
                        descoberto[x] = chute[y]
                        cont += 1
        tentativas += chute + " "
        print ("")
        if cont > 0:
          print(f"Você acertou {cont} letra(s)! A resposta possui a letra {chute}.")
        if cont == 0:
            erros += 1
            print(f"Você errou! A resposta não possui a letra {chute}.")
        if erros == 6:
            print(f"Poxa, você perdeu! A resposta era {resposta}.")
            hist += "D "
            jogada = False
        if "".join(descoberto) == resposta:
            vitoria += 1
            print(f"Parabéns! Você venceu pela {vitoria}° vez! A resposta era {resposta}.")
            hist += "V "
            jogada = False
    continua = ""
    recente = hist[-10:]
    print(f"Seu histórico recente é {recente}")
    while continua not in continuar:
        print("Deseja jogar novamente?")
        continua = input("")
        continua = continua.lower()
        if continua == "sim" or continua == "s":
            jogada = True
            rodada += 1
        else:
            jogando = False

print("Obrigado por jogar, até a próxima!")