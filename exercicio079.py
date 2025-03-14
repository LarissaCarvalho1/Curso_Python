'''
Crie um programa onde o usuário possa digitar 
vários valores numéricos e cadastre-os em uma 
lista. Caso o número já exista lá dentro, 
ele não será adicionado. No final, serão 
exibidos todos os valores únicos 
digitados, em ordem crescente.
'''
valores = []
resposta = 'S'
while True:
    valor = int(input('Digite um valor: '))
    
    if valor not in valores:
        valores.append(valor)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')

    resposta = input('Quer continuar? [S/N]: ').strip().upper()
    if resposta == 'N':
        break
valores.sort()
print(f'-=' * 20)
print(f'Você digitou os valores {valores}')