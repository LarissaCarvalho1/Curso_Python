'''
Leia o peso de cinco pessoas. No final, mostre 
qual foi o maior e o menor peso lidos
'''
for pessoa in range(1, 6):
    peso = float(input(f'Peso {pessoa}° pessoa: '))

    if pessoa == 1:
        maior_peso = peso
        menor_peso = peso
    else:
        if peso > maior_peso:
            maior_peso = peso
        if peso < menor_peso:
            menor_peso = peso

print(f'O maior peso lido foi de {maior_peso}Kg')
print(f'O menor peso lido foi de {menor_peso}Kg')