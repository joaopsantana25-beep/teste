'''
Exercicio 070
Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.
'''

numero_de_eleitores = int(input("Digite o número de eleitores: "))

votos_candidato1=0
votos_candidato2=0
votos_candidato3=0

while True:
    voto = int(input("Digite 1 para votar no candidato 1; 2 para o canditado 2; 3 para o candidato 3: "))

    if voto ==1:
        votos_candidato1+=1
    
    elif voto==2:
        votos_candidato2+=1

    elif voto==3:
        votos_candidato3+=1

    else:
        print("Voto inválido, tente novamente")
        continue

    numero_de_eleitores-=1
    print("Voto registrado com sucesso!")

    if numero_de_eleitores==0:
        break

print(f"O candidato 1 recebeu {votos_candidato1} votos.")
print(f"O candidato 2 recebeu {votos_candidato2} votos.")
print(f"O candidato 3 recebeu {votos_candidato3} votos.")