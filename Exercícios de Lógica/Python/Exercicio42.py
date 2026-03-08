'''
Exercicio 042
Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são: "Telefonou para a vítima?" "Esteve no local do crime?" "Mora perto da vítima?" "Devia para a vítima?" "Já trabalhou com a vítima?"

O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.

Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
'''
lista=["Telefonou para a vítima? ", "Esteve no local do crime? " ,"Mora perto da vítima? ", "Devia para a vítima? " ,"Já trabalhou com a vítima? "]
contador = 0


for i in range (0,5,1):
    resposta = input(lista[i]).lower()

    if resposta == "s":
        contador +=1


if contador ==2:
    pessoa = "suspeita"

elif contador>2 and contador<5:
    pessoa = "Cúmplice"

elif contador==5:
    pessoa = "Assassino"

else:
    pessoa = "Inocente"

print(f"Pelas respostas dadas a pessoa é considerada {pessoa}.")