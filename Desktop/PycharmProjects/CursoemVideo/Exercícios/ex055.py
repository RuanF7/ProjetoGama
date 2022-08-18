maior = 0
menor = 0
for p in range(1, 6):
    pes = float(input('Digite o peso da {}ª pessoa: '.format(p)))
    if p == 1:
        maior = pes
        menor = pes
    else:
        if pes > maior:
            maior = pes
        if pes < menor:
            menor = pes
print('O maior peso lido foi de {}Kg'.format(maior))
print('O menor peso lido foi de {}Kg'.format(menor))
