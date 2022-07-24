#EXERCICIO 8...

#Palíndromo. Um palíndromo é uma seqüência de caracteres cuja leitura é idêntica se feita da direita para esquerda ou vice−versa. Por exemplo: OSSO e OVO são palíndromos. Em textos mais complexos os espaços e pontuação são ignorados. A frase SUBI NO ONIBUS é o exemplo de uma frase palíndroma onde os espaços foram ignorados. Faça um programa que leia uma seqüência de caracteres, mostre−a e diga se é um palíndromo ou não.

string = input('Informe uma string: ').upper()
contrario = string[::-1]

if (string.replace(' ', '') == contrario.replace(' ', '')):
    print('A string é um palindromo')
else:
    print('A string NAO é um palindromo')
