#EXERCICIO 12

#Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:

 #Tabuada de 5:
# 5 X 1 = 5
# 5 X 2 = 10
# ...
# 5 X 10 = 50

num = int(input('Digite o numero que deseja tabuar: '))

while 0 < num >10:
    num = int(input('So podemos tabuar números inteiros entre 0 e 10 por favor Digite o número novamente:  '))

print()
print(f'Tabuada de {num}: \n')

cont = 0
tab = 1


while cont < 10:
  res = int(num * tab)
  print(f'{num} X {tab} = {res}')
  cont = cont +1
  tab = tab +1