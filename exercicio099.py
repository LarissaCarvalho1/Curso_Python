'''
Faça um programa que tenha uma função chamada maior(), 
que receba vários parâmetros com valores inteiros.

Seu programa tem que analisar todos os valores e 
dizer qual deles é o maior.
'''
from time import sleep
def maior(* numeros):
    total = len(numeros)
    maior_num = 0

    print('-=' * 30)
    print('Analisando os valores passados...')
    for numero in numeros:
        print(numero, end=' ', flush=True)
        sleep(0.5)

    if numeros != ():
        maior_num = max(numeros)

    print(f'Foram informados {total} valores ao todo.')
    print(f'O maior valor informado foi {maior_num}.')
    sleep(1)

maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()