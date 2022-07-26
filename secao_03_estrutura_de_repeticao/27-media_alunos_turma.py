#EXERCICIO 27 ..

#Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma. As turmas não podem ter mais de 40 alunos.

num_turmas = int(input('Por favor digite o número de turmas que deseja calcular: '))
print()
cont = 1
total_alunos = [] 

print('Por favor digite o número de alumnos de cada turma: \n')

for a in range(num_turmas):
  num_alum = int(input(f'Quantos alúnos tem a turma {cont})? : \n'))
  if num_alum > 40:
    num_alum = int(input(f'A turma {cont})não pode ter mais de 40 alúnos por favor digite um novo valor: '))
  cont += 1
  total_alunos.append(num_alum)

media = int( sum(total_alunos) / len(total_alunos))

print()

print(f'a média de alunos por turma é de: {media} alunos. ')