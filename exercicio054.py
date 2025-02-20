'''
Leia o ano de nascimento de sete pessoas. No final, mostre 
quantas pessoas ainda não atingiram a maioridade e quantas 
já são maiores. Para a maioridade, considere 21 anos

'''
from datetime import date

ano_atual = date.today().year
idade = 0
menoridade = 0
maioridade = 0

for contador_pessoa in range(7):    
    ano_nascimento = int(input(f'Ano de nascimento da {contador_pessoa + 1}° pessoa: '))
    idade = ano_atual - ano_nascimento

    if idade >= 21:
        maioridade += 1
    else:
        menoridade += 1

print(f'Ao todo tivemos {maioridade} pessoas maiores de idade.')
print(f'E também tivemos {menoridade} pessoas menores de idade.')