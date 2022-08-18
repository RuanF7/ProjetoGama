from random import randint
aleat = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print(f'Os números gerados foram: ', end='')
for c in aleat:
    print(f'{c}', end=' ')
print(f'\nO maior númeor foi o {max(aleat)},\nE o menor foi {min(aleat)}')
