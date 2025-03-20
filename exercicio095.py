'''
Aprimore o DESAFIO 093 para que ele funcione com 
vários jogadores, incluindo um sistema de 
visualização de detalhes do aproveitamento 
de cada jogador.
'''
time = list()
jogador = dict()
partidas = list()

while True:
    jogador.clear()
    jogador['nome'] = input('Nome do jogador: ').strip().title()
    total_partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()

    for cont in range(0, total_partidas):
        partidas.append(int(input(f'   Quantos gols na partida {cont + 1}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())

    while True:
        resp = input('Quer continuar? [S/N]: ').upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break

print('-=' * 30)
print('cod ', end='')
for key in jogador.keys():
    print(f'{key:<15}', end='')
print()
print('-' * 40)

for indice, valor in enumerate(time):
    print(f'{indice:>3} ', end='')
    for dado in valor.values():
        print(f'{str(dado):<15}', end='')
    print()
print('-' * 40)

while True:
    busca = int(input('Mostrar dados de qual jogador? [999 para parar]: '))

    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com o código {busca}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}: ')

        for indice, gols in enumerate(time[busca]["gols"]):
            print(f'   No jogo {indice + 1} fez {gols} gols.')
    print('-' * 40)
print('<< VOLTE SEMPRE! >>')