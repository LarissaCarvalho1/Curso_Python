'''
Calcule o valor a ser pago por um produto, considerado o seu 
preço normal e condição de pagamento:

- À vista dinheiro/cheque: 10% de desconto
- À vista no cartão: 5% de desconto
- Em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros

'''
formas_pagamento = ['à vista no dinheiro/cheque', 'à vista no cartão', 'em até 2x no cartão', 'em 3x ou mais no cartão']
preco_atual = float(input('Preço das compras: '))

print('-=' * 20)
print('''Formas de Pagamento Disponíveis:
[ 0 ] Dinheiro/Cheque
[ 1 ] À vista no cartão
[ 2 ] Em até 2x no cartão
[ 3 ] 3x ou mais no cartão''')
print('-=' * 20)
forma_pagamento = int(input('Escolha a forma de pagamento: '))
preco_a_pagar = ''

if forma_pagamento == 0:
    preco_a_pagar = preco_atual * 90/100
    print(f'Com o pagamento {formas_pagamento[forma_pagamento]}, você terá 10% de desconto e pagará R${preco_a_pagar:.2f}')
elif forma_pagamento == 1:
    preco_a_pagar = preco_atual * 95/100
    print(f'Com o pagamento {formas_pagamento[forma_pagamento]}, você terá 5% de desconto e pagará R${preco_a_pagar:.2f}')
elif forma_pagamento == 2:
    preco_a_pagar = preco_atual
    print(f'Com o pagamento {formas_pagamento[forma_pagamento]}, você pagará R${preco_a_pagar:.2f}')
elif forma_pagamento == 3:
    preco_a_pagar = preco_atual * 120/100
    print(f'Com o pagamento {formas_pagamento[forma_pagamento]}, terá um acrescimo de 20% sobre o valor original e você pagará R${preco_a_pagar:.2f}')
else:
    print('Opção Inválida/Não Disponível!')