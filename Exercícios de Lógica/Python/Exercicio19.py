'''
Exercicio 019

Faça um Programa que peça dois números e imprima o maior deles.
'''

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

if num1>num2:
    print("O primeiro número é o maior.")

elif num1<num2:
    print("O segundo número é o maior.")

else:
    print("Os dois números são iguais")