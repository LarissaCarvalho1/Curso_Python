'''
Leia o nome e o preço de vários produtos. 
O programa deverá perguntar se o usuário 
vai continuar. No final, mostre: 

A) Qual é o total gasto na compra.
B) Quantos produtos custam mais de R$1000.
C) Qual é o nome do produto mais barato.
'''
total_produtos = 0
total_gasto = 0
total_mil = 0
nome_prod_barato = ''
menor_preco = 0

print('--' * 16)
print(f'{"LOJA SUPER BARATÃO":^30}')
print('--' * 16)

while True:
    nome_produto = input('Nome do Produto: ').strip().title()
    preco = float(input('Preço: R$ '))
    total_produtos += 1
    total_gasto += preco

    if preco > 1000:
        total_mil += 1

    if total_produtos == 1 or preco < menor_preco:
        nome_prod_barato = nome_produto
        menor_preco = preco

    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Quer continuar? [S/N]: ').strip().upper()[0]
    
    if continuar == 'N':
        break
print('=-' * 16)
print(f'{"FIM DO PROGRAMA":^30}')
print(f'O total da compra foi R${total_gasto:.2f}')
print(f'Temos {total_mil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {nome_prod_barato} que custa R${menor_preco:.2f}')