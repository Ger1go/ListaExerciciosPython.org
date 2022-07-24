#EXERCICIO 4..

#Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.

vogal = ['A','E','I','O','U']
vogais = []
consoantes = []
cont = 1

for i in range(10):
  c = input(f'Digite {cont}° caracter: ').upper()
  cont += 1
  if c in vogal:
    vogais.append(c)
  else:
    consoantes.append(c)
q = len(consoantes)

print(f'Você digitou {q} consoantes, e elas são : {consoantes}. ')