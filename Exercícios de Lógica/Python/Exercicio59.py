'''
Exercicio 059
Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.
'''

numeros_pares=0
numeros_impares=0

while True:
    numero = int(input("Digite um número inteiro: "))

    if numero%2==0:
        numeros_pares+=1
    
    else:
        numeros_impares+=1
    
    if numeros_impares+numeros_pares==10:
        break


print(f"Você digitou {numeros_pares} números pares e {numeros_impares} números ímpares.")