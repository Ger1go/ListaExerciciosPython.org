#EXERCICIO 12..

#Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.

alunos = []
Quant_Alunos = 30

for i in range(0, Quant_Alunos):
    aluno = []
    aluno.append(int(input(f'Informe a idade do {i+1}º aluno: ')))
    aluno.append(float(input(f'Informe a altura do {i+1}º aluno: ')))
    alunos.append(aluno)

somaAltura = 0.0
for aluno in alunos:
    somaAltura += aluno[1]



mediaAltura = somaAltura / float(Quant_Alunos)

totAlunosAltos = 0
for aluno in alunos:
    if (aluno[0] >= 13) and (aluno[1] >= mediaAltura):
        totAlunosAltos += 1

print(f'Existem {totAlunosAltos} alunos com mais de 13 anos acima da media de altura')