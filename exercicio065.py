'''
Leia vários numeros inteiros pelo teclado. No final da execução, 
mostre a média entre todos os valores e qual foi o maior e o 
menor valores lidos. O programa deve perguntar ao usuário 
se ele quer ou não continuar a digitar valores.
'''
continuar = 'S'
soma = 0
cont = 0

while continuar != 'N':
    numero = int(input('Digite um númmero: '))
    soma += numero
    cont += 1

    if cont == 1:
        maior = numero
        menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero

    continuar = input('Quer continuar? [S/N] ').strip().upper()

media = soma / cont

print(f'Você digitou {cont} números e a média foi {media}')
print(f'O maior valor foi {maior} e o menor foi {menor}')
