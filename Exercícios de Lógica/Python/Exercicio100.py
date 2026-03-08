'''
Exercicio 100
Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor.
'''

numeros=[]
soma=0

for i in range (10):
    numero=int(input("Digite um número: "))
    numeros.append(numero)
    soma+=numero**2


    


print(f"A soma dos quadrados dos termos digitados é: {soma} ")

