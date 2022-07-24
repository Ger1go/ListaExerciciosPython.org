#EXERCICIO 34..

#Os números primos possuem várias aplicações dentro da Computação, por exemplo na Criptografia. Um número primo é aquele que é divisível apenas por um e por ele mesmo. Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.


num = int(input('Digite um numero inteiro para saber se ele é um número primo: \n'))

c = 1
cont = 0 

for c in range(1, num+1):
  if num % c == 0:
    cont += 1

if cont == 2:
    print('É um número primo.')
else:
  print('Não é um número primo.')
