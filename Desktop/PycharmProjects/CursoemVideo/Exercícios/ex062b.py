print('Vamos fazer uma PA?!')
pa = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
count = 1
total = 0
n = pa
mais = 10
while count != 0:
    total += mais
    while count <= total:
        n += r
        count += 1
        print('{}-> '.format(n), end='')
    mais = int(input('\nGostaria de adicionar mais quantos temos? '))
print('PAUSE')
