'''
Leia o sexo de uma pessoa, mas só aceite os valores "M" ou "F".
Caso esteja errado, peça a digitação novamente até ter um valor correto. 
'''
sexo = input('Informe seu sexo: [M/F] ').strip().upper()[0]

while sexo not in 'MF':
    print('\033[31mDados Inválidos!\033[m')
    sexo = input('Por favor, informe seu sexo: ').strip().upper()[0]
print(f'Sexo {sexo} registrado com \033[32msucesso\033[m')