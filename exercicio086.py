'''
Crie um programa que crie uma matriz de dimensão 3x3 
e preencha com valores lidos pelo teclado.
No final, mostre a matriz na tela, com a 
formatação correta.
'''
# Minha solução
# valores = []
# dados = []

# for cont_linha in range(0, 3):
#     for cont_coluna in range(0, 3):
#         valor = input(f'Digite um valor para [{cont_linha}, {cont_coluna}]: ')
#         dados.append(valor)
#     valores.append(dados[:])
#     dados.clear()

# print('-=' * 20)

# for cont in range(0, 3):
#     print(f'[{valores[cont][0]:^5}][{valores[cont][1]:^5}][{valores[cont][2]:^5}] ')

# Solução professor
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: '))

print('-=' * 30)

for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()