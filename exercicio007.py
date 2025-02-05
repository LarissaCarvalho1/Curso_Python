# Leia as duas notas de um aluno, calcule e mostre a sua média.

primeira_nota = float(input('Primeira Nota: '))
segunda_nota = float(input('Segunda Nota: '))
media = (primeira_nota + segunda_nota) / 2

print(f'1° Nota: {primeira_nota:.1f}')
print(f'2° Nota: {segunda_nota:.1f}')
print(f'Média das notas: {media:.1f}')