n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
if m < 5.0:
    print('Sua média foi {}, você está \033[1:31mREPROVADO!\033[m'.format(m))
elif 5.0 <= m <= 6.9:
    print('Sua média foi {}, você está de \033[1:35mRECUPERAÇÃO!\033[m'.format(m))
else:
    print('Sua média foi {}, você foi \033[1:32mAPROVADO!\033[m'.format(m))
