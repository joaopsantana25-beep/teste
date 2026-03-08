'''
Exercicio 108
Uma empresa de pesquisas precisa tabular os resultados da seguinte enquete feita a um grande quantidade de organizações: 
"Qual o melhor Sistema Operacional para uso em servidores?"

As possíveis respostas são:

1- Windows Server 2- Unix 3- Linux 4- Netware 5- Mac OS 6- Outro

Você foi contratado para desenvolver um programa que leia o resultado da enquete e informe ao final o resultado da mesma.
O programa deverá ler os valores até ser informado o valor 0, que encerra a entrada dos dados. 
Não deverão ser aceitos valores além dos válidos para o programa (0 a 6).
Os valores referentes a cada uma das opções devem ser armazenados num vetor. 
Após os dados terem sido completamente informados, o programa deverá calcular a percentual de cada um dos concorrentes e 
informar o vencedor da enquete. O formato da saída foi dado pela empresa, e é o seguinte:

Sistema Operacional Votos %

Windows Server 1500 17% Unix 3500 40% Linux 3000 34% Netware 500 5% Mac OS 150 2% Outro 150 2%

Total 8800

O Sistema Operacional mais votado foi o Unix, com 3500 votos, correspondendo a 40% dos votos.

'''
numero_de_votos=0
votos_sistemas_operacionais=[0]*6
sistemas_operacionais=["Windows Server","Unix","Linux","Netware","Mac OS","Outro"]


#Função para porcentagem
def porcento(votos_sistemas, total_votos):
    porcetangem=round(votos_sistemas*100/total_votos,1)
    return porcetangem

#Loop de leitura

while True:
    voto = int(input("Digite o voto do sistema operacional (para sair digite 0): "))

    if voto==0:
        print("Fim da Leitura")
        break

    if voto>6 or voto <1:
        print("Voto inválido")
        continue
    
    votos_sistemas_operacionais[voto-1]+=1
    numero_de_votos+=1

#Mostrar o resultado da votação
if numero_de_votos==0:
    print("Nenhum voto foi computado")
    print("Fim do Progama")

else:
    print("\nResultado da votação:")
    print(f"\nForam computados {numero_de_votos} votos.\n")

    print(f'{"Sistema Operacional":<20} {"Votos":>8} {"%":>8}')
    print("-" * 40)

    melhor_sistema = sistemas_operacionais[votos_sistemas_operacionais.index(max(votos_sistemas_operacionais))]

    for i in range(6):
        if votos_sistemas_operacionais[i]>0:
            percentual=porcento(votos_sistemas_operacionais[i],numero_de_votos)
            print(f'{sistemas_operacionais[i]:<20} {votos_sistemas_operacionais[i]:>8}  {percentual:>7}%')

    print(f'\nO total de votos foi {numero_de_votos}\n')
    print(f"O melhor sistema operacional foi {melhor_sistema} com {max(votos_sistemas_operacionais)} votos que corresponde a {porcento(max(votos_sistemas_operacionais),numero_de_votos)}% dos votos ")
    print("Fim do Programa!")