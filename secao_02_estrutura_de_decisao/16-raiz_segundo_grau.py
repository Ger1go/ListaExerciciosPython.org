# EXERCICIO 16.. Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:

# -Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve pedir os demais valores, sendo encerrado;

# -Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;

# -Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;

# -Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;


import math

print("Vamos calcular as raízes de uma equação do segundo grau, na forma ax2 + bx + c. Por favor, insira os valores correspondentes de 'a', 'b', e, 'c': ")
a = float(input("Valor para 'a': "))
if a == 0:
  print('A equação não é de segundo grau, programa encerrado.')
else:
  b = float(input("Valor para 'b': "))
  c = float(input("Valor para 'c': "))

  delta = math.pow(b, 2) - (4*a*c)

  if delta < 0.00:
    print('A equação não possui raices possiveis, programa encerrado.')
  elif delta == 0.00:
    print('A equação possui apenas una raiz real. ')
    raiz = -(b) / (2*a)
    print(f'raiz : {raiz}')
  else:
    print('A equação possui duas raiz reais. ')
    raiz1 = (-(b) + math.sqrt(delta)) / (2 *a)
    raiz2 = (-(b) - math.sqrt(delta)) / (2 *a)
    print(f'Raiz 1 : {raiz1}')
    print(f'Raiz 2 : {raiz2}')
