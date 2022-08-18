par = 0
print('Digite 6 números e lhe direi a soma de todos os que forem pares!')
for c in range(1, 7):
    n = int(input('Digite o {}º número: '.format(c)))
    if n % 2 == 0:
        par += n
print('A soma dos números pares digitados é: {}'.format(par))
