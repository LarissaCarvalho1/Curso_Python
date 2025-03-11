'''
Crie um programa que tenha uma tupla totalmente 
preenchida com uma contagem por extenso, de 
zero até vinte.

Seu programa deverá ler um número pelo teclado 
(entre 0 e 20) e mostrá-lo por extenso.
'''
lista_numeros_por_extenso = ('zero', 'um', 'dois', 'três', 'quatro', 
                            'cinco', 'seis', 'sete', 'oito', 'nove', 
                            'dez', 'onze', 'doze', 'treze', 'quatorze', 
                            'quinze', 'dezesseis', 'dezessete', 'dezoito', 
                            'dezenove', 'vinte')

while True:
    numero_lido = int(input('Digite um número entre 0 e 20: '))

    if numero_lido in range(0, 21):
        numero_extenso = lista_numeros_por_extenso[numero_lido].upper()
        break
    else:
        print('Tente novamente.')

print(f'Você digitou o número {numero_extenso}')