'''
Exercicio 010

Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Farenheit.
'''

def farenheit(celsius):

    F = (celsius*9/5) + 32
    return F

c = float(input("Digite a temperatura em °C: "))


print(f"A temperatura em celsius é {farenheit(c)}°F")
    