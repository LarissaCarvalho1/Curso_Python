'''
Calcule a soma entre todos os números ímpares que são 
múltiplos de três e que se encontram no intervalo de 1 até 500
'''
soma = 0
cont = 0
for contador in range(1, 501, 2):
    if contador % 3 == 0:
        cont += 1
        soma += contador
print(f'A soma entre todos os {cont} números ímpares, que são múltiplos de três,\nno intervalo de 1 a 500 é ', end='')
print(soma)