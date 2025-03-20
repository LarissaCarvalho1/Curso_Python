'''
Leia nome, ano de nascimento e carteira de trabalho 
e cadastre-os (com idade) em um dicionário se por 
acaso a CTPS for diferente de ZERO, o dicionário 
receberá também o ano de contratação e o salário. 
Calcule e acrescente, além da idade, com quantos 
anos a pessoa vai se aposentar.

NOME, IDADE, CARTEIRA DE TRABALHO

SE CARTEIRA != 0:
 PREGUNTA: ANO CONTRATAÇÃO, SALARIO
 COM QUANTOS ANOS A PESSOAS VAI SE APOSENTAR
 35 ANOS DE CONTRIBUIÇÃO PARA SE APOSENTAR
''' 
from datetime import date

ano_atual = date.today().year

nome = input('Nome: ').strip().title()
ano_nascimento = int(input('Ano de Nascimento: '))
ctps = int(input('Carteira de Trabalho [0 NÃO tem]: '))
idade = ano_atual - ano_nascimento

ficha = {
    'nome': nome,
    'idade': idade,
    'ctps': ctps,
}

if ctps != 0:
    ano_contratacao = int(input('Ano de Contratação: '))
    salario = float(input('Salario: '))
    ano_aposentadoria = ano_contratacao + 35

    if ano_aposentadoria >= ano_atual:
        idade_aposentadoria = idade + (ano_aposentadoria - ano_atual)
    else:
        idade_aposentadoria = idade - (ano_aposentadoria - ano_atual)

    ficha['contratacao'] = ano_contratacao
    ficha['salario'] = salario
    ficha['aposentadoria'] = idade_aposentadoria

print('-=' * 30)
for key, valor in ficha.items():
    print(f'{key.capitalize()} tem o valor {valor}')