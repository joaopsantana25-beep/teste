'''
Exercicio 071
Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma. As turmas não podem ter mais de 40 alunos.
'''

Turmas={}

while True:
    turma = input("Digite a turma: ")

    if turma.lower()=="sair" or turma=='':
        break
    alunos = input("Digite a quantidade de alunos: ")

    if not alunos.isdigit():
        print("Por favor coloque valores válidos de alunos")
        continue

    alunos_numeros = int(alunos)

    if alunos_numeros>40 or alunos_numeros<0:
        print("Por favor coloque um valor válidos, o máximo de alunos por turma é 40.")
        continue

    Turmas[turma]=alunos_numeros
    print("Turma Cadastrada!")

if Turmas:
    media = sum(Turmas.values())/len(Turmas)

    print(f"A média de alunos por sala é {media:.2f}")
    
else:
    print("Nenhuma turma cadastrada")



