'''
Crie um programa que gerencie o aproveitamento de um 
jogador de futebol. O programa vai ler o nome do 
jogador e quantas partidas ele jogou. Depois vai 
ler a quantidade de gols feitos em cada partida. 
No final, tudo isso será guardado em um dicionário, 
incluindo o total de gols feitos durante o campeonato.
'''
nome = input('Nome do jogador: ').capitalize()
partidas = int(input(f'Quantas partidas {nome} jogou? '))
gols = []
total_gols = 0
cont = 0
for partida in range(partidas):
    gol = int(input(f'  Quantos gols na partida {partida}? '))
    total_gols += gol
    gols.append(gol)

jogador = {
    'nome': nome,
    'total_partidas': partidas,
    'gols': gols,
    'total': total_gols
}

print('-=' * 30)
print(jogador)
print('-=' * 30)

for key, valor in jogador.items():
    print(f'O campo {key} tem o valor {valor}.')

print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {jogador["total_partidas"]} partidas.')

for gols in jogador['gols']:
    print(' ' * 3, f'=> Na partida {cont}, fez {gols} gols.' )
    cont += 1

print(f'Foi um total de {jogador["total"]} gols.')