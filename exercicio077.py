'''
Crie um programa que tenha uma tupla com várias palavras (não usar acentos). 
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
'''
palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro', 'inovacao', 'tecnologia')

for palavra in palavras:
    palavra_formatada = palavra.upper()
    
    print(f'\nNa palavra {palavra_formatada} temos', end=' ')
    for letra in palavra_formatada:
        if letra in 'AEIOU':
            letra_encontrada = letra.lower()
            print(letra_encontrada, end=' ')
