'''
Leia vários números inteiros pelo teclado. O programa só vai 
parar quando o usuário digitar o valor 999, que é a condição 
de parada. No final, mostre quantos números foram digitados 
e qual foi a soma entre eles (desconsiderando o flag)

'''
cont_numero = soma = 0
while True:
    numero = int(input('Digite um valor [999 para parar]: '))
    
    if numero == 999:
        break

    soma += numero
    cont_numero += 1
print(f'A soma dos {cont_numero} valores foi {soma}!')