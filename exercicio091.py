'''
Crie um programa onde 4 jogadores joguem um 
dado e tenham resultados aleatórios. Guarde 
esses resultados em um dicionário em ordem, 
sabendo que o vencedor tirou o maior 
número no dado.
'''
from random import randint
from time import sleep
from operator import itemgetter

jogo = {
    'jogador1': randint(1, 6),
    'jogador2': randint(1, 6),
    'jogador3': randint(1, 6),
    'jogador4': randint(1, 6),
}

# ranking = sorted(jogo.items(), key=lambda x: x[1], reverse=True)

ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)

print('Valores sorteados:')
for key, valor in jogo.items():
    print(' ' * 3, f'O {key} tirou {valor} no dado.')
    sleep(1)

print('-=' * 30)
print('Ranking dos jogadores:')
for posicao, valor in enumerate(ranking):
    print(' ' * 3, f'{posicao + 1}º lugar: {valor[0]} com {valor[1]}')
    sleep(1) 