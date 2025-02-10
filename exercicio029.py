'''
Leia a velocidade de um carro.

Se ela ultrapassar 80km/h, mostre uma mensagem dizendo que ele
foi multado.

A multa vai custar R$ 7,00 por km acima do limite.
'''
velocidade_carro = float(input('Velocidade atual do carro (Km): '))
velocidade_maxima_via = 80
km_acima_limite = 0
multa_km_acima_limite = 7
multa_total = 0

if velocidade_carro > velocidade_maxima_via:
    km_acima_limite = velocidade_carro - velocidade_maxima_via
    multa_total = km_acima_limite * multa_km_acima_limite
    
    print(f'Você foi MULTADO! O carro está acima do limite de {velocidade_maxima_via}km/h permitido na via. ')
    print(f'Valor da Multa: R$ {multa_total:.2f}')
print('Boa viagem!')