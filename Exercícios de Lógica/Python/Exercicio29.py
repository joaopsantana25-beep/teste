'''
Exercicio 029
As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contrataram para desenvolver o programa que calculará os reajustes.

Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:

salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante :
    aumento de 5% Após o aumento ser realizado,
informe na tela:
    o salário antes do reajuste;
    o percentual de aumento aplicado;
    o valor do aumento;
    o novo salário, após o aumento.
'''

salario = float(input("Digite o seu salário: "))
salario_reajustado=0

if salario <=280:
    salario_reajustado=salario*1.2
    print(f"O seu salário antes do reajuste era: {salario} \nO percentual de aumento aplicado foi de: 20%\n O aumento foi de {salario_reajustado-salario}\nE seu novo salário será de: {salario_reajustado}")

elif salario>280 and salario<=700:
    salario_reajustado=salario*1.15
    print(f"O seu salário antes do reajuste era: {salario} \nO percentual de aumento aplicado foi de: 15%\nO aumento foi de {salario_reajustado-salario}\nE seu novo salário será de: {salario_reajustado}")

elif salario>700 and salario<=1500:
    salario_reajustado=salario*1.1
    print(f"O seu salário antes do reajuste era: {salario} \nO percentual de aumento aplicado foi de: 10%\nO aumento foi de {salario_reajustado-salario}\nE seu novo salário será de: {salario_reajustado}")

else:
    salario_reajustado=salario*1.05
    print(f"O seu salário antes do reajuste era: {salario} \nO percentual de aumento aplicado foi de: 5%\nO aumento foi de {salario_reajustado-salario}\nE seu novo salário será de: {salario_reajustado}")

