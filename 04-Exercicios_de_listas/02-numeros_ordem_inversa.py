#EXERCICIO 2..

#Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.

num = []

for c in range(10):
	n = int(input('Digite um número '))
	num.append(n)

num.reverse() 
print(num)

