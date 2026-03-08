'''
Exercicio 060
A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o n−ésimo termo.
'''

lista=[1,1]

n = int(input("Digite até que termo da sequência você deseja ver: "))

if n ==1:
   print([1])

elif n == 2:
   print(lista)

else: 
    for i in range (n-2):
        fibonachi = lista[i+1] + lista[i]
        lista.append(fibonachi)



print(lista)