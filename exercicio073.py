'''
Crie uma tupla preenchida com os 20 primeiros colocados 
da Tabela do Campeonato Brasileiro de Futebol, na ordem 
de colocação. Depois mostre:

- Apenas os 5 primeiros colocados.
- Os últimos 4 colocados da tabela.
- Uma lista com os times em ordem alfabética.
- Em que posição na tabela está o time da Chapecoense.
'''
times = ('Palmeiras', 'Flamengo', 'Internacional', 'Grêmio', 
         'São Paulo', 'Atlético-MG', 'Athletico-PR', 'Cruzeiro', 
         'Botafogo', 'Santos', 'Bahia', 'Fluminense', 'Corinthians', 
         'Chapecoense', 'Ceará SC', 'Vasco da Gama', 'Sport Recife', 
         'América - MG', 'EC Vitória', 'Paraná')

print('Lista de times do Brasileirão: ')
for posicao, time in enumerate(times):
    print(f'{posicao + 1}ª - {time}')
print(f'-=' * 20)

print('Os 5 primeiros são: ')
for cont in range(5):
    print(f'{cont + 1}ª - {times[cont]}')
print(f'-=' * 20)

print('Os 4 últimos são: ')
for cont in range(-4, 0):
    print(times[cont])
print(f'-=' * 20)

times_ordem_alfabetica = sorted(times)
print('Times em ordem alfabética: ')
for time_ordenado in times_ordem_alfabetica:
    print(time_ordenado)
print(f'-=' * 20)

posicao_chapeco = times.index('Chapecoense') + 1
print(f'O Chapecoense está na {posicao_chapeco}ª posição.')