# Import modules to use
from words import *
import string
import random

# 1. Welcome
print("Welcome to the game hangman in Python")

def get_valid_word(palabras):
  word = random.choice(palabras)

  # Choose a good word
  while '-' in word or ' ' in word: # While - or ' '
    word = random.choice(palabras)

  return word.upper()




word = get_valid_word(palabras)
intentos = []
errores = []
vidas = 6

while vidas > 0:

    resultado = ""
    for letter in word:
        if letter in intentos:
            resultado = resultado + letter + " "
        else:
            resultado = resultado + ('_ ')


    if resultado == word:
         print("you win")
         break

    print("guess the word\n" , resultado)
    print("lives left: ", vidas)
    letra = input()

    if letra in intentos or letra in errores:
        print("already guessed: ", letra)
    elif letra in word:
        print("Acertaste")
        intentos.append(letra)
    else:
        print("try again")
        vidas = vidas - 1
        print(hangpics[vidas])
        errores.append(letra)

    if vidas == 0:
        print("you lost, word: ", word)


  


