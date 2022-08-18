maior = homem = mulher20 = 0
print('-' * 30)
print('     CADASTRE UMA PESSOA')
print('-' * 30)
while True:
    Idade = int(input('Idade: '))
    Sexo = ' '
    while Sexo not in 'MF':
        Sexo = str(input('Sexo : [M/F] ')).strip().upper()[0]
    if Idade >= 18:
        maior += 1
    if Sexo == 'M':
        homem += 1
    if Idade < 20 and Sexo == 'F':
        mulher20 += 1
    print('-' * 30)
    Cont = ' '
    while Cont not in 'SN':
        Cont = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if Cont == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {maior}')
print(f'Ao todo temos {homem} homems cadastrados')
print(f'E temos {mulher20} mulheres com menos de 20 anos')
