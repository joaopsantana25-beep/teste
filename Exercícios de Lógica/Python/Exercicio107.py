'''Exercicio 107
Uma grande emissora de televisão quer fazer uma enquete entre os seus telespectadores para saber qual o melhor jogador após 
cada jogo. Para isto, faz-se necessário o desenvolvimento de um programa, que será utilizado pelas telefonistas, 
para a computação dos votos. Sua equipe foi contratada para desenvolver este programa. Para computar cada voto, 
a telefonista digitará um número, entre 1 e 23, correspondente ao número da camisa do jogador.
Um número de jogador igual zero, indica que a votação foi encerrada. 
Se um número inválido for digitado, o programa deve ignorá-lo, mostrando uma breve mensagem de aviso, 
e voltando a pedir outro número. Após o final da votação, o programa deverá exibir: 

O total de votos computados; 
Os númeos e respectivos votos de todos os jogadores que receberam votos; 
O percentual de votos de cada um destes jogadores; 
O número do jogador escolhido como o melhor jogador da partida, 
juntamente com o número de votos e o percentual de votos dados a ele. 

Observe que os votos inválidos e o zero final não devem ser computados como votos. 
O resultado aparece ordenado pelo número do jogador. O programa deve fazer uso de arrays.
O programa deverá executar o cálculo do percentual de cada jogador através de uma função. 
Esta função receberá dois parâmetros: o número de votos de um jogador e o total de votos. 
A função calculará o percentual e retornará o valor calculado.

Exemplo: Enquete: Quem foi o melhor jogador?

Número do jogador (0=fim): 9 Número do jogador (0=fim): 10 Número do jogador (0=fim): 9 Número do jogador (0=fim): 10 Número do jogador (0=fim): 11 Número do jogador (0=fim): 10 Número do jogador (0=fim): 50 Informe um valor entre 1 e 23 ou 0 para sair! Número do jogador (0=fim): 9 Número do jogador (0=fim): 9 Número do jogador (0=fim): 0

Resultado da votação:

Foram computados 8 votos.

Jogador Votos % 9 4 50,0% 10 3 37,5% 11 1 12,5% O melhor jogador foi o número 9, com 4 votos, correspondendo a 50% do total de votos.
'''

numero_de_votos=0
jogadores = [0] * 23

while True:
    voto=int(input("\nDigite o voto: "))

    if voto ==0:
        print("Fim da Votação")
        break

    if voto>23 or voto<0:
        print("Voto inválido")
        continue

    print("Voto Computado")
    jogadores[voto-1]+=1
    numero_de_votos+=1

#Funçao de porcentagem de votos
def porcento(votos_jogador, total_votos):
    porcetangem=round(votos_jogador*100/total_votos,2)
    return porcetangem

#Mostrar o resultado da votação
if numero_de_votos==0:
    print("Nenhum voto foi computado")
    print("Fim do Progama")

else:
    print("\nResultado da votação:")
    print(f"\nForam computados {numero_de_votos} votos.\n")

    print(f'{"Jogador":^12} | {"Votos":^12} | {"%":^12}')
    print("-" * 40)

    for i in range(23):
        if jogadores[i] > 0:
            percentual = porcento(jogadores[i], numero_de_votos)
            print(f'{i+1:^12} | {jogadores[i]:^12} | {percentual:^11}%')

    print(f"\nO melho jogador foi o camisa {jogadores.index(max(jogadores))+1}, com {max(jogadores)} votos correspondendo a {porcento(max(jogadores),numero_de_votos)} do total de votos.")

print("Fim do Programa")