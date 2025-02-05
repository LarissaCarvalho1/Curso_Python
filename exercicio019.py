# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. 
# Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido. 
import random

aluno1 = input('Nome do 1° Aluno: ')
aluno2 = input('Nome do 2° Aluno: ')
aluno3 = input('Nome do 3° Aluno: ')
aluno4 = input('Nome do 4° Aluno: ')
lista_alunos = [aluno1, aluno2, aluno3, aluno4]
escolhido = random.choice(lista_alunos)
print(f'O aluno(a) escolhido foi {escolhido}')

