dados = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota1: '))
    nota2 = float(input('Nota2: '))
    media = (nota1 + nota2) / 2
    dados.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-=' * 30)
print('No. NOME            MÉDIA')
print('-' * 30)
for i, a in enumerate(dados):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-' * 35)
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe): ' ))
    if opc == 999:
        break
    if opc <= len(dados) - 1:
        print(f'Notas de {dados[opc][0]} são {dados[opc][1]}')
print('<<< VOLTE SEMPRE >>>')