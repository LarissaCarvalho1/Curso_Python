'''
Leia dois valores e mostre um menu na tela 

[1]somar
[2]multiplicar
[3]maior
[4]novos números
[5]sair do programa

Seu programa deverá realizar a operação solicitada 
em cada caso
'''
from time import sleep
primeiro_valor = int(input('Primeiro valor: '))
segundo_valor = int(input('Segundo valor: '))
opcao = ''

while opcao != '5':
    print('-==' * 10)
    print('[ 1 ] Somar')
    print('[ 2 ] Multiplicar')
    print('[ 3 ] Maior')
    print('[ 4 ] Novos Números')
    print('[ 5 ] Sair do Programa')
    opcao = input('>>>>> Qual é sua opção: ')

    if opcao == '1':
        soma = primeiro_valor + segundo_valor
        print(f'A soma entre {primeiro_valor} + {segundo_valor} é {soma}')

    elif opcao == '2':
        produto = primeiro_valor * segundo_valor
        print(f'O resultado de {primeiro_valor} x {segundo_valor} é {produto}')

    elif opcao == '3':

        if primeiro_valor == segundo_valor:
            print('Números IGUAIS. Não há valor maior.')
        elif primeiro_valor > segundo_valor:
            print(f'Entre {primeiro_valor} e {segundo_valor} o maior valor é {primeiro_valor}')
        else:
            print(f'Entre {primeiro_valor} e {segundo_valor} o maior valor é {segundo_valor}')
        
    elif opcao == '4':
        print('Informe os números novamente:')
        primeiro_valor = int(input('Primeiro valor: '))
        segundo_valor = int(input('Segundo valor: '))

    elif opcao == '5':
        print('Finalizando...')
        print('-==' * 10)

    else:
        print('Opção inválida! Tente novamente.')
    sleep(1)
print('Fim do programa! Volte sempre!')