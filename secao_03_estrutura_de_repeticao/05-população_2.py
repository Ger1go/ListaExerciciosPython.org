#EXERCICIO 5..

#Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.

print('Vamos calcular o número de anos necessários para igualar a população de dois paises.') 
pais1 = input('Digite o nome do primeiro país que deseja comparar: \n').upper()
população_a = int(input(f'Insira a população de {pais1}. \n'))
percentual1 = float(input(f'Digite a taxa de crescimento anual do {pais1}: \n'))
pais2 = input('Digite o nome do segundo país que deseja comparar: \n').upper()
população_b = int(input(f'Insira a população de {pais2}. \n'))
percentual2 = float(input(f'Digite a taxa de crescimento anual do {pais2}: \n'))
taxa_de_crescimento_de_a = (percentual1 + 100) / 100
taxa_de_crescimento_de_b = (percentual2 + 100) / 100
anos = 0 

while população_a < população_b:
    print(f'#################### VAI LEVAR {anos} ANOS #################### \n ')
    print(f'População de {pais1}: {população_a}')
    print(f'População de {pais2}: {população_b}')
    print()
    anos += 1
    população_a *= taxa_de_crescimento_de_a
    população_b *= taxa_de_crescimento_de_b
    