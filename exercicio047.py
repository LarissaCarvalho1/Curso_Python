'''
Mostre na tela todos os números pares que estão no intervalo entre 1 e 50
'''
print('Os números pares entre 1 e 50 são:')
# Realiza 50 iterações
# for contador in range(1, 51):
#     print('.', end='')
#     if contador % 2 == 0:
#         print(contador, end=' ')

# Reduz o uso do processador pela metade, fazendo 25 iterações, pois realiza apenas as interações necessárias
for contador in range(2, 51, 2):
    print('.', end='')
    print(contador, end=' ')
