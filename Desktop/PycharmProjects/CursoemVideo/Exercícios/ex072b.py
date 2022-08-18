contagem = (
'zero', 'um', 'dois', 'tres', 'quatro',
'cinco', 'seis', 'sete', 'oito', 'nove',
'dez', 'onze', 'doze', 'treze', 'catorze',
'quinze', 'dezesseis', 'dezessete', 'dezoito',
'dezenove', 'vinte')
for c in contagem:
    n = int(input('Digite um número: '))
    if 0 <= n <= 20:
        break
print(f'Você digitou o número: {contagem[n]}')
