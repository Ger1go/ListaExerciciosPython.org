#EXERCICIO 12.. Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58

altura = float(input("Por favor digite a sua altura para saber qual é seu peso ideal: "))
peso = 72.7*altura - 58
peso2 = int(peso)
print(f"O seu peso ideal é: {peso2}Kg")