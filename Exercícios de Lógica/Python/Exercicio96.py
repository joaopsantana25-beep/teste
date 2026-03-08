'''Exercicio 096
Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os 
números IMPARES no vetor impar. Imprima os três vetores.
'''
numeros=[]
numeros_pares=[]
numeros_impares=[]

for i in range(20):
    numero=int(input("Digite um número inteiro: "))

    numeros.append(numero)

    if numero%2==0:
        numeros_pares.append(numero)
    else:
        numeros_impares.append(numero)

print(numeros)
print(numeros_pares)
print(numeros_impares)