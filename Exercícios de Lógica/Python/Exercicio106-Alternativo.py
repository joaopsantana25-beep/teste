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

# Exercício 106 - versão final

porcento = 0.09
salarios = []
contadores = [0] * 9  # 9 intervalos de salário

# Leitura das vendas
while True:
    vendas = float(input("Digite o valor que você vendeu em bruto nessa semana (para sair digite -1): "))
    if vendas == -1:
        break
    salario = 200 + vendas * porcento
    salarios.append(salario)

if not salarios:
    print("Nenhuma venda foi computada!")
else:
    # Contagem automática usando fórmula
    for salario in salarios:
        indice = int((salario - 200) // 100)
        if indice > 8:
            indice = 8
        contadores[indice] += 1

    # Impressão da tabela
    limites = [
        "200-299", "300-399", "400-499", "500-599",
        "600-699", "700-799", "800-899", "900-999", "1000+"
    ]

    print("\nDistribuição dos salários:\n")
    for i, contador in enumerate(contadores):
        print(f"{contador:>2} vendedor(es) recebeu(m) salário(s) entre ${limites[i]}")

    # Busca de salários na lista
    while True:
        print(f"\nSalários registrados: {salarios}")
        entrada = input("\nDigite o salário que deseja buscar (ou Enter para sair): ")
        if not entrada:
            break
        try:
            buscar_salario = float(entrada)
        except ValueError:
            print("Digite um valor numérico válido!")
            continue

        posicoes = [i+1 for i, s in enumerate(salarios) if s == buscar_salario]
        if posicoes:
            print(f"O salário {buscar_salario} está nas posições: {posicoes}")
        else:
            print("O salário não está na lista!")

print("\nFim do Programa!")


