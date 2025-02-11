'''
Escreva um programa para aprovar o empréstimo bancário 
para a compra de uma casa. O programa vai perguntar o 
valor da casa, o salário do comprador e em quantos 
anos ele vai pagar.

Calcule o valor da prestação mensal, sabendo que ela não 
pode exceder 30% do salário ou então o empréstimo será negado.
'''

valor_casa = float(input('Qual o valor da casa? '))
salario_comprador = float(input('Qual o salário do comprador? '))
anos = int(input('Quantos anos de financiamento? '))
minimo = salario_comprador * 30/100
prestacao_mensal = valor_casa / (anos * 12)

print(f'Para pagar uma casa de R${valor_casa:.2f} em {anos} a prestação será de R${prestacao_mensal:.2f}')

if prestacao_mensal > minimo:
    print('Emprétimo NEGADO!')
else:
    print('Emprestimo APROVADO!')

