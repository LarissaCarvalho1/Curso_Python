'''
Leia uma frase pelo teclado e mostre:

- Quantas vezes apareceu a letra "A"
- Em que posição ela aparece a primeira vez
- Em que posição ela aparece a última vez
'''

frase = input('Digite uma frase: ').strip()
frase_formatada = frase.upper()
conta_a = frase_formatada.count('A')
primeira_ocorrencia_a = frase_formatada.find('A') + 1
ultima_ocorrencia_a = frase_formatada.rfind('A') + 1


print(f'Analisando a frase "{frase}"...')
print(f'A letra "A" apareceu {conta_a}x na frase')
print(f'A primeira ocorrência de "A" foi na posição {primeira_ocorrencia_a}')
print(f'A última ocorrência de "A" foi na posição {ultima_ocorrencia_a}')
