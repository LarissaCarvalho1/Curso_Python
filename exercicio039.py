'''
Leia o ano de nascimento de um jovem e informe, 
de acordo com a sua idade: 

- Se ele ainda vai se alistar ao serviço militar
- Se é a hora de se alistar
- Se já passou do tempo do alistamento

Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
'''
from datetime import date

ano_atual = date.today().year
ano_nascimento = int(input('Em que ano você nasceu? '))
idade = ano_atual - ano_nascimento
idade_minima_alistamento = 18
tempo_alistamento = 0
ano_alistamento = 0

print(f'Quem nasceu em {ano_nascimento} tem {idade} anos em {ano_atual}')

if idade < idade_minima_alistamento:
    tempo_alistamento = idade_minima_alistamento - idade
    ano_alistamento = ano_atual + tempo_alistamento
    print(f'Ainda faltam {tempo_alistamento} anos para o seu alistamento')
    print(f'Seu alistamento será em {ano_alistamento}')

elif idade == idade_minima_alistamento:
    print('Você tem que se alistar IMEDIATAMENTE!')

elif idade > idade_minima_alistamento:
    tempo_alistamento = idade - 18
    ano_alistamento = ano_atual - tempo_alistamento
    print(f'Você já deveria ter se alistado há {tempo_alistamento} anos.')
    print(f'Seu alistamento foi em {ano_alistamento}')
