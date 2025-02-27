'''
Jogue par ou ímpar com o computador. O jogo só será 
interrompido quando o jogador PERDER, mostrando o 
total de vitórias consecutivas que ele 
conquistou no final do jogo.
'''
from random import randint
vitorias_consecutivas = soma = 0
escolha_jogador = escolha_computador = ''

print('=-' * 15)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-' * 15)

while True:
    num_computador = randint(0, 10)
    num_jogador = int(input('Diga um valor: '))
    escolha_jogador = input('Par ou Ímpar? [P/I]').strip().upper()

    # Decide escolha do computador
    if escolha_jogador == 'P':
        escolha_computador = 'I'
    elif escolha_jogador == 'I':
        escolha_computador = 'P'

    # Soma e decide se par ou ímpar
    soma = num_computador + num_jogador
    if soma % 2 == 0:
        par_impar = 'PAR'
    else:
        par_impar = 'ÍMPAR'
    
    print('--' * 15)
    print(f'Você jogou {num_jogador} e o computador {num_computador}.')
    print(f'Total de {soma} deu {par_impar}.')
    print('--' * 15)

    # Quem venceu
    if par_impar[0] == escolha_jogador:
        vitorias_consecutivas += 1
        print('Você VENCEU!')
        print('Vamos jogar novamente...')
    else:
        print('Você PERDEU!')
        break
    print('-=' * 15)
print('-=' * 15)
print(f'GAME OVER! Você venceu {vitorias_consecutivas} vezes.')  
