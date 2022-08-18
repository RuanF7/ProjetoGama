valores = list()
for count in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição: {count} ')))
print('=-' * 30, end=' ')
print(f'\nVocê digitou os valores: {valores}')
for c, v in enumerate(valores):
    print(f'\nVocê digitou o valor {v} na posição {c}', end=' ')
print(f'\nO maior valor digitado foi {max(valores)}')
print(f'O menor valor digitado foi {min(valores)}')
