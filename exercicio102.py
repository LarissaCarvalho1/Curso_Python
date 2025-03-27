'''
Crie um programa que tenha uma função fatorial() que receba 
dois parâmetros: o primeiro que indique o número a calcular 
e o outro chamado show, que será um valor lógico (opcional) 
indicando se será mostrado ou não na tela o processo de 
cálculo do fatorial.
'''
def fatorial(numero, show=False):
    '''
    -> Calcula o Fatorial de um número.
    :param numero: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor Fatorial de um número. 
    '''
    print('-' * 25)
    contador = numero
    tot_fatorial = 1
    while contador > 0:
        if show:
            print(contador, end='')
            print(' x ' if contador > 1 else ' = ', end='')
        tot_fatorial *= contador
        contador -= 1
    return tot_fatorial


# Programa principal
print(fatorial(5, True))
# help(fatorial)