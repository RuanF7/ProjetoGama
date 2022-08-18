matriz = [[], [], [],
          [], [], [],
          [], [], []]
for c in range(0, 9):
    val = int(input(f'Digite o {c}º valor: '))
    matriz[c].append(val)
print(f'[ {matriz[0]} ][ {matriz[1]} ][ {matriz[2]} ]')
print(f'[ {matriz[3]} ][ {matriz[4]} ][ {matriz[5]} ]')
print(f'[ {matriz[6]} ][ {matriz[7]} ][ {matriz[8]} ]')
