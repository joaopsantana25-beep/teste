'''
Exercicio 058
Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número. Não utilize a função de potência da linguagem.
'''

base = int(input("Digite um número inteiro que será a base: "))

expoente = int(input("Digite um número inteiro que será o expoente: "))

resultado = 1

if expoente ==0:
    resultado =1


elif expoente>0:
    for i in range (expoente):
        resultado = resultado*base

    

else:
    for i in range (-expoente):
        resultado = resultado/base


print(resultado)

