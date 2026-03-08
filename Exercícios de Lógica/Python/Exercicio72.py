'''
Exercicio 072
Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um.
'''
soma=0
numero_de_cds= input("Digite quantos cds você comprou: ")

if not numero_de_cds.isdigit():
    print("Por favor digite um valor válido")

else:   
    numero_de_cds=int(numero_de_cds)

if numero_de_cds<0:
    print("Por favor digite um valor válido de cds")

elif int(numero_de_cds)==0:
    print("Nenhum CD foi comprado!\nFim do Programa!")

else:
    for cd in range (numero_de_cds):
        while True:
            preco_do_cd=input("Digite o preço do cd: ")

            if not preco_do_cd.replace(".","",1).isdigit():
                print("Por favor coloque um valor válido")
                continue

            preco_do_cd=float(preco_do_cd)

            if (preco_do_cd)<0:
                print("Por favor coloque um valor válido!")
                continue

            soma+=(preco_do_cd)
            print("Preço computado")
            break


    print(f"Você tem ao todo {numero_de_cds} cd's")
    print(f"O preço médio que você gastou por cd foi R$ {soma/(numero_de_cds)} reais.")
