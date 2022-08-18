jogador = {}
partidas = []
jogador['Nome'] = str(input('Nome do Jogador: '))
tot = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
for v in range(0, tot):
    partidas.append(int(input(f'Quantos gols na partida {v+1}? ')))
jogador['Gols'] = partidas[:]
jogador['Total'] = sum(partidas)
print('-=' * 30)
print(jogador)
print('-=' * 30)
for k, v in jogador.items():
    print(f'  - O campo {k} tem valor {v} ')
print('-=' * 30)
print(f'O jogador {jogador["Nome"]} jogou {tot} partidas')
for i, v in enumerate(jogador['Gols']):
    print(f'   => Na partida {i+1}, fez {v} gols.')
print(f'Foi um total de {jogador["Total"]} gols.')
