#EXERCICIO 9.. Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius. C = 5 * ((F-32) / 9).

F = float(input("Informe a temperatura em graus Fahrenheit para fazer a conversão a graus celsius: "))
C = 5 *((F-32)/9) 
print(f"A temperatura em graus celsius é de: {C:.2f}°")
