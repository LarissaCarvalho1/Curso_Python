'''
Leia um ano qualquer e mostre se ele é BISSEXTO.

Se final não for 00 e múltiplo de 4 e não múltiplo de 100 -> bissexto
Se final for 00, múltiplo de 4, 100 e 400 -> bissexto
Se final for 00, múltiplo de 4 e 100, não de 400 -> Não bissexto 
'''
from datetime import date

ano = int(input('Qual ano quer analisar? Coloque 0 para analisar o ano atual: '))

if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é BISSEXTO.')
else:
    print(f'O ano {ano} NÃO é BISSEXTO.')


# ano_digitado_str = input('Digite um ano: ')
# ano_digitado_int = int(ano_digitado_str)
# dois_ultimos_digitos = ''
# bissexto_nao_bissexto = 'NÃO é BISSEXTO'

# if ano_digitado_str.isnumeric() and len(ano_digitado_str) == 4:
#     dois_ultimos_digitos = ano_digitado_str[2:]
# else:
#     print(f'{ano_digitado_str} não é um valor válido!')

# if dois_ultimos_digitos != '00':
#     if ano_digitado_int % 4 == 0 and ano_digitado_int % 100 != 0:
#         # bissexto_nao_bissexto = 'é BISSEXTO'
#         print(f'O ano {ano_digitado_int} é BISSEXTO!')
#     else:
#         print(f'O ano {ano_digitado_int} NÃO é BISSEXTO!')
# else:
#     if ano_digitado_int % 4 == 0 and ano_digitado_int % 100 == 0 and ano_digitado_int % 400 == 0:
#         # bissexto_nao_bissexto = 'é BISSEXTO'
#         print(f'O ano {ano_digitado_int} é BISSEXTO!')
#     else:
#         print(f'O ano {ano_digitado_int} NÃO é BISSEXTO!')