'''
Leia o nome completo de uma pessoa, mostre em seguida o primeiro e o último nome separadamente.

Ex.: Ana Maria de Souza
primeiro: Ana
último: Souza
'''
nome = input('Seu nome completo: ').strip()
lista_palavra_nome = nome.split()
primeiro_nome = lista_palavra_nome[0]
ultimo_nome = lista_palavra_nome[-1]

print('Muito prazer em te conhecer!')
print(f'Seu primeiro nome é {primeiro_nome}')
print(f'Seu último nome é {ultimo_nome}')