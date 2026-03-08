'''
Exercicio 069
Faça um programa que peça para n pessoas a sua idade, ao final o programa deverá verificar se a média de idade da turma varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.
'''

lista_de_idades=[]

while True:
    entrada =(input("Digite a sua idade: "))

    if entrada == '':
        break

    if not entrada.isdigit():
        print("Por favor digite um número válido")
        continue

    idade = int(entrada)
    
    if idade<=0:
        print("Por favor digite uma idade válida")
        continue

   
    lista_de_idades.append(idade)

    
if lista_de_idades:
    media=sum(lista_de_idades)/len(lista_de_idades)

    if media<=25:
        classificacao="jovem"

    elif media<=60:
        classificacao="adulta"
    
    else:
        classificacao="idosa"

    print(f'A média das idades é {media} e a turma é {classificacao}')

else:
    print("Nenhuma idade foi digitada")
    
    

