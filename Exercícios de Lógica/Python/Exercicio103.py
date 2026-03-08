'''Exercicio 103
Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos com mais de 13 anos 
possuem altura inferior à média de altura desses alunos.
'''
idades = [14, 15, 13, 16, 12, 14, 15, 13, 14, 16,
          15, 14, 13, 14, 15, 16, 14, 13, 15, 14,
          16, 15, 14, 13, 14, 15, 16, 14, 13, 15]

alturas = [1.60, 1.70, 1.55, 1.80, 1.50, 1.65, 1.72, 1.58, 1.62, 1.78,
           1.70, 1.66, 1.54, 1.63, 1.71, 1.79, 1.64, 1.56, 1.73, 1.67,
           1.81, 1.74, 1.68, 1.57, 1.61, 1.75, 1.82, 1.66, 1.55, 1.72]


media = sum(alturas)/len(alturas)
contador=0

for idade,altura in zip(idades,alturas):
    if idade<13 and altura<media:
        contador+=1

print(f"A média de alturas é: {media:.2f} ")
print(f'O número de alunos menores de 13 anos com a altura inferior a média é: {contador}')