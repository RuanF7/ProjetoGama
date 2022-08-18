p = int(input('Digite o primeiro número da PA: '))
r = int(input('Agora digite sua razão: '))
dec = p + (10 - 1) * r
for c in range(p, dec + r, r):
    print(c, end=' ')
