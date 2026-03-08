'''
Exercicio 045
O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:

                  Até 5 Kg   File Duplo R$ 4,90 por Kg, Alcatra R$ 5,90 por Kg Picanha R$ 6,90 por Kg       Acima de 5 Kg R$ 5,80 por Kg  R$ 6,80 por Kg  R$ 7,80 por Kg
 

Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há limites para a quantidade de carne por cliente.

Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra.

Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra: 
tipo de carne quantidade de carne preço total tipo de pagamento valor do desconto valor a pagar.

'''

massa = float(input("Digite quantos kilos você pegou de carne: "))
tipo = input("Digite o tipo de carne (F - File Duplo, A - Alcatra, P - Picanha): ").upper()
compra = input("Você usará o cartão da loja para fazer a compra (S/N): ").upper()

if tipo == "F":
    tipo = "File Duplo"
    
    if massa<=5:
        preco = massa * 4.9
    
    else:
        preco = massa * 5.8

elif tipo == "A":
    tipo = "Alcatra"

    if massa<=5:
        preco = massa * 5.9

    else:
        preco = massa * 6.80

elif tipo == "P":
    tipo = "Picanha"

    if massa<=5:
        preco = massa * 6.9

    else:
        preco = massa * 7.80

else:
    print("Valor inválido, por favor digite 'F' para filé duplo, 'A' para alcatra e 'P' para picanha! ")



if compra == "S":
    desconto = preco*0.1 
    preco_desconto = preco*0.9

elif compra == "N":
    desconto = 0
    preco_desconto = preco

else:
    print("Por favor digite 'S' se for usar o cartão da loja ou 'N' se não for usar o cartão")



#Nota fiscal

print("\nNota Fiscal")
print(f"\nTipo de carne comprada: {tipo}")
print(f"\nQuantidade de carne comprada: {massa}Kg")
print(f"\nUso cartão da loja: {compra}")
print(f"\nValor sem desconto: R$ {preco}")
print(f"\nDescontos: R$ {desconto}")
print(f"\nTotal a pagar: R$ {preco_desconto}")



