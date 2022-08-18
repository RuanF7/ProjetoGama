vel = int(input('Qual é a velocidade?'))
km = int(80)
if vel > km:
    print('Você foi multado!')
    mul = (vel-km)*7
    print('A multa vai custar: R${:.2f}'.format(mul))
