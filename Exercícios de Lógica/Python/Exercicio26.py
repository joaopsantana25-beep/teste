'''
Exercicio 026
Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.
'''

num1=float(input("Digite o preço do primeiro produto: "))
num2=float(input("Digite o preço do segundo produto: "))
num3=float(input("Digite o preço do terceiro produto: "))

if num1<num2 and num1<num3:
    print("Você deve comprar o primeiro produto")


elif num2<num1 and num2<num3:
    print("Você deve comprar o segundo produto")

else:
    print("Você deve comprar o terceiro produto")