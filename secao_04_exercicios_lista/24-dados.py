#EXERCICIO 24...

#Faça um programa que simule um lançamento de dados. Lance o dado 100 vezes e armazene os resultados em um vetor . Depois, mostre quantas vezes cada valor foi conseguido. Dica: use um vetor de contadores(1-6) e uma função para gerar numeros aleatórios, simulando os lançamentos dos dados.

import random

dado = [0] * 6

for i in range(0, 100):
    lancamento = random.randint(0, 5)
    dado[lancamento] += 1

for i in range(0, 6):
    print(f'{i + 1} - {dado[i]}') 

    