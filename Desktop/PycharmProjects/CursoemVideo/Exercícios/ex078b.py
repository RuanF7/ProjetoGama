listvalores = []
maior = 0
menor = 0
for count in range(0, 5):
    listvalores.append(int(input(f'Digite um valor para a posição {count}: ')))
    if count == 0:
        maior = menor = listvalores[count]
    else:
        if listvalores[count] > maior:
            maior = listvalores[count]
        elif listvalores[count] < menor:
            menor = listvalores[count]
print('=-'*30)
print(f'Você digitou os valores: {listvalores}')
print(f'O maior valor foi o {maior} nas posições ', end='')
for i, v in enumerate(listvalores):
    if v == maior:
        print(f'{i}...', end='')
print()
print(f'O menor valor foi o {menor} nas posições ', end='')
for i, v in enumerate(listvalores):
    if v == menor:
        print(f'{i}...', end='')
print()
