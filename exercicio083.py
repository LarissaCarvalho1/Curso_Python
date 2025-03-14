'''
Crie um programa onde o usuário digite uma expressão 
qualquer que use parênteses. Seu aplicativo deverá 
analisar se a expressão passada está com os 
parêntese abertos e fechados na ordem 
correta.
'''
expressao = input('Digite a expressão: ').strip()
parenteses_abre = expressao.count('(')
parenteses_fecha = expressao.count(')')

if parenteses_abre == parenteses_fecha:
    print('Sua expressão está VÁLIDA!')
else:
    print('Sua expressão está ERRADA!')