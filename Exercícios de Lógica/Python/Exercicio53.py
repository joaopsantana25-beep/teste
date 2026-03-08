'''
Exercicio 053
Faça um programa que leia 5 números e informe a soma e a média dos números.
'''

lista=[]

while True:
    num = float(input("Digite um número: "))
    lista.append(num)

    if len(lista)==5:
        break

print(f'A soma dos número que você digitou é {sum(lista)} e a média é {sum(lista)/len(lista)}')