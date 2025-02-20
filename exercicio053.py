'''
Leia uma frase qualquer e diga se ela é um palíndromo, 
desconsiderando os espaços.

Ex.: 
APOS A SOPA
A SACADA DA CASA
A TORRE DA DERROTA
O LOBO AMA O BOLO
ANOTARAM A DATA DA MARATONA
'''

frase = input('Digite uma fase qualquer: ').strip().upper()
lista_palavras_frase = frase.split()
frase_sem_espacos = ''.join(lista_palavras_frase)
frase_invertida_sem_espacos = frase_sem_espacos[::-1]

print(f'O inverso de {frase_sem_espacos} é {frase_invertida_sem_espacos}')
if frase_sem_espacos == frase_invertida_sem_espacos:
    print('Temos um PALÍNDROMO!')
else:
    print('A frase digitada NÃO é um PALÍNDROMO!')