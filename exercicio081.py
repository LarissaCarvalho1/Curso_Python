'''
Crie um programa que vai ler vários números 
e colocar em uma lista. 

Depois disso, mostre: 

- Quantos números foram digitados
- A lista de valores, ordenada de forma 
decrescente.
- Se o valor 5 foi digitado e está ou 
não na lista.
'''
numeros = []

while True:
    numero = int(input('Digite um valor: '))
    numeros.append(numero)

    while True:
        resposta = input('Quer continuar? [S/N] ').strip().upper()
        if resposta not in 'SN':
            print('Digite apenas "S" ou "N" para continuar ou sair.')
        else:
            break

    if resposta == 'N':
        break

total_numeros = len(numeros)
numeros.sort(reverse=True)

print(f'-=' * 20)
print(f'Você digitou {total_numeros} elementos.')
print(f'Os valores em ordem decrescente são {numeros}')

if 5 in numeros:
    print(f'O valor 5 faz parte da lista!')
else:
    print(f'O valor 5 NÃO foi encontrado na lista!')
    