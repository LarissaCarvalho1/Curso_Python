'''
Faça o computador "pensar" em um número inteiro entre 0 e 5
e peça para o usuário tentar descobrir qual foi o número 
escolhido pelo computador.

O programa deverá escrever na tela se o usuário venceu ou perdeu.
'''
from random import randint
from time import sleep

print('Tente adivinhar o número em que pensei.')
numero_computador = randint(0, 5)
numero_usuario = int(input('Digite um número entre 0 e 5: '))

print('Analisando sua resposta...')
sleep(2)

if numero_usuario == numero_computador:
    print(f'Parabéns, você VENCEU!')
    print(f'O número pensado foi {numero_computador}')
else:
    print('Poxa, não foi dessa vez...Você PERDEU!')
    print(f'Número pensado: {numero_computador}')