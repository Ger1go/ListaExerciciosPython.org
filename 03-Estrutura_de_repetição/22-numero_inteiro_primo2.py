#EXERCICIO 22..

#Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais número ele é divisível.

num = int(input('Digite um número inteiro patra descobrir se é um numero primo: '))
tot = 0
noprim = [] 
for c in range(1, num +1):
    if num % c == 0:
      noprim.append(c)
      tot += 1
print()    
if tot == 2:
  print(f'Ele é um número primo porque só é divisivel entre 1 e {num}')
else:
    print(f'Ele não é um número primo, pois é divisivel por {noprim}')