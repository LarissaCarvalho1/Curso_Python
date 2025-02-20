'''
Leia seis números inteiros e mostre a soma apenas daqueles 
que forem pares. Se o valor digitado por ímpar, desconsidere-o.
'''
soma = 0
cont = 0
for contador in range(0, 6):
    numero = int(input(f'Digite o {contador + 1}° número:'))

    if numero % 2 == 0:
        soma += numero
        cont += 1
print(f'A soma dos {cont} números PARES acima é {soma}')
