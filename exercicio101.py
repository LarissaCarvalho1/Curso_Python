'''
Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.
'''
def voto(ano_nascimento):
    from datetime import date

    ano_atual = date.today().year
    idade = ano_atual - ano_nascimento
    
    if idade < 16:
        tipo_voto = 'NÃO VOTA'
    elif 16 <= idade < 18 or idade > 65:
        tipo_voto = 'VOTO OPCIONAL'
    else:
        tipo_voto = 'VOTO OBRIGATÓRIO'
    
    return f'Com {idade} anos: {tipo_voto}.'


ano_nasc = int(input('Em que ano você nasceu? '))
resposta = voto(ano_nasc)
print(resposta)
