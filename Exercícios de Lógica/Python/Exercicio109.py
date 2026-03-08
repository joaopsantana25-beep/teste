'''Exercicio 109
As Organizações Tabajara resolveram dar um abono aos seus colaboradores em reconhecimento ao bom resultado alcançado durante
o ano que passou. 
 
Para isto contratou você para desenvolver a aplicação que servirá como uma projeção de quanto será gasto com o pagamento deste 
abono. Após reuniões envolvendo a diretoria executiva, a diretoria financeira e os representantes do sindicato laboral, 
chegou-se a seguinte forma de cálculo:

Cada funcionário receberá o equivalente a 20% do seu salário bruto de dezembro;

O piso do abono será de 100 reais, isto é, aqueles funcionários cujo
salário for muito baixo recebem este valor mínimo;

Neste momento, não se deve ter nenhuma preocupação com colaboradores com
tempo menor de casa, descontos, impostos ou outras particularidades.

Seu programa deverá permitir a digitação do salário de um número indefinido (desconhecido) de salários.
Um valor de salário igual a 0 (zero) encerra a digitação. 
Após a entrada de todos os dados o programa deverá calcular o valor do abono concedido a cada colaborador, 
de acordo com a regra definida acima. 
Ao final, o programa deverá apresentar: 

O salário de cada funcionário, juntamente com o valor do abono; 
O número total de funcionários processados; 
O valor total a ser gasto com o pagamento do abono; 
O número de funcionários que receberão o valor mínimo de 100 reais; 
O maior valor pago como abono;
'''

salarios=[]
abonos=[]
salarios_abonados=[]
abono_minimo=100

numero_de_funcionarios=0
numero_de_funcionarios_100reais=0


while True:
    salario=float(input("Digite o salário: "))

    if salario ==0:
        print("Fim da leitura")
        break

    if salario<0:
        print("Digite um salário válido!")
        continue

    
    abono = salario*0.2
    
    if abono<=abono_minimo:
        abono=abono_minimo
        numero_de_funcionarios_100reais+=1

    salarios.append(salario)
    abonos.append(abono)
    salarios_abonados.append(salario+abono)
    numero_de_funcionarios+=1

if numero_de_funcionarios==0:
    print("Nenhum funcionário registrado!")
    print("Fim do Progama!")

else:
    #O salário de cada funcionário, juntamente com o valor do abono; 
    print("\nResultado do processo:")

    print(f'{"Salario":<10} {"Abono":>10} {"Salario+Abono":>20}')
    print("-" * 40)

    for i in range(len(salarios)):
        print(f'{salarios[i]:<10.2f} {abonos[i]:>10.2f} {salarios_abonados[i]:>20.2f}')
    
    #O número total de funcionários processados; 
    print(f'\nAo todo foram processados {numero_de_funcionarios} funcionários')

    #O valor total a ser gasto com o pagamento do abono;
    print(f"\nAo todo será gasto, apenas com abonos, o total de R$ {sum(abonos):.2f} reais.")
    print(f'\nSerá gasto um total de R$ {sum(salarios_abonados):.2f} reais.')

    #O número de funcionários que receberão o valor mínimo de 100 reais; 
    print(f"\n{numero_de_funcionarios_100reais} funcionários receberão o abono mínimo de R$ 100,00 reais")

    #O maior valor pago como abono;
    print(f"\nO maior abono pago foi de R$ {max(abonos):.2f} reais.")

    print(f"\nFim do Programa!")

