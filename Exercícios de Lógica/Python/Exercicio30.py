'''
Exercicio 030
Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, 
que depende do salário bruto (conforme tabela abaixo) e 10% para o INSS e que o FGTS corresponde a 11% do Salário Bruto,
 mas não é descontado (é a empresa que deposita).

O Salário Líquido corresponde ao Salário Bruto menos os descontos. 
O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.

Desconto do IR: 
Salário Bruto até 900 (inclusive) - isento ; 
Salário Bruto até 1500 (inclusive) - desconto de 5% ; 
Salário Bruto até 2500 (inclusive) - desconto de 10% ; 
Salário Bruto acima de 2500 - desconto de 20%

Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.

    Salário Bruto: (5 * 220)        : R$ 1100,00
    (-) IR (5%)                     : R$   55,00
    (-) INSS ( 10%)                 : R$  110,00
    FGTS (11%)                      : R$  121,00
    Total de descontos              : R$  165,00
    Salário Liquido                 : R$  935,00
'''


horas=float(input("Digite quantas horas você trabalha no mês: "))
pagamento_hora = float(input("Digite quanto você recebe por hora: "))

salario_bruto = horas*pagamento_hora

if salario_bruto<=900:
    IR = salario_bruto*0
    INSS= salario_bruto*0.1
    FGTS = salario_bruto*0.11
    
    print(f"\nSalário Bruto: ({horas}*{pagamento_hora})                  : R$ {salario_bruto}")
    print(f"\n(-) IR (0%)                                 : R$ {IR}")
    print(f"\n(-) INSS (10%)                              : R$ {INSS}")
    print(f"\nFGTS (11%)                                  : R$ {FGTS}")
    print(f"\nTotal de descontos                          : R$ {IR+INSS}")
    print(f"\nSalário Líquido                             : R$ {salario_bruto-(IR+INSS)}")

elif salario_bruto<=1500:
    IR = salario_bruto*0.05
    INSS= salario_bruto*0.1
    FGTS = salario_bruto*0.11

    print(f"\nSalário Bruto: ({horas}*{pagamento_hora})                  : R$ {salario_bruto}")
    print(f"\n(-) IR (5%)                                 : R$ {IR}")
    print(f"\n(-) INSS (10%)                              : R$ {INSS}")
    print(f"\nFGTS (11%)                                  : R$ {FGTS}")
    print(f"\nTotal de descontos                          : R$ {IR+INSS}")
    print(f"\nSalário Líquido                             : R$ {salario_bruto-(IR+INSS)}")


elif salario_bruto<=2500:
    IR = salario_bruto*0.1
    INSS= salario_bruto*0.1
    FGTS = salario_bruto*0.11

    print(f"\nSalário Bruto: ({horas}*{pagamento_hora})                  : R$ {salario_bruto}")
    print(f"\n(-) IR (10%)                                : R$ {IR}")
    print(f"\n(-) INSS (10%)                              : R$ {INSS}")
    print(f"\nFGTS (11%)                                  : R$ {FGTS}")
    print(f"\nTotal de descontos                          : R$ {IR+INSS}")
    print(f"\nSalário Líquido                             : R$ {salario_bruto-(IR+INSS)}")


else:
    IR = salario_bruto*0.2
    INSS= salario_bruto*0.1
    FGTS = salario_bruto*0.11

    print(f"\nSalário Bruto: ({horas}*{pagamento_hora})                  : R$ {salario_bruto}")
    print(f"\n(-) IR (20%)                                : R$ {IR}")
    print(f"\n(-) INSS (10%)                              : R$ {INSS}")
    print(f"\nFGTS (11%)                                  : R$ {FGTS}")
    print(f"\nTotal de descontos                          : R$ {IR+INSS}")
    print(f"\nSalário Líquido                             : R$ {salario_bruto-(IR+INSS)}")


    

    
    