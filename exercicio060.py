'''
Faça um programa que leia um número qualquer e mostre o seu fatorial

ex.: 
5! = 5x4x3x2x1 = 120
'''
from math import factorial
# Primeira Solução com Módulo math + factorial
# n = int(input('Digite um número para calcular seu Fatorial: '))
# f = factorial(n)
# print(f'O Fatorial de {n} é {f}.')

# Segunda resolução utilizando lógica matemática
contador = 0
print('Calculadora Fatorial')
numero = int(input('Digite um número: '))
contador = numero
fatorial = 1
print(f'Calculando {numero}! =', end=' ')
while contador > 0:
    print(f'{contador}', end='')
    print(' x ' if contador > 1 else ' = ', end='')
    fatorial *= contador
    contador -= 1
print(fatorial)

