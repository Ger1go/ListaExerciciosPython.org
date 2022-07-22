#EXERCICIO 18..

#Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.

num = []

q = int(input('Quantidade de numeros: '))

for n in range(q):
  num.append(int(input('Digite um número: ')))


#------------------------------------------------
#MENOR NÚMERO

menornum = num[0]

cont = 1
while cont < len(num):
    if num[cont] < menornum:
        menornum = num[cont]
    cont = cont + 1

print(f"O menor numero é {menornum}")

#-----------------------------------------------
#MAIOR NÚMERO 

maiornum = num[0]

cont = 1
while cont < len(num):
    if num[cont] > maiornum:
        maiornum = num[cont]
    cont = cont + 1
        
print(f"O maior numero é {maiornum}")

#----------------------------------------------
#SOMA



soma = 0

for c in num:
  soma += c

print(f'soma de números é : {soma}')