# Pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por km rodado. 

dias_alugados = int(input('Por quantos dias o carro foi alugado? '))
km_percorrido = float(input('Quantos km rodados? '))
valor_pagar = (dias_alugados * 60) + (km_percorrido * 0.15)
print(f'O total a pagar é de R${valor_pagar:.2f}')