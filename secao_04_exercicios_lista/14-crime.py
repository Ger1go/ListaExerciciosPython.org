#EXERCICIO 14 ..

#Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:

#"Telefonou para a vítima?"

#"Esteve no local do crime?"

#"Mora perto da vítima?"

#"Devia para a vítima?"

#"Já trabalhou com a vítima?"

#O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

perguntas = ('\n Voce telefonou para a vitima?- S (sim) ou N (nao): ',
             '\n Voce esteve no local do crime?- S (sim) ou N (nao): ',
             '\n Voce mora perto da vitima?- S (sim) ou N (nao): ',
             '\n Voce devia para a vitima?- S (sim) ou N (nao): ',
             '\n Voce trabalhou para a vitima?- S (sim) ou N (nao): ')

respostas = []

for pergunta in perguntas:
    respostas.append(input(pergunta).upper())

classificacao = 0
for resposta in respostas:
    if (resposta == 'S'):
        classificacao += 1

if (classificacao < 2):
    print('\n Inocente')
elif (classificacao == 2):
    print('\n Suspeito')
elif (classificacao <= 4):
    print('\n Cumplice')
else:
    print('\n Assassino')

    