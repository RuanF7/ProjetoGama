from random import randint
from time import sleep
n: int = (int(input('Estou pensando em um número de 0 a 5, você consegue adivinhar qual? ')))
sort = randint(0, 5)
print('PROCESSANDO...')
sleep(1)
if n == sort:
    print('Você acertou, o número é: {}'.format(n))
else:
    print('Que pena, você errou!')