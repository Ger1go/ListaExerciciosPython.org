#EXERCICIO 8 ..

#Faça um programa que leia 5 números e informe a soma e a média dos números.

numeros = []

for c in range(1, 6):
  numeros.append(int(input('Digite 5 numeros: ')))

soma = 0

for c in numeros:
  soma += c

print(f'soma de números é : {soma}')

#----media

media = float(soma / len(numeros))

print(f'A media dos números é: {media} ')

