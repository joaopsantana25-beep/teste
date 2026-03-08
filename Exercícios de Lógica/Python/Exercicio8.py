'''
Exercicio 008

Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
'''

dinheiro = float(input("Quanto você ganha por hora: "))
horas = float(input("Quantas horas você trabalha por mês: "))

salario = dinheiro * horas

print(f"O seu salário é: R$ {salario} reais")