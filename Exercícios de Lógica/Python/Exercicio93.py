'''
Exercicio 093
Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.
'''
lista=[]

for i in range(10):
    numero=float(input("Digite um número: "))
    print("Número computado")
    lista.append(numero)

print('\nLista inversa de vetores: ')

for numero in reversed(lista):
    print(numero)
