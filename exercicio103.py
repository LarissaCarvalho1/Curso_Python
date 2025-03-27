'''
Faça um programa que tenha uma função chamada ficha(), 
que recebe dois parâmetros opcionais: o nome de um 
jogador e quantos gols ele marcou.

O programa deverá ser capaz de mostrar a ficha do 
jogador, mesmo que algum dado não tenha sido 
informado corretamente.
'''
def ficha(jogador='<desconhecido>', gol=0):
    return f'O jogador {jogador} fez {gol} gol(s) no campeonato.'


nome = input('Nome do Jogador: ')
gols = input('Número de Gols: ')

if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0

if nome.strip() == '':
    resposta = ficha(gol=gols)
else:
    resposta = ficha(nome, gols)
print(resposta)
