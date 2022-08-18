s = float(input('Qual o seu salário? '))
a1 = 15/100
a2 = 10/100
if s <= 1250:
    print('Você receberá um aumento de {}%, e seu novo salário será R${:.2f}'.format(15, s + (s * a1)))
else:
    print('Você receberá um aumento de {}%, e seu novo salário será R${:.2f}'.format(10, s + (s * a2)))
