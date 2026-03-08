'''
Exercicio 004

Faça um Programa que peça as 4 notas bimestrais e mostre a média.
'''
contador = 0
soma=0

while contador<4:
    num=float(input("Digite sua nota bimestral: "))

    soma+=num
    contador+=1

media = soma/4

print(f"A sua média é {media}")
