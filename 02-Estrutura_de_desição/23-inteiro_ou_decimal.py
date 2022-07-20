#EXERCICIO 23.. Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de arredondamento.

num = float(input('Digite um numero para saber se ele é um inteiro ou decimal: '))

if num % 1 == 0:
  print('Seu numero é inteiro.')
else:
    print('Seu numero é decimal.')

    