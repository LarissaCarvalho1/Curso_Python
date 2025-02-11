'''
Leia o peso e a altura de uma pessoa, calcule seu IMC 
e mostre seu status, de acordo com a tabela abaixo:

- Abaixo de 18,5: Abaixo do Peso
- Entre 18,5 e 25: Peso ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade mórbida
'''
print('-=' * 20)
print('CALCULADORA DE IMC')
print('-=' * 20)

peso = float(input('Peso (kg): '))
altura = float(input('Altura (M): '))
imc = peso / (altura ** 2)

print(f'O IMC dessa pessoa é de {imc:.1f}')
if imc < 18.5:
    print('Você está ABAIXO do PESO normal!')
elif imc < 25:
    print('PARABÉNS, você está na faixa de PESO NORMAL')
elif imc < 30:
    print('Você está em SOBREPESO!')
elif imc < 40:
    print('Você está em OBESIDADE!')
else:
    print('Você está em OBESIDADE MÓRBIDA, cuidado!')
