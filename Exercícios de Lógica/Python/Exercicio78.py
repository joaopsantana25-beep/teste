'''
Exercicio 078
Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo, 
a mais gordo e o mais magro, para isto você deve fazer um programa que pergunte a cada um dos clientes da academia seu código,
sua altura e seu peso.

O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo código.

Ao encerrar o programa também deve ser informados os códigos e valores do clente mais alto, do mais baixo, 
do mais gordo e do mais magro, além da média das alturas e dos pesos dos clientes.
'''
informacoes_clientes={}

while True: 
    codigo = input("Qual o seu código: ")

    if codigo == '0':
        break

    peso = float(input("Qual o seu peso: "))
    altura = float(input("Qual a sua altura: "))

    informacoes_clientes[codigo]={
        'peso': peso,
        'altura': altura
    }


#operações 

if not informacoes_clientes:
    print("A lista está vazia")

else:

    codigo_mais_alto = max(informacoes_clientes, key=lambda codigo: informacoes_clientes[codigo]["altura"] )
    altura_mais_alta = informacoes_clientes[codigo_mais_alto]['altura']

    codigo_mais_baixo = min(informacoes_clientes, key=lambda codigo: informacoes_clientes[codigo]["altura"] )
    altura_mais_baixa = informacoes_clientes[codigo_mais_baixo]['altura']

    codigo_mais_gordo = max(informacoes_clientes, key=lambda codigo: informacoes_clientes[codigo]["peso"] )
    peso_mais_alto = informacoes_clientes[codigo_mais_gordo]['peso']

    codigo_mais_magro = min(informacoes_clientes, key=lambda codigo: informacoes_clientes[codigo]["peso"] )
    peso_mais_baixo = informacoes_clientes[codigo_mais_magro]['peso']

    media_altura = sum(informacoes["altura"] for informacoes in informacoes_clientes.values()) / len(informacoes_clientes)

    media_peso = sum(informacoes["peso"] for informacoes in informacoes_clientes.values()) / len(informacoes_clientes)


    #saidas

    print(f"\nO código da pessoa mais alta: {codigo_mais_alto} com {altura_mais_alta} m")
    print(f"\nO código da pessoa mais baixa: {codigo_mais_baixo} com {altura_mais_baixa} m")

    print(f"\nO código da pessoa mais gordo: {codigo_mais_gordo} com {peso_mais_alto} Kg")
    print(f"\nO código da pessoa mais magra: {codigo_mais_magro} com {peso_mais_baixo} Kg")

    print(f'\nA média de alturas é :{media_altura:.2f}')
    print(f'\nA média de pesos é : {media_peso:.2f}')