#EXERCICIO 17..

#Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário.

#Ex.: 5!=5.4.3.2.1=120

fat = int(input('Digite um numero inteiro para calcular a sua expressão fatorial: '))

cont = fat
f = 1

print(f'Calculando {fat}! = ', end = '')
while cont > 0:
    print(f'{cont}', end = '')
    print(f' x ' if cont > 1 else ' = ', end = '')
    f *= cont
    cont -= 1

print(f'{f}')