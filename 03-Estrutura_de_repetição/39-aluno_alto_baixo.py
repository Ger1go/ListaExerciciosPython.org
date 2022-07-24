#EXERCICIO 39..

#Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno e o segundo representando a sua altura em centímetros. Encontre o aluno mais alto e o mais baixo. Mostre o número do aluno mais alto e o número do aluno mais baixo, junto com suas alturas.

cod_alunos = [] 
altura_alunos = []

alu = 1
codigo = 1

while codigo != 0:
 print(f'Aluno n°{alu}')
 codigo = int(input('Digite o código: '))
 if codigo == 0:
   continue
 altura = int(input('Digite a altura: '))
 print('-------')
 cod_alunos.append(codigo)
 altura_alunos.append(altura)

 alu += 1

else:
  alto = altura_alunos.index(max(altura_alunos)) 
  baixo = altura_alunos.index(min(altura_alunos))
 
  print('---------------------------------------------','\n'*2)
  print(f'O aluno mais alto é o do codigo {cod_alunos[alto]}. \n Com uma altura de {altura_alunos[alto]}cm .\n')
  print(f'O aluno mais baixo é o do codigo {cod_alunos[baixo]}. \n Com uma altura de {altura_alunos[baixo]}cm .\n')

  