'''
Leia dois números inteiros e compare-os, 
mostrado na tela uma mensagem:

- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais
'''
primeiro_numero = int(input('Primeiro Número: '))
segundo_numero = int(input('Segundo Número: '))
maior_numero = primeiro_numero

if maior_numero != segundo_numero:
    if maior_numero < segundo_numero:
        maior_numero = segundo_numero
        print(f'O SEGUNDO valor é maior, {maior_numero}')
    else:
        print(f'O PRIMEIRO valor é maior, {maior_numero}')
else:
    print('Não existe valor maior, os dois são iguais')


