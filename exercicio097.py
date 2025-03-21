'''
Faça um programa que tenha uma função chamada escreva(), 
que receba um texto qualquer como parâmetro e mostre 
uma mensagem com tamanho adaptável.

Ex.: escreva('Olá, mundo!')

Saída: 
~~~~~~~~~~~
Olá, mundo!
~~~~~~~~~~~
'''
def escreva(texto):
    tamanho_texto = len(texto) + 4
    print(f'~' * tamanho_texto)
    print(f'  {texto}')
    print('~' * tamanho_texto)


escreva('Gustavo Guanabara')
escreva('Curso de Python no YouTube')
escreva('CeV')