#EXERCICIO 5

#Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.

listaPar = []
listaImpar = []
listaNumeros = []
numero = 0

print('Informe os números:')
for i in range(20):
  listaNumeros.append((int(input('Número ' + str(i+1) + ':\n' ))))
  numero = listaNumeros[i]
  if(numero%2 == 0):
        listaPar.append(numero)
  else:
 		listaImpar.append(numero)

print(f'A lista de números total é : {listaNumeros}')
print(f'A lista de números pares é : {listaPar}')
print(f'A lista de números impar é : {listaImpar}')

