'''Exercicio 102
Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.
'''
vetorA=[1,2,3,4,5,6,7,8,9,10]
vetorB=[11,12,13,14,15,16,17,18,19,20]
vetorC=[21,22,23,24,25,26,27,28,29,30]
vetorD=[]

for a,b,c in zip(vetorA,vetorB,vetorC):
    vetorD.append(a)
    vetorD.append(b)
    vetorD.append(c)


print(vetorD)
