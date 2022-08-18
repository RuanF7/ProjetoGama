valores = [[], []]
val = 0
for c in range(1, 8):
    val = int(input(f'Digite o {c}º valor: '))
    if val % 2 == 0:
        valores[0].append(val)
    else:
        valores[1].append(val)
valores[0].sort()
valores[1].sort()
print('=-' * 30)
print(f'Os valores pares digitados foram: {valores[0]} ')
print(f'Os valores ímpares digitados foram: {valores[1]}')
