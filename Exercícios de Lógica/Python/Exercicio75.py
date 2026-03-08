'''
Exercicio 075
O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui uma loja de conveniências.

Faça um programa que implemente uma caixa registradora rudimentar.

O programa deverá receber um número desconhecido de valores referentes aos preços das mercadorias.

Um valor zero deve ser informado pelo operador para indicar o final da compra.

O programa deve então mostrar o total da compra e perguntar o valor em dinheiro que o cliente forneceu,
para então calcular e mostrar o valor do troco.

Após esta operação, o programa deverá voltar ao ponto inicial, para registrar a próxima compra.

A saída deve ser conforme o exemplo abaixo: Lojas Tabajara Produto 1: R$ 2.20 Produto 2: R$ 5.80 Produto 3: R$ 0 Total: R$ 9.00 Dinheiro: R$ 20.00 Troco: R$ 11.00
'''



while True:
    lista_de_precos=[]
    
    while True:
            preco_do_produto =float(input("Digite o preço do produto: "))
      
            if preco_do_produto==0:
                break

            lista_de_precos.append(preco_do_produto)
            print("Preço computado com sucesso")
        
    dinheiro = float(input("Quanto dinheiro foi dado pelo cliente: "))
    troco = dinheiro-sum(lista_de_precos)

    for i in range(len(lista_de_precos)):
        print(f'Produto {i+1}: R$ {lista_de_precos[i]} ')

    print(f'Total: R$ {sum(lista_de_precos)} ')
    print(f'Dinheiro: R$ {dinheiro}')
    print(f'Troco: R$ {troco}')



    if input("Para realizar uma nova compra aperte qualquer tecla ")=='':
            break

    
