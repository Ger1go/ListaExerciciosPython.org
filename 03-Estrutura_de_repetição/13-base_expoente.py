#EXERCICIO 13..

#Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número. Não utilize a função de potência da linguagem.

print('Digite dois numeros, base e expoente para calcular a sua potencia \n')
base = int(input('BASE: '))
expo = int(input('EXPOENTE: ')) 

cont = 1 
potencia = 1

while cont <= expo :
  potencia *=  base
  cont += 1

print(f' A potencia de {base} elevado a {expo} é {potencia}')

