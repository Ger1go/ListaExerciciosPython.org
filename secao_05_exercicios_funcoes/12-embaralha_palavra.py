#EXERCICIO 12 ..

#Embaralha palavra. Construa uma função que receba uma string como parâmetro e devolva outra string com os carateres embaralhados. Por exemplo: se função receber a palavra python, pode retornar npthyo, ophtyn ou qualquer outra combinação possível, de forma aleatória. Padronize em sua função que todos os caracteres serão devolvidos em caixa alta ou caixa baixa, independentemente de como foram digitados.

from random import shuffle

def embaralha(palavra):
    
    lista = []
    for letra in palavra:
        lista.append(letra.lower())
        
    shuffle(lista)
    
    string = ''
    for i in lista:
        string = string + i
        
    return string

palavra = input('Informe uma palavra: ')
    
resultado = embaralha(palavra)

print(resultado)

