# Leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m².

largura_parede = float(input('Largura da parede: '))
altura_parede = float(input('Altura da parede: '))
area = largura_parede * altura_parede
qtd_tintas_necessarias = area / 2

print(f'Sua parede tem a dimensão de {largura_parede}x{altura_parede} e sua área é de {area}m².')
print(f'Para pintar essa parede, você precisará de {qtd_tintas_necessarias}l de tinta.')