#EXERCICIO 26..

#Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.

print('VENVINDO AO PROGRAMA ELEITORAL 3.0:')
eleitores = int(input('Qual é o número de eleitores? \n'))
lista_votos1 = 0
lista_votos2 = 0
lista_votos3 = 0

print('Esses são os candidatos: ') 

print('Digite 1 para votar no candidato 1')
print('Digite 2 para votar no candidato 2')
print('Digite 3 para votar no candidato 3')

for c in range(eleitores):
  voto = int(input(' O seu voto vai para:  '))
  if voto > 3:
    voto = int(input('Valor invalido, por favor escolha um candidato do 1 até o 3. O seu voto vai para:  '))
  if voto == 1:
    lista_votos1 += 1
  elif voto == 2:
    lista_votos2 += 1
  elif voto == 3:
    lista_votos3 += 1
    
total1 = lista_votos1

total2 = lista_votos2

total3 = lista_votos3


votos_totais = max(total1, total2, total3)

if votos_totais == total1 and votos_totais == total2:
    print(f'EMPATE entre o candidato 1 e candidato 2! Com um total de {votos_totais} votos! ')
elif votos_totais == total1 and votos_totais == total3:
      print(f'EMPATE entre o candidato 1 e candidato 3!Com um total de {votos_totais} votos!')
elif votos_totais == total2 and votos_totais == total3:
      print(f'EMPATE entre o candidato 2 e candidato 3!Com um total de {votos_totais} votos!')
else:
  if votos_totais == total1:
    total = total1 
    votos_totais = 'Candidato 1'
  elif votos_totais == total2:  
    total = total2
    votos_totais = 'Candidato 2'
  elif votos_totais == total3:  
    total = total3 
    votos_totais = 'Candidato 3'


  print(f'O {votos_totais} é o ganhador! Com um total de {total} votos! ')