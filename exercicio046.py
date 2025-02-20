'''
Mostre na tela uma contagem regressiva para o 
estouro de fogos de artifício, indo de 10 até 0, 
com uma pausa de 1 segundo entre eles
'''
from time import sleep

print('Os fogos vão estourar em...')
for contador in range(10, -1, -1):
    print(contador)
    sleep(1)
print('BUM! BUM! POOW!')