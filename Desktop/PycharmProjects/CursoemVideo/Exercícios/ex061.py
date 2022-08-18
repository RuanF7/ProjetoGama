print('Vamos fazer uma PA?!')
p = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
n = p
count = 1
while count <= 10:
    print(n, end=' ')
    n += r
    count += 1
