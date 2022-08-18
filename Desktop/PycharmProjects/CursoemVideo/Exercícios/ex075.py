n = (int(input('Digite um número: ')),
     int(input('Digite outro número: ')),
     int(input('Digite mais um número: ')),
     int(input('Digite o ultimo número: ')))
print(f'Você digitou os valores: {n}', end='')
print(f'\nO número 9 apareceu {n.count(9)}x')
if 3 in n:
    print(f'O número 3 apareceu na posição {n.index(3) + 1}')
else:
    print('O número 3 não foi digitado!')
print(f'Os valores pares são: ', end=' ')
for num in n:
    if num % 2 == 0:
        print(num, end=' ')
