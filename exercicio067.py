'''
Mostre a tabuada de vários números, um de cada vez, 
para cada valor digitado pelo usuário. O programa 
será interrompido quando o número solicitado for 
nagativo.

Quer ver a tabuada de qual valor?
'''
while True:
    tabuada = int(input('Quer ver a tabuada de qual valor? '))
    print('--' * 20)
    
    if tabuada < 0:
        break

    for cont in range(11):
        print(f'{tabuada}  x {cont:2} = {(tabuada * cont):2}')
    print('--' * 20)
print('PROGRAMA TABUADA ENCERRADO. Volte Sempre!')