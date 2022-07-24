#EXERCICIO 35..

#Encontrar números primos é uma tarefa difícil. Faça um programa que gera uma lista dos números primos existentes entre 1 e um número inteiro informado pelo usuário.

num = int(input('Digite um numero inteiro para saber quantos números primos existem entre o número 1 e o número escolhido: \n'))


listcont = []
cont = 0 



for c in range(1, num + 1):
  tot = 0
  for j in range(1, c + 1):
    if c % j == 0:
      tot += 1
      cont += 1
    else:
      cont += 1

  if tot == 2:
    listcont.append(c)

print(f'A lista de números é : {listcont} ')

