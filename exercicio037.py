'''
Leia um número inteiro qualquer e peça para o 
usuário escolher qual será a base de conversão:

- 1 para Binário
- 2 para octal
- 3 para hexadecimal
'''
numero = int(input('Digite um número: '))

print('''Escolha uma das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
base_conversao = input('Sua opção: ')

if base_conversao == '1':
    numero_binario = bin(numero)[2:]
    print(f'A representação BINÁRIA do número {numero} é {numero_binario}')
elif base_conversao == '2':
    numero_octal = oct(numero)[2:]
    print(f'A representação OCTAL do número {numero} é {numero_octal}')
elif base_conversao == '3':
    numero_hex = hex(numero)[2:]
    print(f'A representação HEXADECIMAL do número {numero} é {numero_hex}')
else:
    print('Opção inválida! Escolha apenas as opções disponíveis acima')