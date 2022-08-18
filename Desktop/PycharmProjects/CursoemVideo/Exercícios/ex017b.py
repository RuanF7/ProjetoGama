from math import hypot
catop = float(input('Digite o valor do cateto aposto: '))
catad = float(input('Digite o valor do cateto adjacente: '))
hip = hypot(catop, catad)
print('O comprimento da hipotenusa é:{:.2f} '.format(hip))