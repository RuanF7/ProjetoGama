sidade = 0
midade = 0
midhom = 0
nomemaisvelho = ''
mmenos = 0
totmulher20 = 0

for p in range(1, 5):
    nome = str(input('Digite o nome da {}ª pessoa: '.format(p))).strip()
    idade = int(input('Digite a idade da {}ª pessoa: '.format(p)))
    sexo = str(input('Digite o sexo da {}ª pessoa [M/F]: '.format(p))).strip()
    sidade += idade
    if p == 1 and sexo in 'Mm':
        midhom = idade
        nomemaisvelho = nome
    if sexo in 'Mm' and idade > midhom:
        midhom = idade
        nomemaisvelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1

midade = sidade / 4
print('A média de idade do grupo é de {} anos'.format(midade))
print('O homem mais velho tem {} anos e se chama {}:'.format(midhom, nomemaisvelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totmulher20))
