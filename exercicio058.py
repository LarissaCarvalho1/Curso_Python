'''
Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em
número entre 0 e 10. Só que agora o jogador vai tentar
adivinhar até acertar, mostrando no final quantos 
palpites foram necessários para vencer.
'''
from random import randint
numero_computador = randint(0, 10)

print('Sou seu computador...')
print('Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')
acertou = False
total_tentativas = 0

while not acertou:
    numero_jogador = int(input('Qual é seu palpite? '))
    total_tentativas += 1
    if numero_jogador == numero_computador:
        acertou = True
    else:
        if numero_jogador > numero_computador:
            print('Menos... Tente mais uma vez.')
        else:
            print('Mais... Tente mais uma vez.')
print(f'Acertou com {total_tentativas} tentativas. Parabéns!')
