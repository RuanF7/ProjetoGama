listvalores = []
while True:
    n = int(input('Digite um valor: '))
    if n not in listvalores:
        listvalores.append(n)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado! Não vou adicionar. ')
    r = str(input('Quer continuar S/N? '))
    if r in 'Nn':
        break
print('=-' * 30)
listvalores.sort()
print(f'Você digitou os valores {listvalores}')
