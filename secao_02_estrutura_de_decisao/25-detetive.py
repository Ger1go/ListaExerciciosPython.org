#EXERCICIO 25.. Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:

#"Telefonou para a vítima?"

#"Esteve no local do crime?"

#"Mora perto da vítima?"

#"Devia para a vítima?"

#"Já trabalhou com a vítima?"

#O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".


print('Olá! bem-vindo ao detetive virtual 2.0!\n')
print('Por favor responda as seguintes perguntas com (S) para sim e (N) para não. \nVamos começar! \n')

res1 = input("Telefonou para a vítima? \n").upper()
res2 = input("Esteve no local do crime? \n").upper()
res3 = input("Mora perto da vítima? \n").upper()
res4 = input("Devia para a vítima? \n").upper()
res5 = input("Já trabalhou com a vítima? \n").upper()

quantidade_positivo = 0

if res1 == 'S':
  quantidade_positivo += 1
if res2 == 'S':
  quantidade_positivo += 1
if res3 == 'S':
  quantidade_positivo += 1
if res4 == 'S':
  quantidade_positivo += 1
if res5 == 'S':
  quantidade_positivo += 1

status = {2 : "Só um Suspeito(a), vamos ficar de olho...",
          3 : "Um(a) Cúmplice! Que falta de vergonha na cara... ",
          4 : "Um(a) Cúmplice! Que falta de vergonha na cara... ",
          5 : "Um Assassino(a)!!! Policia! prenda essa pessoa! "}

print('Sem lugar a duvidas! você é: \n')

if quantidade_positivo in status:
  print(status[quantidade_positivo])
else:
  print('Você é INOCENTE!')