# EXERCICIO 13..

# Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

val = int(input('Digite um número para saber a qual dia da semana ele corresponde: \n'))

if val == 1:
  print('Seu dia é Domingo!')
elif val == 2:
  print('Seu dia é Segunda!')
elif val == 3:
  print('Seu dia é Terça!')
elif val == 4:
  print('Seu dia é Quarta!')
elif val == 5:
  print('Seu dia é Quinta!')
elif val == 6:
  print('Seu dia é Sexta!')
elif val == 7:
  print('Seu dia é Sabado!')
else:
  print('Valor invalido!')