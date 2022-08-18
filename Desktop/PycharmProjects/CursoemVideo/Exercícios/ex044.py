print('{:=^40}'.format('LOJAS GUANABARA '))
pre = float(input('Digite o preço do produto: R$'))
cond = float(input('''O pagamento será:
[1] á vista no dinheiro ou cheque (10% de desconto)
[2] á vista no cartão (5% de desconto)
[3] em 2x no cartão (Valor integral)
[4] em 3x ou mais no cartão (20% de juros)
'''))
if cond == 1:
    avisd = pre - pre * 10 / 100
    print('O valor final do produto será: R${:.2f}.'.format(avisd))
elif cond == 2:
    avisc = pre - pre * 5 / 100
    print('O valor final do produto será: R${:.2f}.'.format(avisc))
elif cond == 3:
    xc = pre
    parc = xc / 2
    print('O valor final do produto será: R${:.2f}, parcelado em 2x de R${:.2f}'.format(pre, parc))
else:
    tparc = int(input('Quantas parcelas? '))
    xc = pre + (pre * 20 / 100)
    parc = xc / tparc
    print('O valor final do produto será: R${:.2f}, parcelado em {}x de {:.2f}'.format(xc, tparc, parc))
