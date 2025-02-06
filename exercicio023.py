'''
Leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

ex.:
Digite um número: 1834
Unidade: 4
Dezena: 3
centena: 8
milhar: 1
'''
numero_digitado = input('Digite um número entre 0 e 9999: ')
numero_digitado_int = int(numero_digitado)
tamanho_numero_digitado = len(numero_digitado)
dezena = '0'
centena = '0' 
milhar = '0'

# Modo matemático
unidade = numero_digitado_int // 1 % 10
dezena = numero_digitado_int // 10 % 10
centena = numero_digitado_int // 100 % 10
milhar = numero_digitado_int // 1000 % 10
print(f'Unidade: {unidade}')
print(f'Dezena: {dezena}')
print(f'Centena: {centena}')
print(f'Milhar: {milhar}')

# Modo string
# if tamanho_numero_digitado == 4:
#     print(f'Unidade: {numero_digitado[3]}')
#     print(f'Dezena: {numero_digitado[2]}')
#     print(f'Centena: {numero_digitado[1]}')
#     print(f'Milhar: {numero_digitado[0]}')
# elif tamanho_numero_digitado == 3:
#     print(f'Unidade: {numero_digitado[2]}')
#     print(f'Dezena: {numero_digitado[1]}')
#     print(f'Centena: {numero_digitado[0]}')
#     print(f'Milhar: {milhar}')
# elif tamanho_numero_digitado == 2:
#     print(f'Unidade: {numero_digitado[1]}')
#     print(f'Dezena: {numero_digitado[0]}')
#     print(f'Centena: {centena}')
#     print(f'Milhar: {milhar}')
# elif tamanho_numero_digitado == 1:
#     print(f'Unidade: {numero_digitado[0]}')
#     print(f'Dezena: {dezena}')
#     print(f'Centena: {centena}')
#     print(f'Milhar: {milhar}')
# else:
#     print('O campo não pode estar vazio!')


