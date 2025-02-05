# Leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo,
# calcule e mostre o comprimento da hipotenusa.

from math import hypot

cateto_oposto = float(input('Cateto Oposto: '))
cateto_adjacente = float(input('Cateto adjacente: '))
hipotenusa = hypot(cateto_oposto, cateto_adjacente)
print(f'O triângulo retângulo com CO = {cateto_oposto} e CA = {cateto_adjacente} tem a Hipotenusa = {hipotenusa:.2f}')
