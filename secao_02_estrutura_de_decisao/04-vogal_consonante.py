#EXERCICIO 4.. Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letra = input('Digite uma letra para saber se é vogal ou consonante \n')

vogais = "aeiou"

if letra in vogais or letra in vogais.upper():
  print(f"A letra '{letra}' é uma: Vogal! ")
else:
  print(f"A letra '{letra}' é uma: Consonante!. ")