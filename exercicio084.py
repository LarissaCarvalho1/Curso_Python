'''
Leia o nome e o peso de várias pessoas, guardando tudo 
em uma lista. No final, mostre: 

- Quantas pessoas foram cadastradas.
- Uma listagem com as pessoas mais pesadas.
- Uma listagem com as pessoas mais leves.
'''
pessoas = []
dados = []
pesos = []

while True:
    nome = input('Nome: ').title().strip()
    peso = float(input('Peso: '))
    
    dados.append(nome)
    dados.append(peso)
    pessoas.append(dados[:])
    dados.clear()

    resposta = input('Quer continuar? [S/N] ').strip()
    if resposta in 'Nn':
        break

for pessoa in pessoas:
    peso = pessoa[1]
    pesos.append(peso)

total_pessoas = len(pessoas)
maior_peso = max(pesos)
menor_peso = min(pesos)

print(f'-=' * 20)
print(f'Ao todo, você cadastrou {total_pessoas} pessoas.')

print(f'O maior peso foi de {maior_peso}Kg. Peso de', end=' ')
for pessoa in pessoas:
    if pessoa[1] == maior_peso:
        print(f'[{pessoa[0]}]', end=' ')

print(f'\nO menor peso foi de {menor_peso}Kg. Peso de', end=' ')
for pessoa in pessoas:
    if pessoa[1] == menor_peso:
        print(f'[{pessoa[0]}]', end=' ')