'''
Leia nome, sexo e idade de várias pessoas, guardando 
os dados de cada pessoa em um dicionário e todos os 
dicionários em uma lista. No final, mostre: 

- Quantas pessoas foram cadastradas
- A média de idade do grupo
- Uma lista com todas as mulheres
- Uma lista com todas as pessoas com idade 
acima da média
'''
pessoas = []
while True:
    nome = input('Nome: ').strip().capitalize()
    sexo = input('Sexo [M/F]: ').strip().upper()
    while sexo not in 'MF':
        print('ERRO! Por favor, digite apenas M ou F.')
        sexo = input('Sexo [M/F]: ').strip().upper()

    idade = int(input('Idade: '))

    pessoa = {
        'nome': nome,
        'sexo': sexo,
        'idade': idade,
    }
    pessoas.append(pessoa.copy())

    respo = input('Quer continuar? [S/N]: ').strip()

    while respo not in 'SsNn':
        print('ERRO! Responda apenas S ou N.')
        respo = input('Quer continuar? [S/N]: ').strip()
    
    if respo in 'Nn':
        break

total_pessoas = len(pessoas)
soma_idade = 0

for pessoa in pessoas:
    soma_idade += pessoa["idade"]

media_idade = soma_idade / total_pessoas

print('-=' * 30)
print(f'A) Ao todo temos {total_pessoas} pessoas cadastradas.')
print(f'B) A média de idade é de {media_idade:.2f} anos.')
print('C) As mulheres cadastradas foram:', end=' ')
for pessoa in pessoas:
    if pessoa['sexo'] == 'F':
        print(f'{pessoa["nome"]},', end=' ')
print()
print('D) Lista das pessoas que estão acima da média:')
for pessoa in pessoas:
    if pessoa["idade"] >= media_idade:
        print('    ', end='')
        for key, valor in pessoa.items():
            print(f'{key.capitalize()} = {valor};', end=' ')
        print()
print('<< ENCERRADO >>')