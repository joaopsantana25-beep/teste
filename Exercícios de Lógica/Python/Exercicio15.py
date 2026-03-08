'''
Exercicio 015
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.

Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê: salário bruto. quanto pagou ao INSS. quanto pagou ao sindicato. o salário líquido. calcule os descontos e o salário líquido, conforme a tabela abaixo:

+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$
Obs.: Salário Bruto - Descontos = Salário Líquido.

'''

horas = int(input("Quantas horas você trabalha no mês: "))
dinheiro = float(input("Quanto você recebe por hora trabalhada: "))
salario_bruto= horas*dinheiro

IR = 0.11*salario_bruto
INSS=0.08*salario_bruto
Sindicato=0.05*salario_bruto
salario_liquido=salario_bruto-IR-INSS - Sindicato

print(f'+ Salário Bruto : {salario_bruto} R$ \n- IR (11%) : {IR} R$ \n- INSS (8%) : {INSS} R$ \n- Sindicato (5%) : {Sindicato} R$ \n= Salário Liquido : {salario_liquido} R$')
