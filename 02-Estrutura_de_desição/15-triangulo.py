#EXERCICIO 15.. Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.

#Dicas:

#Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;

#Triângulo Equilátero: três lados iguais;

#Triângulo Isósceles: quaisquer dois lados iguais;

#Triângulo Escaleno: três lados diferentes;

print('Digite as três medidas para descobrir se pode ser um triangulo, e qual tipo de triangulo ele é: ')
L1 = float(input('Primeira medida: '))
L2 = float(input('Segunda medida: '))
L3 = float(input('Trimeira medida: '))
print()

if L1 < L2 + L3 and L2 < L3 + L1 and L3 < L1 + L2:
  print('Ótimo! suas medidas formam um TRIANGULO! ')
else:
  print('Suas medidas não formam um TRIANGULO.')
if L1 == L2 == L3:
  print("E seu triangulo é um triangulo EQUILATERO!")
elif L1 != L2 != L3 != L1:
  print("E seu triangulo é um triangulo ESCALENO!")
else:
  print("E seu triangulo é um triangulo ISOSCELES!")
