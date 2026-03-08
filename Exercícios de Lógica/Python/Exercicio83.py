'''Exercicio 083
Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos deles estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100].

A entrada de dados deverá terminar quando for lido um número negativo.
'''

intervalo_0_25=0
intervalo_26_50=0
intervalo_51_75=0
intervalo_76_100=0

while True:
    numero = int(input("Digite um número positivo para ser computado, para sair digite um número negativo: "))

    if numero<0:
        print("Você digitou um número negativo, saindo do programa.")
        break

    else:
        if numero<=25:
            intervalo_0_25+=1

        elif numero<=50:
            intervalo_26_50+=1

        elif numero<=75:
            intervalo_51_75+=1
        
        elif numero<=100:
            intervalo_76_100+=1


print(f'Voce digitou {intervalo_0_25} números entre 0 e 25')
print(f'Voce digitou {intervalo_26_50} números entre 26 e 50')
print(f'Voce digitou {intervalo_51_75} números entre 51 e 75')
print(f'Voce digitou {intervalo_76_100} números entre 76 e 100')