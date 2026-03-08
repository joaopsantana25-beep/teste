'''Exercicio 086
Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões,
o programa deve perguntar ao aluno a resposta de cada questão e ao final comparar com o gabarito da prova
e assim calcular o total de acertos e a nota (atribuir 1 ponto por resposta certa).

Após cada aluno utilizar o sistema deve ser feita uma pergunta se outro aluno vai utilizar o sistema.

Após todos os alunos terem respondido informar: Maior e Menor Acerto; 
Total de Alunos que utilizaram o sistema; 
A Média das Notas da Turma. 
Gabarito da Prova: 01 - A 02 - B 03 - C 04 - D 05 - E 06 - E 07 - D 08 - C 09 - B 10 - A

Após concluir isto você poderia incrementar o programa permitindo que o professor digite o 
gabarito da prova antes dos alunos usarem o programa.
'''

gabarito=[]
notas=[]
total_de_notas=0
numeros_alunos=0

for i in range(10):
    resposta = input(f"Digite a resposta da pergunta {i+1}: ").lower()
    gabarito.append(resposta)

while True:
    nota=0

    for i in range(10):
        resposta=input(f'Digite a sua resposta da pergunta {i+1}: ').lower()

        if resposta==gabarito[i]:
            nota+=1
    
    notas.append(nota)
    total_de_notas+=nota
    numeros_alunos+=1
        
    opcao = input('Outro aluno irá usar esse programa(s/n): ').lower()

    if opcao=='n':
        break
        
print(f'A maior nota tirada foi {max(notas)}')
print(f'A menor nota tirada foi {min(notas)}')
print(f'A media de notas da turma foi {total_de_notas/numeros_alunos:.2f}')
