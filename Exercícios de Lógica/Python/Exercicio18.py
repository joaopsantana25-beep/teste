'''
Exercicio 018

Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

'''

tamanho_arquivo=float(input("Digite o tamanho do arquivo (MB): "))
velocidade = float(input("Digite a velocidade de download (Mbps): "))

tempo = (tamanho_arquivo*8/velocidade)/60

print(f"Vai demorar aproximadamente {tempo} minutos para baixar o arquivo")