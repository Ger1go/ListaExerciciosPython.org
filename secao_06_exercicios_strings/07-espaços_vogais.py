#EXERCICIO 7...

#Conta espaços e vogais. Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte:

#1-quantos espaços em branco existem na frase.

#2-quantas vezes aparecem as vogais a, e, i, o, u.


frase = input('Digite uma frase: ')
vogais = 0 
espaços = 0 
for letra in frase:
  if letra == ' ':
    espaços += 1
  elif letra in "aeiou":
    vogais += 1

print(f'A frase tem {vogais} vogais e {espaços} espaços. ')

