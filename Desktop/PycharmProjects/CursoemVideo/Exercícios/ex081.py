listvalores = []
while True:
    n = int(input('Digite um valor: '))
    listvalores.append(n)
    r = str(input('Quer continuar S/N? '))
    if r in 'Nn':
        break
print('=-' * 30)
print(f'Você digitou ', len(listvalores), 'elementos')
listvalores.sort(reverse=True)
print(f'Os valores em ordem decrescente são {listvalores}')
if 5 in listvalores:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado dentro da lista!')
