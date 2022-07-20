#EXERCICIO 7..

#Faça um Programa que leia três números e mostre o maior e o menor deles.

print("Digite tres números, e vamos descobrir qual é o maior e o menor deles!")
n1 = int(input("n°1: "))
n2 = int(input("n°2: "))
n3 = int(input("n°3: "))

print('\n')

#numero maior 

maior = n1

if n2 > n1 and n2 > n3:
  maior = n2
if n3 > n1 and n3 > n2:
  maior = n3

#numero menor

menor = n1

if n2 < n1 and n2 < n3:
  menor = n2
if n3 < n1 and n3 < n2:
  menor = n3

print(f" O maior deles é o numero {maior}!")
print(f" O menor deles é o numero {menor}!")