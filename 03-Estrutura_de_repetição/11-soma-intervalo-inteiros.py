#EXERCICIO 11..

#Altere o programa anterior para mostrar no final a soma dos números.

num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))
soma = 0

for num in range( num1 +1,num2):
  print(num, end = ' ')
  soma += num

print()

print(f'soma é : {soma}')