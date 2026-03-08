'''
Exercicio 076
O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia as um conjunto indeterminado de temperaturas, e informe ao final a menor e a maior temperaturas informadas, bem como a média das temperaturas.
'''

while True:
    lista_de_temperaturas = []

    while True:
        temperatura = (input("Digite a temperatura, para sair digite sair: ")).lower()

        if temperatura in ['sair','']:
            break

        lista_de_temperaturas.append(float(temperatura))

    if lista_de_temperaturas:
        print(f"A menor temperatua digitada é {min(lista_de_temperaturas)}")
        print(f"A maior temperatua digitada é {max(lista_de_temperaturas)}")
        print(f"A média das temperaturas digitadas é {(sum(lista_de_temperaturas)/len(lista_de_temperaturas)):.2f}")

    else:
        print("Nenhuma temperatura foi digitada")

    if input("Para sair aperte enter, para uma nova sessão digite algo: ") =='':
        print('Fim do Programa')
        break
        