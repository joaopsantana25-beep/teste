'''Exercicio 105
Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de dados quando 
for informado um valor igual a -1 (que não deve ser armazenado).

Após esta entrada de dados, faça: 
Mostre a quantidade de valores que foram lidos; 
Exiba todos os valores na ordem em que foram informados, um ao lado do outro; 
Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro; 
Calcule e mostre a soma dos valores; 
Calcule e mostre a média dos valores; 
Calcule e mostre a quantidade de valores acima da média calculada; 
Calcule e mostre a quantidade de valores abaixo de sete; 
Encerre o programa com uma mensagem;
'''

lista=[]
media=0
soma=0
quantidade_valores=0
valores_acima_da_media=0
valores_abaixo_de_sete=0

while True:
    numero = float(input("Digite um valor, para sair digite -1: "))

    if numero ==-1:
        break

    lista.append(numero)

if not lista:
    print("Nenhum valor foi digitado!")
    print("Fim do Programa")

else:
    quantidade_valores=len(lista)
    soma=sum(lista)
    media=soma/quantidade_valores

    #Mostre a quantidade de valores que foram lidos

    print(f'\nForam lidos {quantidade_valores} valores.\n')

    #Exiba todos os valores na ordem em que foram informados, um ao lado do outro

    for valor in lista:
        print(valor,end=' ')

    print("\n") #Dar espaço para a próxima operação

    #Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro

    for valor in reversed(lista):
        print(valor)

    #Calcule e mostre a soma dos valores; 

    print(f"\nA soma dos valores é: {soma}")

    #Calcule e mostre a média dos valores; 

    print(f"\nA média dos valores é: {media:.2f}")

    #Calcule e mostre a quantidade de valores acima da média calculada; 
    for valor in lista:
        if valor>media:
            valores_acima_da_media+=1

    print(f"\nA quantidade de valores acima da média é: {valores_acima_da_media}")

    #Calcule e mostre a quantidade de valores abaixo de sete;
    for valor in lista:
        if valor<7:
            valores_abaixo_de_sete+=1

    print(f"\nA quantidade de valores abaixo de 7 é: {valores_abaixo_de_sete}")

    #Encerre o programa com uma mensagem;

    print("\nFim do Programa!")
