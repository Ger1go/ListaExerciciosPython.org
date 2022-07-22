#EXERCICIO 25..

#Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade da turma varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.

print('Vamos criar um programa que calcule a média de etária na sua turma:')
nu_pessoas = int(input('Quantas pessoas tem na sua turma? \n'))
lista_idade= []

nota = int(input('Digite a primeira idade: '))
lista_idade.append(nota)

for c in range(nu_pessoas - 1):
  nota = int(input('Digite a proxima idade: '))

  lista_idade.append(nota)

    
total = int(sum(lista_idade) / len(lista_idade))

if 0 < total <=25:
  media = "jovem"
elif 26 <= total <= 60:
  media = "adulta"
else:
  media = 'idosa'
print()

print(f'A media de idade é de {total}, você forma parte de uma turma {media}. ')