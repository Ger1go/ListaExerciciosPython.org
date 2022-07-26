#EXERCICIO 24..

#Faça um programa que calcule o mostre a média aritmética de N notas.

print('Vamos criar um programa que calcule a média de notas.')
nu_no = int(input('Quantas notas deseja calcular? \n'))
lista_nota= []
for c in range(nu_no):
  nota = int(input('Digite a nota: '))
  lista_nota.append(nota)
    
total = float(sum(lista_nota) / len(lista_nota))

print(f'A média da suas notas é {total:.2} .')

