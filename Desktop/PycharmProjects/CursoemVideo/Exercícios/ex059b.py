n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
opc: int = int(input('''Digite uma opção para realizar a operação
[1]Somar
[2]Multiplicar
[3]Maior
[4]Novos números
[5]Sair do programa
: '''))
while 5 < opc <= 0:
    print('Opção inválida!')
if opc == 1:
    print('A soma entre {} e {} é {}.'.format(n1, n2, n1 + n2))
if opc == 2:
    print('A multiplicação entre {} e {} é {}.'.format(n1, n2, n1 * n2))
if opc == 3:
    if n1 > n2:
        print('O maior dos números é {}'.format(n1))
    if n1 == n2:
        print('Não ha maior, ambos são iguais!')
    else:
        print('O maior dos números é {}'.format(n2))
if opc == 4:
    n1 = int(input('Digite um novo valor para recomeçar: '))
    n2 = int(input('Agora um outro valor: '))
if opc == 5:
    print('Programa encerrado.')
