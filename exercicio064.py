'''
Leia vários números inteiros pelo teclado. O programa só vai parar 
quando o usuário digitar o valor 999, que é a condição de parada. 
No final, mostre quantos números foram digitados e qual foi a 
soma entre eles (desconsiderando o flag)
'''
# Minha solução
# parada = False
# resultado = 0
# qtd_numeros = 0

# while parada != True:
#     numero = int(input('Digite um número [999 para parar]: '))
#     if numero == 999:
#         parada = True
#         break
#     resultado += numero
#     qtd_numeros += 1
# print(f'Você digitou {qtd_numeros} números e a soma entre eles foi {resultado}')

# Solução professor 
num =  cont = soma = 0
num = int(input('Digite um número [999 para parar]: '))
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um número [999 para parar]: ')) 
print(f'Você digitou {cont} números e a soma entre eles foi {soma}')