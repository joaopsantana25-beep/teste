'''
Exercicio 055
Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.
'''

num1 = int(input("Digite o começo do intervalo: "))

num2 = int(input("Digite o fim do intervalo: "))

if num1<=num2:
    for i in range(num1+1,num2,1):
        print(i)

else:
    for i in range(num1-1,num2,-1):
        print(i)