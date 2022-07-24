#EXERCICIO 11...

#Jogo de Forca. Desenvolva um jogo da forca. O programa terá uma lista de palavras lidas de um arquivo texto e escolherá uma aleatoriamente. O jogador poderá errar 6 vezes antes de ser enforcado.

#Digite uma letra: A
#-> Você errou pela 1ª vez. Tente de novo!

#Digite uma letra: O
#A palavra é: _ _ _ _ O

#Digite uma letra: E
#A palavra é: _ E _ _ O

#Digite uma letra: S
#-> Você errou pela 2ª vez. Tente de novo!

palavra = 'DevPro'.upper()
erros = 0 
print('Jogo da Forca')
print('Descubra a palavra!')

print('A palavra é: ', end = '')
for letra in palavra:
  print(f'_', end = ' ')

conjunto_letras_palavra = set(palavra)
conjunto_letras_digitadas = set()

while (not conjunto_letras_palavra.issubset(conjunto_letras_digitadas)) and erros < 7:
  print()
  print()
  letra_digitada = input('Digite uma letra: ').upper()
  conjunto_letras_digitadas.add(letra_digitada)
  if letra_digitada in conjunto_letras_palavra:
    print('A palavra é: ', end = '')
    for letra in palavra:
      if letra in conjunto_letras_digitadas:
        print(f'{letra} ', end = '')
      else:
        print(f' _ ', end = '')
  else:
    erros += 1
    print(f'-> {erros}° erro de 7. Tente novamente! ')
        
  print()
  print('\nLetras ja utilizadas: ', conjunto_letras_digitadas)

if erros < 7: 
  print('\nVitoria! Venceu o jogo da forca!')
else:
  print('\nInfelizmente perdeu!')
  