import random


def obtener_palabra():
    """Selecciona una palabra aleatoria de una lista predefinida."""
    palabras = ["python", "programacion", "ahorcado", "juego", "codigo","amor", "pelicula", "vida"]
    return random.choice(palabras)

def mostrar_tablero(palabra_secreta, letras_adivinadas):
    """Muestra la palabra con las letras adivinadas y guiones para las faltantes."""
    estado = ""
    for letra in palabra_secreta:
        if letra in letras_adivinadas:
            estado += letra + " "
        else:
            estado += "_ "
    print(estado.strip())
    """El bucle for va a verificar letra por letra en la plabara secreta, 
    si la letra esta en la palabra la muestra mas un espacio en caso contrario 
    se muestra un guión bajo _"""
def juego_ahorcado():
    palabra_secreta = obtener_palabra()
    letras_adivinadas = set()
    intentos = 2
    letras_intentadas = set()
    
    print("¡Bienvenido al juego del Ahorcado!")
    while intentos > 0:
        """Usamos el bucle while para mantener activo mientras el valor
        de intentos sea mayor a 0"""
        mostrar_tablero(palabra_secreta, letras_adivinadas)
        intento_letra = input("Adivina una letra: ").lower()

        # Validar entrada
        if len(intento_letra) != 1 or not intento_letra.isalpha():
            print("Por favor, ingresa solo una letra.")
            continue

        if intento_letra in letras_adivinadas:
            print("Ya has adivinado esa letra.")
            continue
        
        if intento_letra in letras_intentadas:
            print("Ya has intentado esa letra.")
            continue

        if intento_letra in palabra_secreta:
            letras_adivinadas.add(intento_letra)
            print("¡Bien! Letra correcta.")
        else:
            letras_intentadas.add(intento_letra)
            intentos -= 1
            print(f"Letra incorrecta. Te quedan %d intentos." % (intentos ))

        # Verificar si ganó
        if all(letra in letras_adivinadas for letra in palabra_secreta):
            print(f"¡Felicidades! Adivinaste la palabra: {palabra_secreta}")
            break
    else:
        print(f"Perdiste. La palabra era: {palabra_secreta}")

if __name__ == "__main__":
    juego_ahorcado()
"""llama a la función juego_ahorcado() para iniciar el juego."""

