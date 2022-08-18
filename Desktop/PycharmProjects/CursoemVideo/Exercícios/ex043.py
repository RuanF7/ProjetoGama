alt = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))
IMC = peso / (alt ** 2)
if IMC < 18.5:
    print('Seu IMC é {:.2f}, e você está Abaixo do peso!'.format(IMC))
elif 18.5 <= IMC < 25:
    print('Seu IMC é {:.2f}, e você está no peso Ideal!'.format(IMC))
elif 25 <= IMC < 30:
    print('Seu IMC é {:.2f}, e você com Sobrepeso!'.format(IMC))
elif 30 <= IMC < 40:
    print('Seu IMC é {:.2f}, e você está Obeso!'.format(IMC))
else:
    print('Seu IMC é {:.2f}, e você está com Obesidade Mórbida!'.format(IMC))
