'''
Leia três números e mostre qual é o maior e qual é o menor
'''
primeiro_numero = int(input('Primeiro número: '))
segundo_numero = int(input('Segundo número: '))
terceiro_numero = int(input('Terceiro número: '))

maior_numero = primeiro_numero
menor_numero = primeiro_numero

if segundo_numero > maior_numero and segundo_numero > terceiro_numero:
    maior_numero = segundo_numero
elif terceiro_numero > maior_numero:
    maior_numero = terceiro_numero

if segundo_numero < menor_numero and segundo_numero < terceiro_numero:
    menor_numero = segundo_numero
elif terceiro_numero < menor_numero:
    menor_numero = terceiro_numero

print(f'O MAIOR número entre {primeiro_numero}, {segundo_numero} e {terceiro_numero} é {maior_numero}')
print(f'O MENOR número entre {primeiro_numero}, {segundo_numero} e {terceiro_numero} é {menor_numero}')


