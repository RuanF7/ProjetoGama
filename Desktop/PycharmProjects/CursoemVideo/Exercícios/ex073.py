tabela = (
    'Flamengo', 'Palmeiras', 'Vasco', 'Fluminense', 'Botafogo', 'Grêmio', 'Internacional', 'Corinthians', 'São Paulo',
    'Santos', 'Bahia', 'Fortaleza', 'Ceará', 'Sport', 'Red Bull', 'Chapecoense', 'Athletico PR', 'Atlético', 'Cruzeiro',
    'Atlético GO')
print(f'Os 5 primeiros colocados são: {tabela[0:5]}')
print(f'Os 4 últimos colocados são: {tabela[-4:]}')
print(f'A ordem alfabética da tabela é: {sorted(tabela)}')
print(f'O time da Chapecoense está na {tabela.index("Chapecoense")+1}ª posição')
