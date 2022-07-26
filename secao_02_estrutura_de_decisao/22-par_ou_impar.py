#EXERCICIO 22..
#Faça um Programa que peça um número inteiro e determine se ele é par ou impar. Dica: utilize o operador módulo (resto da divisão).

num = int(input('Digite um numero inteiro e vamos descobrir juntos se o seu número é par ou impar: '))
print()
num = num % 2
if num == 1:
  print(' Eita! seu número inteiro é ÍMPAR!')
else:
  print('Eita! seu número inteiro é PAR! ')

  