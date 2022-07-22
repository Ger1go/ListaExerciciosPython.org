#EXERCICIO 28..

#Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um.

quantCD = int(input("Digite a quantidade de CDs: "))
print("")

cont = 0
valorTotal = 0

for n in range(quantCD):
	valorCD = eval(input("Digite o valor do CD: "))
	valorTotal = valorTotal + valorCD
	valorMedio = valorTotal / quantCD
	cont += 1

print("")
print("O valor total investido: R$", valorTotal)
print("O valor médio de cada CD foi de: R$", valorMedio)
