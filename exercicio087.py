'''
Aprimore o desafio anterior, mostrando no final: 

- A soma de todos os valores pares.
- A soma dos valores da terceira coluna.
- O maior valor da segunda linha.
'''
valores = []
dados = []
soma_terceira_coluna = 0
soma_pares = 0

for cont_linha in range(0, 3):
    for cont_coluna in range(0, 3):
        valor = int(input(f'Digite um valor para [{cont_linha}, {cont_coluna}]: '))
        dados.append(valor)

        if valor % 2 == 0:
            soma_pares += valor

    valores.append(dados[:])
    dados.clear()

print(f'-=' * 20)
for cont in range(0, 3):
    print(f'[{valores[cont][0]:^5}][{valores[cont][1]:^5}][{valores[cont][2]:^5}]')

    soma_terceira_coluna += valores[cont][2]

maior = max(valores[1])

print(f'-=' * 20)
print(f'A soma dos valores pares é {soma_pares}')
print(f'A soma dos valores da terceira coluna é {soma_terceira_coluna}')
print(f'O maior valor da segunda linha é {maior}')
