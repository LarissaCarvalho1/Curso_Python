# Leia o nome de uma pessoa e diga se ela tem "SILVA" no nome

nome = input('Seu nome completo: ').strip().upper()

if 'SILVA' in nome:
    print('Você tem "Silva" no nome')
else:
    print('Você NÃO tem "Silva" no nome')