'''
Listas
Exercicio 092
Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.
'''

lista=[]

for i in range(5):
    vetor=int(input("Digite um número inteiro: "))
    print("Número Computado")
    lista.append(vetor)

print('\nLista de vetores:')
for vetor in lista:
    print(vetor)