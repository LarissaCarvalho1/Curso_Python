# Leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import radians, sin, cos, tan
angulo = float(input('Digite o ângulo que você deseja: ')) 
seno = sin(radians(angulo)) 
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print(f'O ângulo {angulo} tem como SENO {seno:.2f}')
print(f'O ângulo {angulo} tem como COSSENO {cosseno:.2f}')
print(f'O ângulo {angulo} tem como TANGENTE {tangente:.2f}')