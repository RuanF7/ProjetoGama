print('Vamos fazer uma PA?!')
p = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
n = p
count = 1
total = 0
outra = 10
while outra != 0:
    total += outra
    while count <= total:
        print(n, end=' ')
        n += r
        count += 1
    print('pausa')
    outra = int(input('\nGostaria de fazer de mostrar mais quantos termos ? '))
print('Progressão finalizada com {} termos mostrados.'.format(total))
