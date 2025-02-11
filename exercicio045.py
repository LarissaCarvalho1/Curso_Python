'''
Crie um programa que faça o computador jogar Jokenpô com você

'''
from time import sleep
import random

jokenpo = ['Pedra', 'Papel', 'Tesoura']
escolha_computador = random.choice(jokenpo)

print('Suas opções: \n[ 0 ] PEDRA\n[ 1 ] PAPEL\n[ 2 ] TESOURA')
escolha_jogador = input('Qual é a sua jogada? ')

if escolha_jogador in ['0', '1', '2']:
    escolha_jogador = jokenpo[int(escolha_jogador)]

    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO!!!')

    print('-=' * 20)
    print(f'Computador jogou {escolha_computador}')
    print(f'Jogador jogou {escolha_jogador}')
    print('-=' * 20)

    if escolha_jogador == escolha_computador:
        vencedor = 'EMPATE!'
    elif(escolha_jogador == 'Pedra' and escolha_computador == 'Tesoura') or \
        (escolha_jogador == 'Papel' and escolha_computador == 'Pedra') or \
        (escolha_jogador == 'Tesoura' and escolha_computador == 'Papel'):
        vencedor = 'JOGADOR VENCE'
    else:
        vencedor = 'COMPUTADOR VENCE'
    print(vencedor)
else:
    print('Valor Inválido!')