'''
Leia um número n inteiro qualquer e mostre na tela os 
n primeiros elementos de uma Sequência de Fibonacci.

ex.: 0 - 1 - 2 - 3 - 5 - 8
'''
print('--' * 20)
print('Sequência de Fibonacci')
print('--' * 20)

qtd_elemento = int(input('Quantos termos você quer mostrar? '))
primeiro_termo = 0
segundo_termo = 1
cont = 3

print('~~' * 20)
print(f'{primeiro_termo} -> {segundo_termo}', end='')
while cont <= qtd_elemento:
    terceiro_termo = primeiro_termo + segundo_termo
    print(f' -> {terceiro_termo}', end='')
    primeiro_termo = segundo_termo
    segundo_termo = terceiro_termo
    cont += 1
print(' -> FIM')
