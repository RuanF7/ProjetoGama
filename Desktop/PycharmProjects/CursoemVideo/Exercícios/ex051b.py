print('Vamos fazer uma PA?!')
pa = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
for c in range(pa, pa + (9 * r) + r, r):
    print(c, end=' ')
