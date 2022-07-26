#EXERCICIO 15..

#Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados, faça:

#Mostre a quantidade de valores que foram lidos;

#Exiba todos os valores na ordem em que foram informados, um ao lado do outro;

#Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;

#Calcule e mostre a soma dos valores;

#Calcule e mostre a média dos valores;

#Calcule e mostre a quantidade de valores acima da média calculada;

#Calcule e mostre a quantidade de valores abaixo de sete;

#Encerre o programa com uma mensagem;

valores = []
valor = 0

while (valor != -1):
    valor = int(input('Informe um valor: '))
    if (valor != -1):
        valores.append(valor)

print(f'\nQuantidade de valores lidos: {len(valores)}')


print(*valores, sep = ' ')
valores.reverse()
print(*valores, sep = '\n')




somaValores = 0
for valor in valores:
    somaValores += valor

media = somaValores / float(len(valores))

print(f'\nSoma dos Valores: {somaValores}')
print(f'\nMedia dos Valores: {media:.2f}')

valoresAcimaDaMedia = 0
valoresAcimaDeSete = 0
for valor in valores:
    if (valor >= media):
        valoresAcimaDaMedia += 1
    if (valor >= 7):
        valoresAcimaDeSete += 1

print(f'\nValores acima da media: {valoresAcimaDaMedia}')
print(f'\nValores acima de sete: {valoresAcimaDeSete}')
