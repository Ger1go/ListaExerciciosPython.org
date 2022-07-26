# EXERCICIO 5..

#Faça um programa para a leitura de duas notas parciais de um aluno.

#O programa deve calcular a média alcançada por aluno e apresentar:

#A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;

#A mensagem "Reprovado", se a média for menor do que sete;

#A mensagem "Aprovado com Distinção", se a média for igual a dez.

nota_1 = float(input("Digite a sua primeira nota: \n"))

nota_2 = float(input('Digite a sua segunda nota: \n'))

media = (nota_1 + nota_2) / 2

print(f'Sua média foi: {media} \n')

if media >= 10:
  print('Aprovado com distinção!')
elif media >= 7:
  print('Aprovado!')
else:
  print("Você foi reprovado :'(")