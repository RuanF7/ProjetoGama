l = float(input('\033[1:31mQual a largura da sua parede?\033[m '))
a = float(input('\033[1:31:43mE qual é a altura dela?\033[m '))
ar = l * a
t = ar / 2
print('A sua parede tem uma área de {} e serão necessários {} litros de tinta'.format(ar, t))