#EXERCICIO 2..

#Faça um programa para imprimir:

#1
#1   2
#1   2   3
#.....
#1   2   3   ...  n
#para um n informado pelo usuário. Use uma função que receba um valor n inteiro imprima até a n-ésima linha.

def imprimir_triangulo_de_numeros(n):
  for i in range(1, n + 1):
    for j in range(1,i +1):
      print(j, end='   ')
    print('')

n = int(input('digite um numero inteiro: '))
imprimir_triangulo_de_numeros(n)
