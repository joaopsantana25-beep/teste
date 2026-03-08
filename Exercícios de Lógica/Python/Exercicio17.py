'''
Exercicio 017
Faça um Programa para uma loja de tintas.

O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.

Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.

Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:

    comprar apenas latas de 18 litros;
    comprar apenas galões de 3,6 litros;
    misturar latas e galões, de forma que o preço seja o menor.
    Acrescente 10% de folga e sempre arredonde os valores para cima,
    isto é, considere latas cheias.
        
'''

area=float(input("Digite o tamanho da área pintada: "))

cobertura = 1.1*area/6

if cobertura > (area//6):
    cobertura=int(cobertura) +1

baldes = cobertura/18

if baldes>(cobertura//18):
    baldes = int(baldes)+1

preco_baldes=baldes*80

galoes = cobertura /3.6

if galoes>(cobertura//3.6):
    galoes = int(galoes)+1

preco_galoes = galoes*25

#Comprar apenas latas de 18 litros

print(f"Se você comprar apenas latas você gastará R$ {preco_baldes}")

#Comprar apenas galoês de 3.6 litros

print(f"Se você comprar apenas galões você gastará R$ {preco_galoes}")

#Comprar latas e galões 
cobertura_extra=0

if baldes>1:
    cobertura_extra = cobertura - (baldes-1)*18

galoes_extra = cobertura_extra/3.6

if galoes_extra>(cobertura_extra//3.6):
    galoes_extra = int(galoes_extra)+1

preco_extra = galoes_extra*25

if preco_extra<80:
    print(f"O preço mais barato é comprar {baldes-1} latas e {galoes_extra} galoes e o preço será {(baldes-1)*80 + preco_extra} reais ")
