'''
Exercicio 052
Faça um programa que leia 5 números e informe o maior número.
'''

lista=[]

while True:
    num = float(input("Digite um número: "))
    lista.append(num)

    if len(lista)==5:
        break

print(f'O maior número que você digitou foi: {max(lista)}')