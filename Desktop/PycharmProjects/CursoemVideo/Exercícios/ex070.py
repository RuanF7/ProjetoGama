totga = maior = barato = count = 0
menor = ' '
print('-' * 30)
print('LOJAS SUPER BARATÃO')
print('-' * 30)
while True:
    nome = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$'))
    count += 1
    totga += preco
    if preco > 1000:
        maior += 1
    if count == 1 or preco < barato:
        barato = preco
        menor = nome
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print('-' * 30)
print(f'O total da compra foi R${totga:.2f}')
print(f'Temos {maior} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {menor} que custa R${barato:.2f}')
