km = float(input('Quantos km você andou com o carro? '))
d = int(input('E por quantos dias ele foi alugado? '))
total = (d * 60) + (km * 0.15)
print('O preço a pagar pelo veículo é de R${:.2f} '.format(total))
