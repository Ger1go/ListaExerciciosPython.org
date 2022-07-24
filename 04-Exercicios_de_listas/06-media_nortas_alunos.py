#EXERCICIO 6..

#Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.

print('Vamos ver a média dos alunos que foram aprovados.\n')

listaNotas = []
notasAluno = []

for i in range(10):
  media = 0
  notasAluno = []
  print ('>>>>>>>>>>>>>>>>>>> ALUNO ' + str(i + 1) + ' <<<<<<<<<<<<<<<<<<<' )
  for j in range(4):
    notasAluno.append(float(input('Nota ' + str(j+1) + ': \n')))
    media += notasAluno[j]
    
  media = media/4
  if media >= 7:
    listaNotas.append(media)
print(listaNotas)
total = len(listaNotas)

print(f'No total, temos {total} aluno(s) com média maior ou igual a 7. ')