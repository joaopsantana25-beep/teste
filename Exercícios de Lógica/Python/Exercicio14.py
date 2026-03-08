'''
Exercicio 014
João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho.

Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente.

João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso.

Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.
'''

peso_pescado = float(input("Digite quandos quilos foi pescado: "))

peso_estabelecido=50
peso_excedente=peso_pescado-peso_estabelecido

if peso_excedente>0:
    multa = peso_excedente*4
    print(f"Joao pescou {peso_excedente} a mais do que poderia e a multa será de R$ {multa} reais.")

elif peso_excedente<=0:
    print("João não pagará nenhuma multa pois pescou dentro do limite estabelecido.")