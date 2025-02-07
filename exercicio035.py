'''
Leia o comprimento de três retas e diga ao usuário se elas 
podem ou não formar um triângulo.

a + b > c
a + c > b
b + c > a
'''
print('Informe os comprimentos das retas: ')
primeira_reta = int(input('Primeira reta: '))
segunda_reta = int(input('Segunda reta: '))
terceira_reta = int(input('Terceira reta: '))
triangulo_nao_triangulo = 'NÃO formam TRIÂGULO'

if (primeira_reta + segunda_reta > terceira_reta) and (primeira_reta + terceira_reta > segunda_reta) and (segunda_reta + terceira_reta > primeira_reta):
    triangulo_nao_triangulo = 'formam TRIÂNGULO'

print(f'As retas com comprimentos {primeira_reta}, {segunda_reta} e {terceira_reta} {triangulo_nao_triangulo}')
