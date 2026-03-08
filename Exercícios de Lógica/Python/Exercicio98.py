'''
Exercicio 098
Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.
'''

numeros = []
soma=0
mult=1

for i in range(5):
    numero=int(input("Digite um número inteiro: "))
    numeros.append(numero)
    soma+=numero
    mult*=numero
    print(f"\nNúmero Computado, {numero}!\n")


print(f'A soma dos números é {soma}')
print(f'O produto dos números é {mult}')