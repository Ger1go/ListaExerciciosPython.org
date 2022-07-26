#EXERCICIO 8..

#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

print(" Digite o preço de três produtos para saber qual deve comprar! ")

print('\n')

a = int(input('Produto 1:R$'))
b = int(input('Produto 2:R$'))
c = int(input('Produto 3:R$'))

barato = a

if b < a and b < c:
  barato = b

if c < a and c < b: 
  barato = c

print(f'O produto mais barato é o de: R${barato}!')

