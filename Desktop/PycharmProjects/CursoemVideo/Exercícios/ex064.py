n = count = soma = 0
n = int(input('Digite um número [ou 999 para parar]: '))
while n != 999:
    soma += n
    count += 1
    n = int(input('Digite um número [ou 999 para parar]: '))
print('Foram digitados {} números e a soma desses números é {}.'.format(count, soma))
print('FIM')
