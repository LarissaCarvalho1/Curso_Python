'''
Simule o funcionamento de um caixa eletrônico. 
No início, pergunte ao usuário qual será o valor
a ser sacado (número inteiro) e o programa vai 
informar quantas cédulas de cada valor serão 
entregues.

obs: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1
'''
print('=' * 30)
print(f'{"BANCO LC":^30}')
print('=' * 30)
valor = int(input('Que valor você quer sacar? '))
montante = valor
cedula_atual = 50
total_cedula = 0

while True:
    if montante >= cedula_atual:
        total_cedula = montante // cedula_atual
        montante -= total_cedula * cedula_atual
    else:
        if total_cedula > 0:
            print(f'Total de {total_cedula:.0f} cédulas de R${cedula_atual}')
        if cedula_atual == 50:
            cedula_atual = 20
        elif cedula_atual == 20:
            cedula_atual = 10
        elif cedula_atual == 10:
            cedula_atual = 1

        if montante == 0:
            break

print('=' * 30)
print('Volte sempre ao BANCO LC! Tenha um bom dia!')
