# Leia o preço de um produto e mostre seu novo preço, com 5% de desconto. 
preco_atual = float(input('Preço atual do produto: '))
novo_preco_desconto = preco_atual * 95 / 100
print(f'O produto que custa R$ {preco_atual:.2f} reais, com o desconto de 5%, passará a custar R$ {novo_preco_desconto:.2f} reais.')