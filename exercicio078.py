'''
Leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor 
valor digitado e as suas respectivas 
posições na lista.

'''
valores = []

for cont in range(5):
    valor = int(input(f'Digite um valor para a posição {cont}: '))
    valores.append(valor)
print(f'Você digitou os valores {valores}')

maior = max(valores)
menor = min(valores)

print(f'O maior valor digitado foi {maior} nas posições', end=' ')
for posicao, valor in enumerate(valores):
    if valor == maior:
        print(f'{posicao}...', end=' ')

print(f'\nO menor valor digitado foi {menor} nas posições', end=' ')
for posicao, valor in enumerate(valores):
    if valor == menor:
        print(f'{posicao}...', end=' ')
