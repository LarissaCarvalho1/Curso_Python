# Leia um número e mostre o seu dobro, triplo e raiz quadrada.

num = int(input('Digite um valor: '))
num_dobro = num * 2
num_triplo = num * 3
num_raiz_quadrada = num ** (1/2)

print(f'Número digitado: {num}')
print(f'Seu dobro: {num_dobro}')
print(f'Seu triplo: {num_triplo}')
print(f'Sua raiz quadrada: {num_raiz_quadrada:.2f}')