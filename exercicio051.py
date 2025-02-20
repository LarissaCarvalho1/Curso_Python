'''
Leia o primeiro termo e a razão de uma PA. No final, 
mostre os 10 primeiros termos dessa progressão.
'''
primeiro_termo_pa = int(input('Primeiro termo: '))
razao_pa = int(input('Razão: '))
decimo = primeiro_termo_pa + (10 - 1) * razao_pa

for contador in range(primeiro_termo_pa, decimo + razao_pa, razao_pa):
    print(contador, end=' -> ')
print('ACABOU!')