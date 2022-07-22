#EXERCICIO 21..

#Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que é divisível somente por ele mesmo e por 1.

num = int(input('Digite um número inteiro patra descobrir se é um numero primo: '))
tot = 0
noprim = [] 
for c in range(1, num +1):
    if num % c == 0:
      tot += 1
      

if tot == 2:
  print(f'Ele é um número primo porque é divisivel entre 1 e {num}')
else:
    print('Ele não é um número primo')