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
    last_letter = secret_word[len(secret_word) - 1]

    word_displayed = first_letter + "_" * (len(secret_word) -2) + last_letter
    # Imprimo la palabra con la primer letra y la ultima, los demas espacios los completo con "_"
    print(f"Palabra: {word_displayed}")

    guessed_letters.append(first_letter)
    guessed_letters.append(last_letter)

    mistakes = 0
    while mistakes < max_mistakes:
         # Pedir al jugador que ingrese una letra
        if word_displayed != secret_word:
            letter = input("Ingresa una letra: ").lower()
    
        #verificar que no se haya ingresado un espacio vacio
        if letter == "":
            print("Error, debe ingresar una letra")
            continue

        # Verificar si la letra ya ha sido adivinada
        if letter in guessed_letters and letter != first_letter and letter != last_letter:
            print("Ya has intentado con esa letra. Intenta con otra.")
            continue
        # Agregar la letra a la lista de letras adivinadas
        guessed_letters.append(letter)
    
        # Verificar si la letra está en la palabra secreta
        if letter in secret_word and word_displayed != secret_word:
            print("¡Bien hecho! La letra está en la palabra.")
            print("")
        else:
            if word_displayed != secret_word:
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

        if word_displayed == secret_word:
            print(f"¡Felicidades! Has adivinado la palabra secreta: {secret_word}")
            break
        else:
            word_displayed = "".join(letters)
            print(f"Palabra: {word_displayed}")
    else:
        print(f"¡Oh no! Has alcanzado tu numero maximo de Fallos.")
        print(f"La palabra secreta era: {secret_word}")

# Funcion "dificil"
def dificil(secret_word, max_mistakes, guessed_letters):
    
    word_displayed = "_" * len(secret_word)
    # Mostrar la palabra parcialmente adivinada
    print(f"Palabra: {word_displayed}")

    mistakes = 0
    while mistakes < max_mistakes:
         # Pedir al jugador que ingrese una letra
        letter = input("Ingresa una letra: ").lower()
    
        #verificar que no se haya ingresado un espacio vacio
        if letter == "":
            print("Error, debe ingresar una letra")
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


print("¡Bienvenido al juego de adivinanzas!")
print("Estoy pensando en una palabra. ¿Puedes adivinar cuál es?")
print("")
print("Niveles de dificultad: ")
print("1. Facil: Se muestran las vocales que contiene la palabra. ")
print("2. Media: Se muestra la primer y ultima letra de la palabra. ")
print("3. Dificil: No hay ningun tipo de Ayuda. ")
print("")
dif = (input("Seleccione el nivel de dificultad: "))
ok = True
while ok:
    match dif:
        case "1":
            print("")
            print("Nivel de dificultad elegido: Facil")
            print("")
            facil(secret_word, max_mistakes, guessed_letters)
            ok = False
        case "2":
            print("")
            print("Nivel de dificultad elegido: Media")
            print("")
            media(secret_word, max_mistakes, guessed_letters)
            ok = False
        case "3":
            print("")
            print("Nivel de dificultad elegido: Dificil")
            print("")
            dificil(secret_word, max_mistakes, guessed_letters)
            ok = False
        case _:
            print("")
            print("Error, no existe ese nivel de dificultad.")
            dif = (input("Seleccione el nivel de dificultad: "))
            print("")
