'''
Exercicio 056
Altere o programa anterior para mostrar no final a soma dos números.
'''

num1 = int(input("Digite o começo do intervalo: "))

num2 = int(input("Digite o fim do intervalo: "))
soma = 0

if num1<=num2:
    for i in range(num1+1,num2,1):
        print(i)
        soma+=i
    
    print(f"A soma dos números é {soma}")

else:
    for i in range(num1-1,num2,-1):
        print(i)
        soma+=i
    
    print(f"A soma dos números é {soma}")
