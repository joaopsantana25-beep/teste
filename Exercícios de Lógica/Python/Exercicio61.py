'''
Exercicio 061
Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120
'''

numero=int(input("Digite o número para encontrar seu fatorial: "))
fatorial = 1

if numero<0:
    print("Não existe fatorial de número negativo")

elif numero ==0:
    print("0! = 1")

else:
    for i in range (1,numero+1):
        fatorial=fatorial*i

    print(f'{numero}! = {fatorial}')