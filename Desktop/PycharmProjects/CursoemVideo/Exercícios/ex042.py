print('Dê-me o valor de 3 retas e lhe direi se elas podem formar um triangulo e qual é o seu tipo! ')
r1 = float(input('Digite o valor da primeira reta: '))
r2 = float(input('Digite o valor da segunda reta: '))
r3 = float(input('Digite o valor da terceira reta: '))
if r1 < r2 + r3 and r2 < r2 + r3 and r3 < r2 + r1:
    print('\033[1::44mÉ um triangulo possível!\033[m')
    if r1 == r2 == r3:
        print('E ele é um triangulo do tipo: \033[1::40mEQUILÁTERO!\033[m')
    elif r1 != r2 != r3 != r1:
        print('E ele é um triangulo do tipo: \033[1::40mESCALENO!\033[m')
    else:
        print('E ele é um triangulo do tipo: \033[1::40mISÓSCELES!\033[m')
else:
    print('\033[1::41mNão é um triangulo possível!\033[m')
