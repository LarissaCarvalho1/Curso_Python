# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada. 

from random import shuffle

aluno1 = input('Primeiro Aluno: ')
aluno2 = input('Segundo Aluno: ')
aluno3 = input('Terceiro Aluno: ')
aluno4 = input('Quarto Aluno: ')
lista_alunos = [aluno1, aluno2, aluno3, aluno4]

print('Lista Original: ')
print(lista_alunos)
print('--' * 24)
shuffle(lista_alunos)
print('Lista embaralhada:')
print(lista_alunos)
