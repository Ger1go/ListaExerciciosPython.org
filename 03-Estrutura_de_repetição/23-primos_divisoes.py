#EXERCICIO 23...

#Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário. O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos. Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.

num = int(input('Digite um número inteiro para descorbir todos os números primos que existem entre 1 e o número escolhido: \n'))
 
listcont = []
cont = 0 



for c in range(1, num + 1,2):
  tot = 0
  for j in range(1, c + 1):
    if c % j == 0:
      tot += 1
      cont += 1
    else:
      cont += 1

  if tot == 2:
    listcont.append(c)

print(f'A lista de números é : {listcont} ')
print(f'O número de divisões foi {cont}')