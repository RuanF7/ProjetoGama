import emoji
from random import randint
nome = (str(input('Qual é o seu nome? ')))
print('Olá {}, Eu te desafio para um jogo de JoKenpo!'.format(nome))
jogada = (int(input("""Faça sua jogada:
{} [1]
{} [2]
{} [3]:
""".format(emoji.emojize(":raised_fist:"), emoji.emojize(":raised_hand:"), emoji.emojize(":victory_hand:")))))
PC = randint(1, 3)

if jogada == 1 and PC == 2:
    print('Você colocou {} e eu {}, HA-HA EU VENCI!'.format(emoji.emojize(":raised_fist:"), emoji.emojize(":raised_hand:")))
elif jogada == 1 and PC == 3:
    print('Você colocou {} e eu {}, PARABÉNS, VOCÊ ME VENCEU!'.format(emoji.emojize(":raised_fist:"), emoji.emojize(":victory_hand:")))
elif jogada == 2 and PC == 1:
    print('Você colocou {} e eu {}, PARECE QUE ESSA EU PERDI!'.format(emoji.emojize(":raised_hand:"), emoji.emojize(":raised_fist:")))
elif jogada == 2 and PC == 3:
    print('Você colocou {} e eu {}, VOCÊ FOI DERROTADO!'.format(emoji.emojize(":raised_hand:"), emoji.emojize(":victory_hand:")))
elif jogada == 3 and PC == 1:
    print('Você colocou {} e eu {}, DERROTA! MAIS SORTE NA PRÓXIMA VEZ!'.format(emoji.emojize(":victory_hand:"), emoji.emojize(":raised_fist:")))
elif jogada == 3 and PC == 2:
    print('Você colocou {} e eu {}, FUI DERROTADO!'.format(emoji.emojize(":victory_hand:"),emoji.emojize(":raised_hand:")))
else: print('EMPATE! =O')
