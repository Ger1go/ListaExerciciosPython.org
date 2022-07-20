#EXERCICIO 9.. Faça um Programa que leia três números e mostre-os em ordem decrescente.

print('Digite três numeros: \n')

lista = []

for n in range(3):
    n = int(input(f'Digite o numero {n+1}: '))
    lista.append(n)
  
print()
lista.sort(reverse=True)
print('Seus números em ordem decrescente são: ', lista)

