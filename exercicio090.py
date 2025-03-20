'''
Leia nome e média de um aluno, guardando também a 
situação em um dicionário. No final, mostre o 
conteúdo da estrutura na tela.

'''
nome = input('Nome: ').strip().title()
media = float(input(f'Média de {nome}: '))

if media <= 5:
    situacao = 'Reprovado'
elif media < 7:
    situacao = 'Recuperação'
else:
    situacao = 'Aprovado'

pessoa = {
    'nome': nome,
    'media': media,
    'situacao': situacao
}

print('-=' * 30)
for key, valor in pessoa.items():
    print(f'- {key.capitalize()} é igual a {valor}')

