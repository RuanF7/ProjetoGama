from random import randint
from time import sleep
mega = [[], []]
print('-' * 30)
print('JOGA NA MEGA SENA')
print('-' * 30)
n = int(input('Quantos números você quer que eu sorteie? '))
for c in range(1, 7):
    print(f'Jogo {c}: ', end='')
    num = randint(1, 60)
    print(num)
    sleep(1)
print('-=' * 10, 'Boa Sorte!', '-=' * 10)
#incompleto
