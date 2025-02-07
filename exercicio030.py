'''
Leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR
'''
numero = int(input('Digite um número: '))
par_ou_impar = 'PAR' if numero % 2 == 0 else 'ÍMPAR'

print(f'O número {numero} é {par_ou_impar}')