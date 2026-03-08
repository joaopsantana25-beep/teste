'''Exercicio 082
Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados: valor da dívida, valor dos juros, quantidade de parcelas e valor da parcela.

Os juros e a quantidade de parcelas seguem a tabela abaixo: Quantidade de Parcelas % de Juros sobre o valor inicial da dívida 1 0 3 10 6 15 9 20 12 25

Exemplo de saída do programa: Valor da Dívida, Valor dos Juros, Quantidade de Parcelas, Valor da Parcela R$ 1.000,00 0 1 R$ 1.000,00 R$ 1.100,00 100 3 R$ 366,00 R$ 1.150,00 150 6 R$ 191,67
'''

while True:
    valor_divida = float(input("Digite o valor da dívida: "))
    quantidade_parcelas = int(input("Digite a quantidade de parcelas (1,3,6,9,12): "))
    valor_juros = 0

    if quantidade_parcelas not in [1,3,6,9,12]:
        print("Por favor digite um valor válido")
        continue
    
    else:
        break

if quantidade_parcelas ==1:
    valor_juros=0

elif quantidade_parcelas==3:
    valor_juros=0.10

elif quantidade_parcelas==6:
    valor_juros=0.15

elif quantidade_parcelas==9:
    valor_juros=0.20

elif quantidade_parcelas==12:
    valor_juros=0.25


    


valor_dos_juros = valor_divida*valor_juros
valor_divida_com_juros = valor_divida+valor_dos_juros
valor_parcela =((valor_divida_com_juros/quantidade_parcelas))


print(f'Valor da dívida: R$ {valor_divida_com_juros:.2F}')
print(f'Valor dos juros: R$ {valor_dos_juros:.2F}')
print(f'Quantidade de parcelas: R$ {quantidade_parcelas}')
print(f'Valor das parcelas: R$ {valor_parcela:.2F}')