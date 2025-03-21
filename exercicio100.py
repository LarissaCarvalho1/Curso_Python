'''
Faça um programa que tenha uma lista chamada numeros e 
duas funções chamadas sorteia() e somaPar(). A primeira 
função vai sortear 5 números e vai colocá-los dentro da 
lista e a segunda função vai mostrar a soma entre todos 
os valores PARES sorteados pela função anterior.
'''
from random import randint
from time import sleep
numeros = []

def sorteia(lista):
    print('Sorteando 5 valores da lista:', end=' ')
    for cont in range(5):
        numero = randint(1, 10)
        lista.append(numero)
        print(numero, end=' ', flush=True)
        sleep(0.5)
    print('PRONTO!')


def soma_par(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {lista}, temos {soma}')


sorteia(numeros)
soma_par(numeros)
