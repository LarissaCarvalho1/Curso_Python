'''
Leia o comprimento de três retas e diga ao usuário se elas 
podem ou não formar um triângulo.

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
triangulo_nao_triangulo = 'NÃO PODEM FORMAR Triângulo!'

if (primeira_reta + segunda_reta > terceira_reta) and (primeira_reta + terceira_reta > segunda_reta) and (segunda_reta + terceira_reta > primeira_reta):
    triangulo_nao_triangulo = 'PODEM FORMAR triângulo!'

print(f'Os segmentos acima {triangulo_nao_triangulo}')
