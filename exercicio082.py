'''
Crie um programa que vai ler vários números 
e colocar em uma lista.

Depois disso, crie duas listas extras que 
vão conter apenas pares e os ímpares
digitados, respectivamente.

Ao final, mostre o conteúdo das três 
listas geradas.
'''
numeros = []
numeros_par = []
numeros_impar = []

while True:
    numero = int(input('Digite um número: '))
    numeros.append(numero)

    while True:
        resposta = input('Quer continuar? [S/N] ').upper()
        if resposta not in 'SN':
            print('Digite apena "S" e "N" para continuar ou sair.')
        else:
            break
    
    if resposta == 'N':
        break

for numero in numeros:
    if numero % 2 == 0:
        numeros_par.append(numero)
    else:
        numeros_impar.append(numero)
        
print(f'-=' * 20)
print(f'A lista completa é {numeros}')
print(f'A lista de pares é {numeros_par}')
print(f'A lista de ímpares é {numeros_impar}')