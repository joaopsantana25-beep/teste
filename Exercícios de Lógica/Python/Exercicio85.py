'''Exercicio 085
Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código.
Os códigos utilizados são: 1, 2, 3, 4 - Votos para os respectivos candidatos 
(você deve montar a tabela ex: 1 - Jose/ 2- João/etc) 5 - Voto Nulo 6 - Voto em Branco

Faça um programa que calcule e mostre: O total de votos para cada candidato;
O total de votos nulos; O total de votos em branco; A percentagem de votos nulos sobre o total de votos; 
A percentagem de votos em branco sobre o total de votos.

Para finalizar o conjunto de votos tem-se o valor zero.'''
candidato1=0
candidato2=0
candidato3=0
candidato4=0
votoNulo=0
VotoEmBranco=0
totalDeVotos=0

while True:
    voto = int(input("Digite seu voto(para sair digite 0): "))

    if voto ==0:
        break
    elif voto==1:
        candidato1+=1
    elif voto==2:
        candidato2+=1
    elif voto==3:
        candidato3+=1
    elif voto==4:
        candidato4+=1
    elif voto ==5:
        votoNulo+=1
    elif voto==6:
        VotoEmBranco+=1

    totalDeVotos+=1


    
if not totalDeVotos:
    print("Não houve votos")

else:
    print(f"O primeiro candidato recebeu {candidato1} votos")

    print(f"O segundo candidato recebeu {candidato2} votos")

    print(f"O terceiro candidato recebeu {candidato3} votos")

    print(f"O quarto candidato recebeu {candidato4} votos")

    print(f'Houve um total de {totalDeVotos} votos. Sendo {votoNulo} votos nulos que é {votoNulo*100/totalDeVotos:.2f}% dos votos totais e {VotoEmBranco} votos em branco que é {VotoEmBranco*100/totalDeVotos:.2f}% dos votos totais')
