'''
Pergunte a distância de uma viagem em km. Calcule o preço da 
passagem, cobrando R$0,50 por km para viagens de até 200km
e R$0,45 para viagens mais longas.
'''
distancia_km = float(input('Distância da viagem em km: '))
valor_por_km_1 = 0.50
valor_por_km_2 = 0.45
preco_passagem = 0

if distancia_km <= 200:
    preco_passagem = distancia_km * valor_por_km_1
else:
    preco_passagem = distancia_km * valor_por_km_2

print(f'Você está prestes a começar uma viagem de {distancia_km}km.')
print(f'E o preço da passagem para esta viagem será de R${preco_passagem:.2f}')