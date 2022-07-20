#EXERCICIO 17.. Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.

#---------------------------------------------------------------------------------------------------------------------------

#Para calcularmos se um ano é bissexto utilizamos uma regra bastante prática, se o ano não terminar em 00 e for divisível por 4 dizemos que ele é bissexto. 
#Um número é divisível por 4 quando a sua dezena é divisível por 4. Por exemplo, 1988 é divisível por 4, pois 88:4 = 22. 
#Portanto, os seguintes anos são bissextos: 1988, 1992, 1996, 2000, 2004, 2008, 2012, 2016, 2020, 2024, 2028, 2032, 2036, 2040, 2044, 2048, 2052, ... .
# Os anos terminados em 00 serão bissextos se a divisão deles por 400 for exata, isto é, o resto da divisão precisa ser igual a zero.

#---------------------------------------------------------------------------------------------------------------------------

from datetime import date
ano = int(input('Digite um ano para saber se ele foi bissexto ou não, se quiser saber o ano atual, digite 0 :'))
print()
if ano == 0:
  ano = date.today().year
  

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
  print(f'O ano {ano} é BISSEXTO.')
else:
  print(f'O ano {ano} não é BISSEXTO.')
