n = 1
x = 0
from random import randint
from time import sleep
sort = randint(0, 10)
print('Estou pensando em um número de 0 a 10, você consegue adivinhar qual? ')
while n != sort:
    n = int(input('Digite o número: '))
    print('PROCESSANDO...')
    sleep(0.5)
    if n != sort:
        x += 1
        print('Você errou, tente de novo: ')
    if n == sort:
        x += 1
print('Parabéns, você acertou! O número que eu pensei foi o número {}. Você precisou de {} tentativa(s) para acerta-lo!'.format(sort, x))
