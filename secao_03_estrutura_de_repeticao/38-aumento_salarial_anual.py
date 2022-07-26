#EXERCICIO 38..

#Um funcionário de uma empresa recebe aumento salarial anualmente:

#Sabe-se que:

#-A Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;

#-B Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;

#-C A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior. Faça um programa que determine o salário atual desse funcionário. Após concluir isto, altere o programa permitindo que o usuário digite o salário inicial do funcionário.

salario_ini = float(input('Digite o seu salario inicial no ano de 1995: '))

for c in range(1995,1997):
  salario_ini = float(salario_ini * 1.015)

per = 1.03


for j in range(1996, 2023):
  salario_ini = float(salario_ini * per)
  per = float(per * 2)


print(f'Atualmente o seu salario é de $R {salario_ini:.2f} .')
