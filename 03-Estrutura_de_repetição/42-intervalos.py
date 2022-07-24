#EXERCICIO 42.. #######################################################

#Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos deles estão nos seguintes intervalos:

#[0-25], [26-50], [51-75] e [76-100].

#A entrada de dados deverá terminar quando for lido um número negativo.

n25 = []
n50 = []
n75 = []
n100 = []
numero = True
while numero > 0:
    numero = float(input("Digite um número: "))
    if numero > 0 and numero <= 25:
        n25.append(numero)
    elif numero > 25 and numero <= 50:
        n50.append(numero)
    elif numero > 50 and numero <= 75:
        n75.append(numero)
    elif numero > 75 and numero <= 100:
        n100.append(numero)

print('\n No intervalo de  0 até 25  tem : ', len(n25),'números') 
print('\n No intervalo de 25 até 50  tem : ', len(n50),'números')
print('\n No intervalo de 50 até 75  tem : ', len(n75),'números')
print('\n No intervalo de 75 até 100 tem: ', len(n100),'números')

