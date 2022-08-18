d = float(input('Qual a distância da viagem em km?'))
vc = d*0.5
vl = d*0.45
if d <= float(200):
    print('A sua viagem custará: R${:.2f}'.format(vc))
else:
    print('A sua viagem custará: R${:.2f}'.format(vl))
