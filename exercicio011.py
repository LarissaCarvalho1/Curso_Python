# Leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m².

largura_parede = int(input('Largura da parede: '))
altura_parede = int(input('Altura da parede: '))
area = largura_parede * altura_parede
qtd_tintas_necessarias = area / 2

print(f'Para pintar uma área de {area}m² será necessário {qtd_tintas_necessarias} latas de tinta. ')