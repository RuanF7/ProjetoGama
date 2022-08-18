n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
esc = 0
while esc != 5:
    print('''    [1]somar
     [2]multiplicar
     [3]maior
     [4]novos números
     [5]sair do programa
     ''')
    esc = int(input('Digite a opção que deseja realizar: '))
    if esc == 1:
        soma = n1 + n2
        print('A soma de {} e {} é: {}'.format(n1, n2, soma))
    elif esc == 2:
        mult = n1 * n2
        print('A multiplicação entre {} e {} é: {}'.format(n1, n2, mult))
    elif esc == 3:
        if n1 > n2:
            print('O maior número entre {} e {} é: {}'.format(n1, n2, n1))
        elif n2 > n1:
            print('O maior número entre {} e {} é: {}'.format(n1, n2, n2))
    elif esc == 4:
        n1 = int(input('Digite um novo valor para recomeçar: '))
        n2 = int(input('Agora um outro valor: '))
    elif esc == 5:
        print('Saindo do programa, Até logo!')
