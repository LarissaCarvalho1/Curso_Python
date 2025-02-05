# Leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
salario_atual = float(input('Salário atual do funcionário: '))
novo_salario_aumento = salario_atual * 115 / 100
print(f'O funcionário que recebia R${salario_atual:.2f} reais, com o aumento de 15%, passará a receber R$ {novo_salario_aumento:.2f} reais.')