'''
Exercicio 006
Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
'''
import math as mt

raio=float(input("Digite o raio do círculo: "))

area =(mt.pi)*(raio**2) 

print(f"A área do círculo de raio {raio} é: {area}")