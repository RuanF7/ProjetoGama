sexo = str(input('''Qual é o seu sexo?
Digite (M) para masculino e (F) para feminino: ''')).upper().strip()[0]
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Por favor, digite apenas (M) ou (F)!')).upper().strip()[0]
print('Sexo {} registrado!'.format(sexo))
print('Fim!')
