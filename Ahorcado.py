import random
img_Ahorcado = ['''

  +---+
  |   |
      |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

palabras = 'hormiga babuino tejon murcielago oso castor camello gato almeja cobra pantera coyote cuervo ciervo perro burro pato aguila huron zorro rana cabra ganzo halcon leon lagarto llama topo mono alce raton mula salamandra nutria buho panda loro paloma piton conejo carnero rata cuervo rinoceronte salmon foca oveja mofeta perezoso serpiente arana ciguena cisne tigre sapo trucha pavo comadreja ballena lobo wombat cebra'.split()

def obtenerPalabraAlAZAR(listaDePalabras):
    #Esta funcion devuelve una cadena al azar de la lista de cadenas pasada como argumento.
    indiceDePalabras = random.randint(0, len(listaDePalabras) - 1)
    return listaDePalabras[indiceDePalabras]

def mostrarTablero(img_Ahorcado, letrasIncorrectas, letrasCorrectas, palabraSecreta):
    print(img_Ahorcado[len(letrasIncorrectas)])
    print()

    print('Letras incorrectas:', end=' ')
    for letra in letrasIncorrectas:
        print(letra, end=' ')
    print()

    espaciosVacios = '_' * len(palabraSecreta)

    for i in range(len(palabraSecreta)): #Completar los espacios vacios con las letras adivinadas

        if palabraSecreta[i] in letrasCorrectas:
            espaciosVacios = espaciosVacios[:i] = palabraSecreta[i] + espaciosVacios[i+1:]

    for letra in espaciosVacios: #Mostrar la palabra secreta con espacios entre cada lerta 
        print(letra, end=' ')
    print()
def obtenerIntento(letrasProbadas):
    #Devuelve la letra ingresada por el jugador. Verifica que el jugador ha ingresado solo una letra, y no otra cosa.
    while True:
        print('Adivina una letra.')
        intento = input()
        intento = intento.lower()
        if len(intento) != 1:
            print('Por favor, introduce una letra.')
        elif intento in letrasProbadas:
            print('Ya has probado esa letra . Elije otra.')
        elif intento not in 'abcdefghijklmnñopqrstuvwxyz':
            print('Por favor ingresa una LETRA.')
        else:
            return intento
    
def jugarDeNuevo():
        #Esta funcion devuelve true si el juego quiere volver a jugar, en caso contrario devuelve false.
    print('¿Quieres jugar de nuevo? (sí o no)')
    return input().lower().startswith('s')



print('A H O R C A D O')
letrasIncorrectas = ''
letrasCorrectas = ''
palabraSecreta = obtenerPalabraAlAZAR(palabras)
juegoTerminado = False

while True:
    mostrarTablero(img_Ahorcado, letrasIncorrectas, letrasCorrectas, palabraSecreta)

            #Permite al jugador escribir una letra.
    intento = obtenerIntento(letrasIncorrectas + letrasCorrectas)
            
    if intento in palabraSecreta:
        letrasCorrectas = letrasCorrectas + intento

            #Verifica si el jugador ha ganado.
        encontradoTodasLasLetras = True
        for i in range(len(palabraSecreta)):
            if palabraSecreta[i] not in letrasCorrectas:
                encontradoTodasLasLetras: False
                break
        
        if encontradoTodasLasLetras:
            print('¡Sí! ¡La palabra secreta es "' + palabraSecreta + '"! ¡Has ganado!')

            juegoTerminado = True
    else:
        letrasIncorrectas = letrasIncorrectas + intento

            #Comprobar si el jugador ha agotado todos sus intentos y ha perdido.
        if len(letrasIncorrectas)  == len(img_Ahorcado) - 1:
            mostrarTablero(img_Ahorcado, letrasIncorrectas, letrasCorrectas, palabraSecreta)
            print('¡Te has quedado sin intentos!\nDespués de ' + str(len(letrasIncorrectas)) + ' intentos fallidos y ' + str(len(letrasCorrectas)) + ' aciertos, la palabra era "' + palabraSecreta + '"')

            juegoTerminado = True

                #Preguntar al jugador si quiere volver a jugar (pero sólo si el juego ha terminado).

    if juegoTerminado:
        if jugarDeNuevo():
            letrasIncorrectas = ''
            letrasCorrectas = ''
            juegoTerminado = False
            palabraSecreta = obtenerPalabraAlAZAR(palabras)
        else:
            break             
    


