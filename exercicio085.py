'''
Crie um programa onde o usuário possa digitar sete 
valores numéricos e cadastre-os em uma lista única 
que mantenha separados os valores pares e ímpares. 
No final, mostre os valores pares e ímpares em 
ordem crescente.
'''
valores = [[], []]

for cont in range(1, 8):
    valor = int(input(f'Digite o {cont}º valor: '))

    if valor % 2 == 0:        
        valores[0].append(valor)
    else:        
        valores[1].append(valor)

print(f'-=' * 20)
print(f'Os valores pares digitados foram:', end=' ')
valores[0].sort()
print(valores[0])

print(f'Os valores ímpares digitados foram:', end=' ')
valores[1].sort()
print(valores[1])
