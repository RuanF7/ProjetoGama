listagem = ('Pão', 0.50,
            'Leite', 3.99,
            'Queijo', 3.50,
            'Presunto', 2.50,
            'Manteiga', 9.90,
            'Café', 8.80,
            'Suco', 10.00)
print('=' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('=' * 40)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')
print('=' * 40)
