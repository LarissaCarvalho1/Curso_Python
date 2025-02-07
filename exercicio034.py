'''
Pergunte o salário de um funcionário e calcule o valor do seu
aumento.

Para salários superiores a R$1250,00, calcule um aumento de 10%

Para inferiores ou iguais, o aumento é de 15%
'''

salario_atual = float(input('Qual o salário do funcionário: '))
salario_minimo = 1250
aumento_salario_superior = 1.10
aumento_salario_inferior = 1.15
novo_salario = 0
aumento_total_salario = 0

if salario_atual > salario_minimo:
    novo_salario = salario_atual * aumento_salario_superior
    aumento_total_salario = novo_salario - salario_atual
else:
    novo_salario = salario_atual * aumento_salario_inferior
    aumento_total_salario = novo_salario - salario_atual

print(f'Analisando o salário de R${salario_atual:.2f}...')
print(f'Com o aumento em reais de R${aumento_total_salario:.2f}')
print(f'O novo salário será de R${novo_salario:.2f}')