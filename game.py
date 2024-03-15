import random
# Lista de palabras posibles
words = ["python", "programacion", "computadora", "codigo", "desarrollo",
"inteligencia"]

# Elegir una palabra al azar
secret_word = random.choice(words)
# Número máximo de intentos permitidos
max_mistakes = 6
# Lista para almacenar las letras adivinadas
guessed_letters = []

print("¡Bienvenido al juego de adivinanzas!")
print("Estoy pensando en una palabra. ¿Puedes adivinar cuál es?")

# Funcion "facil"
def facil(secret_word, max_mistakes, guessed_letters):
    # Agrego las vocales a las letras adivinadas
    guessed_letters = ["a","e","i","o","u"]

    # Mostrar la palabra parcialmente adivinada
    letters = []
    for letter in secret_word:
        if letter in guessed_letters:
            letters.append(letter)
        else:
            letters.append("_")
    
    word_displayed = "".join(letters)
    print(f"Palabra: {word_displayed}")

    mistakes = 0
    while mistakes < max_mistakes:
        # Pedir al jugador que ingrese una letra
        letter = input("Ingresa una letra: ").lower()
    
        #verificar que no se haya ingresado un espacio vacio
        if letter == "":
            print("Error. Debe ingresar una letra")
            continue

        # Verificar si la letra ya ha sido adivinada
        if letter in guessed_letters:
            print("Ya has intentado con esa letra. Intenta con otra.")
            continue
        # Agregar la letra a la lista de letras adivinadas
        guessed_letters.append(letter)
    
        # Verificar si la letra está en la palabra secreta
        if letter in secret_word:
            print("¡Bien hecho! La letra está en la palabra.")
            print("")
        else:
            print("Lo siento, la letra no está en la palabra.")
            mistakes += 1
            print("Numeros de Fallos: ", mistakes)
            print("")
 
        # Mostrar la palabra parcialmente adivinada
        letters = []
        for letter in secret_word:
            if letter in guessed_letters:
                letters.append(letter)
            else:
                letters.append("_")
    
        word_displayed = "".join(letters)
        print(f"Palabra: {word_displayed}")
        # Verificar si se ha adivinado la palabra completa
        if word_displayed == secret_word:
            print(f"¡Felicidades! Has adivinado la palabra secreta: {secret_word}")
            break
    else:
        print(f"¡Oh no! Has alcanzado tu numero maximo de Fallos.")
        print(f"La palabra secreta era: {secret_word}")

# Funcion "media"
def media (secret_word, max_mistakes, guessed_letters):
    first_letter = secret_word[0]
    last_letter = secret_word[len(secret_word)]

    word_displayed = first_letter + "_" * (len(secret_word) -2) + last_letter
    # Imprimo la palabra con la primer letra y la ultima, los demas espacios los completo con "_"
    print(f"Palabra: {word_displayed}")

    mistakes = 0
    while mistakes < max_mistakes:
         # Pedir al jugador que ingrese una letra
        letter = input("Ingresa una letra: ").lower()
    
        #verificar que no se haya ingresado un espacio vacio
        if letter == "":
            continue

        # Verificar si la letra ya ha sido adivinada
        if letter in guessed_letters:
            print("Ya has intentado con esa letra. Intenta con otra.")
            continue
        # Agregar la letra a la lista de letras adivinadas
        guessed_letters.append(letter)
    
        # Verificar si la letra está en la palabra secreta
        if letter in secret_word:
            print("¡Bien hecho! La letra está en la palabra.")
            print("")
        else:
            print("Lo siento, la letra no está en la palabra.")
            mistakes += 1
            print("Numeros de Fallos: ", mistakes)
            print("")
 
        # Mostrar la palabra parcialmente adivinada
        letters = []
        for letter in secret_word:
            if letter in guessed_letters:
                letters.append(letter)
            else:
                letters.append("_")
    
        word_displayed = "".join(letters)
        print(f"Palabra: {word_displayed}")
        # Verificar si se ha adivinado la palabra completa
        if word_displayed == secret_word:
            print(f"¡Felicidades! Has adivinado la palabra secreta: {secret_word}")
            break
    else:
        print(f"¡Oh no! Has alcanzado tu numero maximo de Fallos.")
        print(f"La palabra secreta era: {secret_word}")

word_displayed = "_" * len(secret_word)
# Mostrar la palabra parcialmente adivinada
print(f"Palabra: {word_displayed}")

mistakes = 0
while mistakes < max_mistakes:
     # Pedir al jugador que ingrese una letra
    letter = input("Ingresa una letra: ").lower()
    
    #verificar que no se haya ingresado un espacio vacio
    if letter == "":
        continue

    # Verificar si la letra ya ha sido adivinada
    if letter in guessed_letters:
        print("Ya has intentado con esa letra. Intenta con otra.")
        continue
    # Agregar la letra a la lista de letras adivinadas
    guessed_letters.append(letter)
    
    # Verificar si la letra está en la palabra secreta
    if letter in secret_word:
        print("¡Bien hecho! La letra está en la palabra.")
        print("")
    else:
        print("Lo siento, la letra no está en la palabra.")
        mistakes += 1
        print("Numeros de Fallos: ", mistakes)
        print("")
 
    # Mostrar la palabra parcialmente adivinada
    letters = []
    for letter in secret_word:
        if letter in guessed_letters:
            letters.append(letter)
        else:
            letters.append("_")
    
    word_displayed = "".join(letters)
    print(f"Palabra: {word_displayed}")
    # Verificar si se ha adivinado la palabra completa
    if word_displayed == secret_word:
        print(f"¡Felicidades! Has adivinado la palabra secreta: {secret_word}")
        break
else:
    print(f"¡Oh no! Has alcanzado tu numero maximo de Fallos.")
    print(f"La palabra secreta era: {secret_word}")