#EXERCICIO 3..

#Faça um Programa que leia 4 notas, mostre as notas e a média na tela

lista = []

for c in range(4):
  n = float(input('Digite a nota: '))
  lista.append(n)

print(f'As quatro notas são : {lista}')
media = sum(lista) / len(lista)
print(f'A média de notas é : {media}')