'''Exercicio 106
Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus vendedores com base em comissões. 
O vendedor recebe $200 por semana mais 9 por cento de suas vendas brutas daquela semana. 
Por exemplo, um vendedor que teve vendas brutas de $3000 em uma semana recebe $200 mais 9 por cento de $3000, ou seja, 
um total de $470. 

Escreva um programa (usando um array de contadores) que determine quantos vendedores receberam salários nos seguintes intervalos de
valores: 
$200 - $299 
$300 - $399 
$400 - $499 
$500 - $599 
$600 - $699
$700 - $799 
$800 - $899 
$900 - $999 
$1000 em diante 

Desafio: Crie uma fórmula para chegar na posição da lista a partir do salário, sem fazer vários ifs aninhados.
'''

porcento=0.09
salarios=[]
contadores = [0,0,0,0,0,0,0,0,0] #Cada digito corresponde a uma amplitude no salário


while True:
    vendas = float(input("Digite o valor que você vendeu em bruto nessa semana (para sair digite -1): ")) 

    if vendas ==-1:
        break

    salario = 200+vendas*porcento
    salarios.append(salario)

if not salarios:
    print("Nenhuma venda foi computada!")

else:
    for salario in salarios:
       indice = int((salario - 200) // 100)

       if indice>8:
            indice=8
    
       contadores[indice] += 1



    lower_limit=200
    upper_limit=299

    for contador in contadores:
        if lower_limit!=1000:
            print(f'\n{contador} vendedores receberam um salário entre ${lower_limit} - {upper_limit}')
        else:
            print(f'\n{contador} vendedores receberam um salário acima de $1000\n')

        lower_limit+=100
        upper_limit+=100


    #Desafio

    print(salarios)

    while True:
        print(f'Os salários na lista são: {salarios}')
        buscar_salario =(input("\nDigite o salário que você deseja saber a posição: "))

        if not buscar_salario:
            print("Digite um salário para ser buscado")
            continue 

        buscar_salario=float(buscar_salario)

        if buscar_salario in salarios:
            print(f"\nO salário buscado está no {salarios.index(buscar_salario)+1}° lugar da lista")

        else:
            print("\nO salário não está na lista!")

        opcao=input("\nVocê deseja continuar (s/n): ").lower()

        if opcao == "n":
            break

print("\nFim do Programa!")    

