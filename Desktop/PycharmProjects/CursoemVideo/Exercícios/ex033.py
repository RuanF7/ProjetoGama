print('Digite 3 números diferentes para saber qual é o maior e o menor entre eles!')
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
if n1 > n2 and n1 > n3:
    print('{} é o maior!'.format(n1))
if n2 > n1 and n2 > n3:
    print('{} é o maior!'.format(n2))
else:
    print('{} é o maior!'.format(n3))

if n1 < n2 and n1 < n3:
    print('{} é o menor!'.format(n1))
if n2 < n1 and n2 < n3:
    print('{} é o menor!'.format(n2))
else:
    print('{} é o menor!'.format(n3))
