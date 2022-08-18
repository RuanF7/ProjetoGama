import math
catop = float(input('Digite o valor do cateto aposto: '))
catad = float(input('Digite o valor do cateto adjacente: '))
hip = (catop ** 2) + (catad ** 2)
comphip = math.sqrt(hip)
print('O comprimento da hipotenusa é:{:.2f} '.format(comphip))

