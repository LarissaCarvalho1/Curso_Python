'''
Leia duas notas de um aluno e calcule sua média,
mostrando uma mensagem no final, de acordo com a média atingida:

- Abaixo de 5.0: REPROVADO
- Entre 5.0 e 6.9: RECUPERAÇÃO
- Média 7.0 ou superior: APROVADO
'''
primeira_nota = float(input('Primeira Nota: '))
segunda_nota = float(input('Segunda Nota: '))
media = (primeira_nota + segunda_nota) / 2

print(f'Tirando {primeira_nota:.1f} e {segunda_nota:.1f}, a média do aluno é {media:.1f}')
if media < 5:
    print('O aluno está REPROVADO!')
elif media <= 6.9:
    print('O aluno está em RECUPERAÇÃO!')
else:
    print('O aluno está APROVADO!')