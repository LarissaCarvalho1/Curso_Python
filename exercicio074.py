'''
Crie um programa que vai gerar cinco números aleatórios 
e colocar em uma tupla.

Depois disso, mostre a listagem de números gerados e também 
indique o menor e o maior valor que estão na tupla
'''
from random import randint

numeros_aleatorios = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
maior = max(numeros_aleatorios)
menor = min(numeros_aleatorios)

print('Os valores sorteados foram:', end=' ')
for numero in numeros_aleatorios:
    print(numero, end=' ')

print(f'\nO maior valor sorteado foi: {maior}')
print(f'O menor valor sorteado foi: {menor}')
