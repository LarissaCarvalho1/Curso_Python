# Leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. 

# Considere: US$1,00 = R$ 3,27

dinheiro_real = float(input('Quanto dinheiro você tem na carteira? R$ '))
convesao_dolar = dinheiro_real / 3.27
print(f'Com R${dinheiro_real:.2f} você pode comprar US${convesao_dolar:.2f}')