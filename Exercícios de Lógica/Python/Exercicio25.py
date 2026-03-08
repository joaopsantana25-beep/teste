'''
Exercicio 025
Faça um Programa que leia três números e mostre o maior e o menor deles.
'''


num1=float(input("Digite o primeiro número: "))
num2=float(input("Digite o segundo número: "))
num3=float(input("Digite o terceiro número: "))

if num1>num2 and num1>num3:
    print(f"O primeiro número {num1} é o maior")


elif num2>num1 and num2>num3:
    print(f"O segundo número {num2} é o maior")

else:
    print(f"O terceiro número {num3} é o maior")


if num1<num2 and num1<num3:
    print(f"O primeiro número {num1} é o menor")


elif num2<num1 and num2<num3:
    print(f"O segundo número {num2} é o menor")

else:
    print(f"O terceiro número {num3} é o menor")