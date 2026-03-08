'''
Exercicio 067
Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário.

O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos.

Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.
'''


fim_da_contagem = int(input("Digite o número que será o fim do intervalo: "))
numeros_primos=[]
numero_de_divisoes=0

if fim_da_contagem>=2:
    numeros_primos=[2]

    for i in range (3,fim_da_contagem+1,2):
        teste = True

        for j in range (2,(i)):
            numero_de_divisoes+=1
            if i%j==0:
                teste=False
                break
        
        if teste:
            numeros_primos.append(i)
        


    print(f'Os números primos entre 1 e {fim_da_contagem} são {numeros_primos}')
    print(f"Foram feitas {numero_de_divisoes} para chegar nesse resultado")

else:
    print("Por favor digite um número inteiro maior que 1")