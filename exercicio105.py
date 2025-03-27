'''
Faça um programa que tenha uma função notas() que pode 
receber várias notas de alunos e vai retornar um 
dicionário com as seguintes informações: 

- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação (opcional)

Adicione também as docstrings da função
'''
def notas(*nota, sit=False):
    '''
    -> Função para analisar notas e situação de vários alunos.
    :param numero: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma.
    '''
    total_notas = len(nota)
    maior_nota = max(nota)
    menor_nota = min(nota)
    media = sum(nota) / total_notas
    ficha = {
        'total': total_notas,
        'maior': maior_nota,
        'menor': menor_nota,
        'media': media,
    }

    if sit:
        if media >= 7:
            situacao = 'BOA'
        elif media >= 5:
            situacao = 'RAZOÁVEL'
        else:
            situacao = 'RUIM'
        ficha['situacao'] = situacao
    
    return ficha
        

resposta = notas(3.5, 2, 6.5, 2, 7, 4, sit=True)
print(resposta)
help(notas)