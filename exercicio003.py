# Leia dois números e mostre a soma entre eles

num1 = input('Primeiro número: ')
num2 = input('Segundo número: ')
if num1.isnumeric() and num2.isnumeric():
    num1_formatado = int(num1)
    num2_formatado = int(num2)
    resultado = num1_formatado + num2_formatado
    print(f'A soma entre {num1_formatado} e {num2_formatado} é {resultado}')
else:
    print('Não foi possível realizar a soma. Digite apenas números.')