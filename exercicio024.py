# Leia o nome de uma cidade e diga se ela começa ou não com "SANTO"

nome_cidade = input('Qual o nome da cidade? ').strip()
nome_cidade_formatado = nome_cidade.upper()

if nome_cidade_formatado[:5] == 'SANTO':
    print(f'A cidade {nome_cidade} começa com "Santo"')
else:
    print(f'A cidade {nome_cidade} não começa com "Santo"')

