vc = int(input('\033[0:31mQual é o valor da casa que você gostaria de comprar? R$'))
s = int(input('\033[0:37mQual é o seu salário? R$'))
qa = int(input('\033[0:32mEm quantos anos você gostaria de pagar essa casa? '))
pre = (vc / 12) / qa
if pre > s - (s * 30 / 100):
    print('\033[7:31:43mO seu empréstimo foi negado!\033[m')
else:
    print('\033[4:36:40mO valor da prestação de seu emprestimo será de R${:.2f} por mês.\033[m'.format(pre))
