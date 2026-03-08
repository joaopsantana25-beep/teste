'''
Exercicio 079
Um funcionário de uma empresa recebe aumento salarial anualmente.

Sabe-se que: Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00; 
Em 1996 recebeu aumento de 1,5% sobre seu salário inicial; A partir de 1997 (inclusive), os aumentos salariais sempre 
correspondem ao dobro do percentual do ano anterior.

Faça um programa que determine o salário atual desse funcionário. Após concluir isto, altere o programa permitindo 
que o usuário digite o salário inicial do funcionário.
'''

salario = float(input("Digite o salário: "))
percentual_de_aumento = 1.5/100

for i in range(1996,2025):
    salario = salario*(1+percentual_de_aumento)
    print(f"Salário em {i}: R$ {salario:.2f} (aumento de {percentual_de_aumento*100:.2f}%) )")
    percentual_de_aumento=percentual_de_aumento*2

print(f'O salário atualmente é : R$ {salario:.2f}')