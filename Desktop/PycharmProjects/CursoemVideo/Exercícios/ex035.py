print('Dê-me o valor de 3 retas e lhe direi se elas podem formar um triangulo! ')
r1 = float(input('Digite o valor da primeira reta: '))
r2 = float(input('Digite o valor da segunda reta: '))
r3 = float(input('Digite o valor da terceira reta: '))
if r1 < r2 + r3 and r2 < r2 + r3 and r3 < r2 + r1:
    print('É um triangulo possível!')
else:
    print('Não é um triangulo possível!')
