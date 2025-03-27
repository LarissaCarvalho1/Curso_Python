'''
Crie um programa que tenha a função leiaInt(), que vai 
funcionar de forma semelhante à função input() do Python, 
só que fazendo a validação para aceitar apenas um valor numérico.

ex: 
n = leiaInt('Digite um n')
'''
def leia_int(mensagem):
    ok = False
    numero = 0

    while True:
        valor = input(mensagem)
        if valor.isnumeric():
            numero = int(valor)
            ok = True
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
        if ok:
            break
    return numero


# Programa principal
valor = leia_int('Digite um número: ')
print(f'Você acabou de digitar o número {valor}')
