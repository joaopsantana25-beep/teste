'''Exercicio 089
Faça um programa que peça um numero inteiro positivo e em seguida mostre este numero invertido. Exemplo: 12376489 => 98467321
'''

numero = input("Digite um inteiro positivo: ")

if int(numero)<0:
    print("Por favor digite um número válido")

else:
    print(f'{numero} => {numero[::-1]}')