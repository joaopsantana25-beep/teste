'''
Exercicio 097
Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, 
imprima o número de alunos com média maior ou igual a 7.0.
'''

medias=[]
medias_maior_7=0

for i in range(10):
    soma=0
    media=0
    for j in range(4):
        nota=float(input("Digite sua nota: "))
        soma+=nota
    
    media=soma/4
    medias.append(media)
    if media>=7:
        medias_maior_7+=1

    print("\nNota computadas\n")

print(f"As médias calculadas foram: {medias}")
print(f"O número de alunos que tiveram média maior ou igual a 7 foi: {medias_maior_7}")
print("Programa Finalizado!")