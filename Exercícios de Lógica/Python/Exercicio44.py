'''
Exercicio 044
Uma fruteira está vendendo frutas com a seguinte tabela de preços:

Até 5 Kg: Morango R$ 2,50  Maçã R$ 1,80    Acima de 5 Kg: morango R$ 2,20 por Kg, maçã 1,50 por Kg



Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, 
receberá ainda um desconto de 10% sobre este total.

Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas 
e escreva o valor a ser pago pelo cliente.

'''

massa_morangos=float(input("Digite quantos kg de morangos foram comprado: "))

massa_maca=float(input("Digite quantos kg de maças foram comprado: "))

massa_total = massa_morangos+massa_maca



if massa_morangos<=5:
    preco_morangos = massa_morangos*2.50

else:
    preco_morangos = massa_morangos*2.20



if massa_maca<=5:
    preco_maca= massa_maca*1.80

else:
    preco_maca = massa_maca*1.50


preco_total = preco_maca+preco_morangos

if massa_total>8 or preco_total>25:
    preco_total = preco_total*0.90


print(f"Você levou ao todo {massa_total} Kg de comida e pagará {preco_total}.")
