'''
Exercicio 043
Um posto está vendendo combustíveis com a seguinte tabela de descontos:

 Álcool: até 20 litros, desconto de 3% por litro
 acima de 20 litros, desconto de 5% por litro 
 
 Gasolina: até 20 litros, desconto de 4% por litro 
 acima de 20 litros, desconto de 6% por litro

Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool,
 G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 
 o preço do litro do álcool é R$ 1,90.
'''

preco_gasolina=2.50
preco_alcool=1.90


litros = float(input("Digite quandos litros foram vendidos: "))
tipo_combustivel = input("Foi álcool ou gasolina (A,G): ").upper()

if tipo_combustivel == "G":
    tipo_combustivel = "gasolina"
    if litros<=20:
        preco_pagar = litros * preco_gasolina * 0.96 
    
    else:
        preco_pagar = litros * preco_gasolina * 0.94

if tipo_combustivel == "A":
    tipo_combustivel = "álcool"
    if litros<=20:
        preco_pagar = litros * preco_alcool* 0.97 
    
    else:
        preco_pagar = litros * preco_alcool * 0.95



print(f"Foi vendido {litros}L de {tipo_combustivel}, o preço a ser pago será de {preco_pagar}.")