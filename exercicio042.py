'''
Refaça o desafio 035 dos triângulos, acrescentando o 
recurso de mostrar que tipo de triângulo será formado: 

- Equilátero: todos os lados iguais
- Isósceles: dois lados iguais
- Escaleno: todos os lados diferentes 

a + b > c
a + c > b
b + c > a

'''
print('-=' * 20)
print('Analisador de Triângulos')
print('-=' * 20)

primeira_reta = float(input('Primeira reta: '))
segunda_reta = float(input('Segunda reta: '))
terceira_reta = float(input('Terceira reta: '))
tipo_triangulo = ''

if (primeira_reta + segunda_reta > terceira_reta) and (primeira_reta + terceira_reta > segunda_reta) and \
   (segunda_reta + terceira_reta > primeira_reta):
    
    if primeira_reta == segunda_reta == terceira_reta:
        tipo_triangulo = 'EQUILÁTERO'
    elif primeira_reta != segunda_reta != terceira_reta != primeira_reta:
        tipo_triangulo = 'ESCALENO'
    else:
        tipo_triangulo = 'ISÓSCELES'
    
    print(f'Os segmentos acima PODEM FORMAR um triângulo {tipo_triangulo}')
else:
    print('Os segmentos acima NÃO PODEM FORMAR Triângulo!')



