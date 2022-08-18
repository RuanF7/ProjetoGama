pessoas = []
pessoaspes = []
totpes = totlev = 0

while True:
    nome = str(input('Digite o nome da pessoa: '))
    pessoaspes.append(nome)
    peso = float(input('Digite o peso da pessoa: '))
    pessoaspes.append(peso)
    pessoas.append(pessoaspes[:])
    pessoaspes.clear()
    r = str(input('Quer continuar S/N? '))
    if r in 'Nn':
        break
for p in pessoaspes:
    if p[1] == 1:
        totpes = p
        totlev = p
    else:
        if p[1] > totpes:
            totpes = p[1]
        if p[1] < totlev:
            totlev = p[1]
print('=-' * 30)
print(f'Foram  cadastradas {len(pessoas[0])-1} pessoas.')
print(f'A pessoa mais pesada foi {totpes}')
print(f'A pessoa mais leve foi {totlev}')
#errado, ver 084b
