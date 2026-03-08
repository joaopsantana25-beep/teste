'''
Exercicio 011

Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre: o produto do dobro do primeiro com metade do segundo. a soma do triplo do primeiro com o terceiro. o terceiro elevado ao cubo.
'''

num1 = int(input("Digite um número inteiro: "))

num2 = int(input("Digite um número inteiro: "))

num3 = float(input("Digite um número real: "))

#Primeira operação

resultado1=2*num1*num2/2
print(resultado1)

#Segunda operação

resultado2 = 3*num1+num3
print(resultado2)

#Terceira operação

resultado3=num3**3
print(resultado3)