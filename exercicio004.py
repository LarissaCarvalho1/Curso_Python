# Leia algo pelo teclado e mostre na tela o seu tipo primitivo
# e todas as informações possíveis sobre ela

informacao = input('Digite qualquer coisa: ')
print(f'O tipo primitivo desse valor é: {type(informacao)}')
print(f'Só tem espaços? {informacao.isspace()}')
print(f'É um número? {informacao.isnumeric()}')
print(f'É alfabético? {informacao.isalpha()}')
print(f'Está em maiúsculas? {informacao.isupper()}')
print(f'Está em minúsculas? {informacao.islower()}')
print(f'Está capitalizada? {informacao.istitle()}')