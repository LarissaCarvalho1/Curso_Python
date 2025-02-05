# Leia um valor em metros e exiba convertido em centímetros e milímetros. 

valor_metros = float(input('Distância em Metros: '))

km = valor_metros / 1000
hm = valor_metros / 100
dam = valor_metros / 10
m = valor_metros
dm = valor_metros * 10 
cm = valor_metros * 100 
mm = valor_metros * 1000 

print(f'A distância {valor_metros} em Quilômetro é {km}km')
print(f'A distância {valor_metros} em Hectômetro é {hm}hm')
print(f'A distância {valor_metros} em Decâmetro é {dam}dam')
print(f'A distância {valor_metros} em Metros é {m}m')
print(f'A distância {valor_metros} em Decímetro é {dm}dm')
print(f'A distância {valor_metros} em Centímetro é {cm}cm')
print(f'A distância {valor_metros} em Milímetro é {mm}mm')