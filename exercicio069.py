'''
Leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, 
o programa deverá perguntar se o usuário quer ou não continuar. 
No final, mostre:

A) Quantas pessoas tem mais de 18 anos.
B) Quantos homens foram cadastrados.
C) Quantas mulheres tem menos de 20 anos.
'''
cont_pessoa = 0
mais_dezoito = 0
cont_homem = 0
mulheres_menos_vinte = 0

while True:
    print('--' * 15)
    print(f'{"CADASTRAR UMA PESSOA":^30}')
    print('--' * 15)

    idade = int(input('Idade: '))
    cont_pessoa += 1

    sexo = ' '
    while sexo not in 'FfMm':
        sexo = input('Sexo: ').strip()[0]

    if idade >= 18:
        mais_dezoito += 1

    if sexo in 'Mm':
        cont_homem += 1

    if sexo in 'Ff' and idade < 20:
        mulheres_menos_vinte += 1
    
    print('--' * 15)
    continuar = ' '
    while continuar not in 'SsNn':
        continuar = input('Quer continuar? [S/N] ').strip()[0]
    
    if continuar in 'Nn':
        break

print('--' * 15)
print(f'{"FIM DO PROGRAMA":^30}')
print(f'Total de pessoas cadastradas: {cont_pessoa}')
print(f'Total de pessoas com mais 18 anos: {mais_dezoito}')
print(f'Ao todo temos {cont_homem} homens cadastrados.')
print(f'E temos {mulheres_menos_vinte} mulheres com menos de 20 anos.')    
