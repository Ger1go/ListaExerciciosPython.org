#EXERCICIO 4.. Faça um Programa que peça as 4 notas bimestrais e mostre a média.

nota1 = int(input("Digite o primeiro numero correspondente a sua primeira nota bimestral: "))
nota2 = int(input("Digite a nota 2: "))
nota3 = int(input("Digite a nota 3: "))
nota4 = int(input("Digite a nota 4: "))
resposta = nota1+nota2+nota3+nota4/4
print(f"A sua media de nota bimestral é de: {resposta}")