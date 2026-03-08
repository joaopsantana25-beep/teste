'''
Exercicio 080
Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno 
e o segundo representando a sua altura em centímetros.

Encontre o aluno mais alto e o mais baixo.

Mostre o número do aluno mais alto e o número do aluno mais baixo, junto com suas alturas.
'''
informações_alunos={}

for numero_do_aluno in range (10):
    aluno = int(input("Digite o número do aluno: "))

    altura_aluno = float(input("Digite a altura do aluno: "))

    informações_alunos[aluno] ={
        'altura' : altura_aluno
    }

aluno_mais_alto = max(informações_alunos, key=lambda aluno: informações_alunos[aluno]['altura'])
altura_mais_alta = informações_alunos[aluno_mais_alto]['altura']

aluno_mais_baixo = min(informações_alunos, key=lambda aluno: informações_alunos[aluno]['altura'])
altura_mais_baixa = informações_alunos[aluno_mais_baixo]['altura']

print(f'O aluno mais alto é o {aluno_mais_alto} com {altura_mais_alta:.2f}')
print(f'O aluno mais baixo é o {aluno_mais_baixo} com {altura_mais_baixa:.2f}')

