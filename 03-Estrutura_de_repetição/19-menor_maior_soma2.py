#EXERCICIO 19..

#Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.

num = []


q = int(input('Quantidade de numeros: '))

if q < 0 or q > 1000:
  q = int(input(' O número deve ser entre 0 e mil, por avor digite a quantidade de numeros novamente: '))

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
