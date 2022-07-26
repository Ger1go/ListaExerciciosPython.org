#EXERCICIO 6.. Faça um Programa que leia três números e mostre o maior deles.

print("Digite tres números, e vamos descobrir qual é o maior deles!")
n1 = int(input("n°1: "))
n2 = int(input("n°2: "))
n3 = int(input("n°3: "))

print('\n')

#------------------------------------------------------primeiro metodo:
#if n1 > n2 and n3:
  #print(f'O n°1 {n1} é o maior!')
#if n2 > n2 and n1:
  #print(f'O n°2 {n2} é o maior!')
#elif n3 > n1 and n2:
  #print(f'O n°3 :{n3} é o maior!')
#------------------------------------------------------

#segundo metodo: 

maior = n1

if n2 > n1 and n2 > n3:
  maior = n2
if n3 > n1 and n3 > n2:
  maior = n3

print(f" O maior deles é o numero {maior}!")