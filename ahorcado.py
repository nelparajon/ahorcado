from unidecode import unidecode
from words import *
import random

def generar_palabra():
    palabra = random.choice(words)
    return palabra

def tablero(palabra, intentos):
    tablero = "_" * len(palabra)
    length = len(palabra)
    print(tablero)
    print(f"Longitud de la palabra: {length}")
    print(f"Intentos iniciales: {intentos}")
    return tablero

def player():
    letra = input("Introduce una letra: ")
    letra_sin_tilde = unidecode(letra)
    return letra_sin_tilde

def juego(letra, tablero, intentos, palabra):
    posiciones = [i for i, char in enumerate(palabra) if char == letra]
    if posiciones:
        for posicion in posiciones:
            tablero = tablero[:posicion] + letra + tablero[posicion + 1:]
        print(tablero)
        print(f"Sigues con : {intentos} intentos")
        return tablero, intentos
    else:
        intentos -= 1
        print(f"Inténtalo de nuevo. Te quedan {intentos} intentos.")
        print(tablero)
        return tablero, intentos

if __name__ == "__main__":
    print("Bienvenido al juego del ahorcado.")

    while True:
    # Genera la palabra antes de llamar a las otras funciones
        palabra = generar_palabra()

        intentos = 8
        tablero_actual = tablero(palabra, intentos)

        while intentos > 0 and "_" in tablero_actual:
            letra_usuario = player()
            tablero_actual, intentos = juego(letra_usuario, tablero_actual, intentos, palabra)
    
        if "_" not in tablero_actual:
            print("¡Felicidades! Has adivinado la palabra. ¿Quieres volver a jugar? Pulsa s para sí o n para no")
            respuesta = input()
        else:
            print(f"¡Lo siento! La palabra era {palabra}. Intentalo de nuevo.")
            respuesta = input("¿Quieres volver a intentarlo? Pulsa s para sí o n para no")

        if respuesta.lower() != 's':
            print("Gracias por jugar. Hasta la próxima")
            break
