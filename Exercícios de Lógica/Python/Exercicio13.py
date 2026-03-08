'''
Exercicio 013

Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas: Para homens: (72.7h) - 58 Para mulheres: (62.1h) - 44.7
'''

h = float(input("Digite sua altura: "))
sexo=input("Digite o seu sexo (M/F): ").lower()

if sexo =="m":
    peso_ideal=(72.7*h)-58
    print(f"Seu peso ideal é {peso_ideal} Kg")

elif sexo == "f":
    peso_ideal=(62.1*h-44.7)
    print(f"Seu peso ideal é {peso_ideal} Kg")

else:
    print("Erro, por favor digite corretamente sua altura e seu sexo.")
