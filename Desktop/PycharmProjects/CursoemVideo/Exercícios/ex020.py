import random
n1 = str(input('Dê-me o nome do primeiro aluno: '))
n2 = str(input('Agora do segundo: '))
n3 = str(input('Do terceiro: '))
n4 = str(input('Por fim, o quarto: '))
sort = (n1, n2, n3, n4)
order = random.sample(sort, k=4)
print('E a ordem das apresentações é: ', order)
