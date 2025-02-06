'''
Leia o nome completo de uma pessoa e mostre: 

- Nome com todas as letras maiúsculas 
- Nome com todas as letras minúsculas 
- Quantas letras ao todo (sem considerar espaços)
- Quantas letras tem o primeiro nome
'''
nome = input('Digite seu nome completo: ')
nome_maiusculo = nome.upper()
nome_minusculo = nome.lower()
lista_palavras_nome = nome.split()
tamanho_primeiro_nome = len(lista_palavras_nome[0])
juntar_palavras = ''.join(lista_palavras_nome)
tamanho_nome_completo = len(juntar_palavras)

print('Analisando seu nome...')
print(f'Seu nome com letras MAIÚSCULAS: {nome_maiusculo}')
print(f'Seu nome com letras minúsculas: {nome_minusculo}')
print(f'Seu nome ao todo tem {tamanho_nome_completo} letras')
print(f'Seu primeiro nome é {lista_palavras_nome[0]} e tem {tamanho_primeiro_nome} letras')
