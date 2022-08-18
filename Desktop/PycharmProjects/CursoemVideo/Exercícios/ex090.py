alunos = {}
alunos['nome'] = str(input('Nome: '))
alunos['media'] = float(input(f'Média de {alunos["nome"]}: '))
if alunos['media'] < 5:
    alunos['situação'] = 'Reprovado'
elif 5 <= alunos['media'] < 7:
    alunos['situação'] = 'Recuperação'
else:
    alunos['situação'] = 'Aprovado'
print('-=' * 30)
print(f'  - nome é igual a', alunos['nome'], end=' ')
print()
print(f'  - média é igual a', alunos['media'], end=' ')
print()
print(f'  - situação é igual a', alunos['situação'], end=' ')
