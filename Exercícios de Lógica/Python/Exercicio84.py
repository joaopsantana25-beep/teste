'''
Exercicio 084
O cardápio de uma lanchonete é o seguinte: Especificação Código Preço
 Cachorro Quente 100 R$ 1,20 
 Bauru Simples 101 R$ 1,30 
 Bauru com ovo 102 R$ 1,50 
 Hambúrguer 103 R$ 1,20 
 Cheeseburguer 104 R$ 1,30 
 Refrigerante 105 R$ 1,00 
 
Faça um programa que leia o código dos itens pedidos e as quantidades desejadas.

Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral do pedido.

Considere que o cliente deve informar quando o pedido deve ser encerrado.
'''

lista = []
cachorro_quente=0
bauru_simples=0
bauru_com_ovo = 0
hamburguer = 0
chesseburguer = 0
refrigerante = 0
preco=0

while True:
    codigo_do_produto=int(input("Digite o código do produto, para sair digite 0: "))
    
    if codigo_do_produto==0:
        break

    quantidade_produto = int(input("Digite a quantidade do item: "))

    if codigo_do_produto==100:
        cachorro_quente+=quantidade_produto
        preco+=quantidade_produto*1.20
    
    elif codigo_do_produto==101:
        bauru_simples+=quantidade_produto
        preco+=quantidade_produto*1.30

    elif codigo_do_produto==102:
        bauru_com_ovo+=quantidade_produto
        preco+=quantidade_produto*1.50

    elif codigo_do_produto==103:
        hamburguer+=quantidade_produto
        preco+=quantidade_produto*1.20
    
    elif codigo_do_produto == 104:
        chesseburguer+=quantidade_produto
        preco+=quantidade_produto*1.30
    
    elif codigo_do_produto==105:
        refrigerante+=quantidade_produto
        preco+=quantidade_produto*1.00

        
if not preco:
    print("Você não comprou nada")

else:
    if cachorro_quente>0:
        print(f'Você comprou {cachorro_quente} cachorros quentes. {cachorro_quente}*{1.20} = {cachorro_quente*1.20:.2f}')

    if bauru_simples>0:
        print(f'Você comprou {bauru_simples} baurus simples. {bauru_simples}*{1.30} = {bauru_simples*1.30:.2f}')

    if bauru_com_ovo>0:
        print(f'Você comprou {bauru_com_ovo} baurus com ovo. {bauru_com_ovo}*{1.50} = {bauru_com_ovo*1.50:.2f}')

    if hamburguer>0:
        print(f'Você comprou {hamburguer} hamburgueres. {hamburguer}*{1.20} = {hamburguer*1.20:.2f}')

    if chesseburguer>0:
        print(f'Você comprou {chesseburguer} chessehamburgueres. {chesseburguer}*{1.30} = {chesseburguer*1.30:.2f}')
    
    if refrigerante>0:
        print(f'Você comprou {refrigerante} refrigerantes. {refrigerante}*{1.00} = {refrigerante*1.00:.2f}')
    
    print(f'O total deu: {preco:.2f}')
    
    
