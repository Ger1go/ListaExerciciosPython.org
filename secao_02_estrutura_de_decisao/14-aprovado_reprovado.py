#EXERCICIO 14..

#Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:

#Média de Aproveitamento Conceito

#Entre 9.0 e 10.0 A

#Entre 7.5 e 9.0 B

#Entre 6.0 e 7.5 C

#Entre 4.0 e 6.0 D

#Entre 4.0 e zero E

#O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.

print('Vamos descobrir qual foi a atribuição da su anota média! \n')
n1 = int(input('Informe a sua primeira nota do parcial: '))
n2 = int(input('Informe a sua segunda nota do parcial: '))
print()
M = (n1 + n2) / 2
print(f'Sua primeira nota foi {n1}.')
print(f'Sua segunda nota foi {n2}.')
print(f'Sua media é de {M}.')

if M >= 9.0 and M <=10.0:


  print('Sua nota é A, você foi aprovado!')
if M >= 7.5 and M <=9.0:
  print('Sua nota é B, você foi aprovado!')
if M >= 6.0 and M <7.5:
  print('Sua nota é C, você foi aprovado!')
if M >= 4.0 and M <6.0:
  print('Sua nota é D, você foi reprovado!')
if M < 4.0:
  print('Sua nota é E, você foi reprovado!')
