tabela = (
    'Flamengo', 'Palmeiras', 'Vasco', 'Fluminense', 'Botafogo',
    'Grêmio', 'Internacional', 'Corinthians', 'São Paulo',
    'Santos', 'Bahia', 'Fortaleza', 'Ceará', 'Sport', 'Red Bull',
    'Chapecoense', 'Athletico PR', 'Atlético', 'Cruzeiro', 'Atlético GO')
print('-=' * 30)
print(f'Os 5 primeiros colocados são: {tabela [0:5]}')
print('-=' * 30)
print(f'Os 4 últimos colocados são: {tabela[-4:]}')
print('-=' * 30)
print(f'Os times em ordemm alfabética: {sorted(tabela)}')
print('-=' * 30)
print(f'A chapecoense estão na posição: {tabela.index("Chapecoense") + 1}')
