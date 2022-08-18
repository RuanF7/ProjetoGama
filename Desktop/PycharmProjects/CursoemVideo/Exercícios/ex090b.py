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
for k, v in alunos.items():
    print(f'   - {k} é igual a {v}')
