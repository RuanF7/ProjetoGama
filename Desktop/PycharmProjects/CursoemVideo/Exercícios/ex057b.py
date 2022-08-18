from random import randint
tent = 1
n = int(input('Estou pensando em um número de 0 a 5, você consegue adivinhar qual? \n'))
sort = randint(0, 5)
while n != sort:
    n = int(input('Você errou, tente novamente!\n'))
    if n != sort:
        tent += 1
    if n == sort:
        tent += 1
print('Você acertou!, o número era {} e você precisou de {} tentativas para adivinhar!'.format(sort, tent))
