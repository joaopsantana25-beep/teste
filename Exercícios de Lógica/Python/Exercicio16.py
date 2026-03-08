'''
Exercicio 016
Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.

Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.

Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
'''

area=float(input("Digite o tamanho da área pintada: "))

cobertura = area/3

if cobertura > (area//3):
    cobertura=int(cobertura) +1

baldes = cobertura/18

if baldes>(cobertura//18):
    baldes = int(baldes)+1

preco=baldes*80

print(f"Será preciso comprar {baldes} balde/s e o preço será de R$ {preco} reais.")