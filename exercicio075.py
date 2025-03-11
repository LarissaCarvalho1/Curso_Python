'''
Leia 4 valores pelo teclado e guarde-os em uma tupla. No final, mostre: 

- Quantas vezes apareceu o valor 9.
- Em que posição foi digitado o primeiro valor 3.
- Quais foram os números pares.
'''
primeiro_valor = int(input('Digite um número: '))
segundo_valor = int(input('Digite outro número: '))
terceiro_valor = int(input('Digite mais um número: '))
quarto_valor = int(input('Digite o último número: '))
valores = (primeiro_valor, segundo_valor, terceiro_valor, quarto_valor)
cont_nove = 0

print(f'Você digitou os valores {valores}')

for valor in valores:
    if valor == 9:
        cont_nove += 1
print(f'O valor 9 apareceu {cont_nove} vezes')

if 3 in valores:
    posicao_tres = valores.index(3) + 1
    print(f'O valor 3 apareceu na {posicao_tres}ª posição.')    
else:
    print('O valor 3 não foi digitado em nenhuma posição.')

print('Os valores pares digitados foram', end=' ')
for valor in valores:
    if valor % 2 == 0:
        print(valor, end=' ')
