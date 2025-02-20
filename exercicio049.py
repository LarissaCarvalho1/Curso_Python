'''
Refaça o DESAFIO 9, mostrando a tabuada de um número 
que o usuário escolher, só que agora utilizando um laço for
'''
tabuada = int(input('Digite um número para ver sua tabuada: '))

print(f'Trabuada do número {tabuada}')
print('--' * 10)
for contador in range(1, 11):
    print(f'{tabuada}  x {contador:2} = {tabuada * contador:2}')
print('--' * 10)