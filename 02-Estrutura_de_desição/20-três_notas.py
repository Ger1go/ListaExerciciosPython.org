#EXERCICIO 20.. Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e presentar:

#A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;

#A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;

#A mensagem "Aprovado com Distinção", se a média for igual a 10.

print('Vamos calcular a media alcançada do seu aluno. Por favor digite as três notas dos parciais:')

n1 = int(input('Nota 1: '))
n2 = int(input('Nota 2: '))
n3 = int(input('Nota 3: '))

media = int((n1 + n2 + n3) / 3 )

if media < 7:
    print(f'Seu aluno foi REPROVADO, sua nota media foi: {media}.')

elif media >= 7 and media < 10:
  print(f'Seu aluno foi APROVADO, sua nota media foi: {media}.')

else:
 print(f'Seu aluno foi APROVADO COM DISTINÇÃO! sua nota media foi de:1 {media}!')