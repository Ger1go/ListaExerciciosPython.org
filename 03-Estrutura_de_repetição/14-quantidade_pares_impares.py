#EXERCICIO 14..

#Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.

pares = 0 
impares = 0 

for n in range(10):
    if int(input('Digite um número: ')) % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f' Temos {pares} números pares e {impares} números impares. ')
