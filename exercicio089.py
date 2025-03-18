'''
Leia nome e duas notas de vários alunos e guarde tudo em uma 
lista composta. No final, mostre um boletim contendo a média 
de cada um e permita que o usuário possa mostrar as notas de 
cada aluno individualmente.
'''
ficha = list()

while True:
    nome = input('Nome: ')
    primeira_nota = float(input('Nota 1: '))
    segunda_nota = float(input('Nota 2: '))
    media = (primeira_nota + segunda_nota) / 2
    ficha.append([nome, [primeira_nota, segunda_nota], media])

    resp = input('Quer continuar? [S/N]: ')
    if resp in 'Nn':
        break

print('-=' * 30)
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 26)

for indice, aluno in enumerate(ficha):
    print(f'{indice:<4}{aluno[0]:<10}{aluno[2]:>8.1f}')

while True:
    print('-' * 35)
    opcao = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opcao == 999:
        print('FINALIZANDO...')
        break
    if opcao <= len(ficha) - 1:
        print(f'Notas de {ficha[opcao][0]} são {ficha[opcao][1]}')
print('<<< VOLTE SEMPRE >>>')