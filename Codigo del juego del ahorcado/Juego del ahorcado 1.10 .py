import random

# Diccionario de categorías con listas de palabras
categorias_palabras = {
    "frutas": ["manzana", "banana", "naranja", "pera", "uva"],
    "paises": ["mexico", "canada", "brasil", "españa", "francia"],
    "colores": ["rojo", "azul", "verde", "amarillo", "negro"],
    "cocina": ["sarten", "cuchillo", "olla", "refrigerador", "microondas"],
    "bano": ["ducha", "lavabo", "espejo", "jabon", "toalla"],
    "dormitorio": ["cama", "almohada", "edredon", "armario", "lampara"],
    "nombres": ["ana", "juan", "maria", "carlos", "luis"]
}

def obtener_palabra(categoria):
    
    """Selecciona y devuelve una palabra aleatoria de la categoría dada. """
    
    palabras = categorias_palabras.get(categoria, [])
    if palabras:
        return random.choice(palabras)

def mostrar_tablero(palabra_secreta, letras_adivinadas):
    
    """Muestra la palabra con las letras adivinadas y guiones bajos para las letras faltantes."""
  
    estado = ""
    for letra in palabra_secreta:
        if letra in letras_adivinadas:
            estado += letra + " "
        else:
            estado += "_ "
    print(estado.strip())

def juego_ahorcado(palabra_secreta):
    
    """Función principal que maneja la lógica del juego del ahorcado para una palabra dada.
    Controla los intentos, las letras adivinadas y muestra el progreso al usuario."""
    
    letras_adivinadas = set()
    intentos = 3  # número de intentos permitidos
    letras_intentadas = set()
    print("¡Comienza tu turno!")

    while intentos > 0:
        mostrar_tablero(palabra_secreta, letras_adivinadas)
        print(f"Letras incorrectas intentadas: {', '.join(sorted(letras_intentadas))}")
        intento_letra = input("Adivina una letra: ").lower()

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
            print(f"Letra incorrecta. Te quedan {intentos} intentos.")

        if all(letra in letras_adivinadas for letra in palabra_secreta):
            print("\n" * 50)
            print(f"¡Felicidades! Adivinaste la palabra: {palabra_secreta}")
            return True
    
    print("\n" * 50)
    print(f"Perdiste. La palabra era: {palabra_secreta}")
    return False

def modo_multijugador():
    
    """Modo multijugador con turnos alternados.
    Cada jugador elige palabras para que el otro las adivine.
    Se lleva un conteo de victorias y derrotas.
    Permite configurar número de rondas antes de iniciar."""
    
    jugador_actual = 1

    while True:
        # Solicitar número de rondas válido al inicio
        while True:
            try:
                rondas_maximas = int(input("Ingresa el número de rondas que desean jugar (mínimo 1): "))
                if rondas_maximas >= 1:
                    break
                else:
                    print("El número debe ser al menos 1.")
            except ValueError:
                print("Por favor, ingresa un número válido.")
    
        jugadores = {
            1: {"victorias": 0, "derrotas": 0},
            2: {"victorias": 0, "derrotas": 0}
        }

        rondas_jugadas = 0
        jugadores[1]["victorias"] = 0
        jugadores[1]["derrotas"] = 0
        jugadores[2]["victorias"] = 0
        jugadores[2]["derrotas"] = 0

        while rondas_jugadas < rondas_maximas:
            print(f"rondas establecidas {rondas_maximas} ")
            palabra = input(f"Jugador {jugador_actual}, ingresa la palabra secreta para que el jugador {2 if jugador_actual == 1 else 1} adivine: ").lower()
            while not palabra.isalpha():
                print("La palabra debe contener solo letras. Intenta de nuevo.")
                palabra = input(f"Jugador {jugador_actual}, ingresa la palabra secreta: ").lower()
            print("\n" * 50)
            resultado = juego_ahorcado(palabra)

            if resultado:
                ganador = 2 if jugador_actual == 1 else 1
                jugadores[ganador]["victorias"] += 1
                jugadores[jugador_actual]["derrotas"] += 1
            else:
                ganador = jugador_actual
                jugadores[ganador]["victorias"] += 1
                jugadores[2 if jugador_actual == 1 else 1]["derrotas"] += 1

            rondas_jugadas += 1
            jugador_actual = 2 if jugador_actual == 1 else 1

        print("\n" * 50)
        print("Juego terminado.")
        print(f"Resultados después de {rondas_maximas} rondas:")
        print(f"Jugador 1 - Victorias: {jugadores[1]['victorias']}, Derrotas: {jugadores[1]['derrotas']}")
        print(f"Jugador 2 - Victorias: {jugadores[2]['victorias']}, Derrotas: {jugadores[2]['derrotas']}")

        opcion = input("¿Quieres jugar otra vez (si) o volver al inicio (no)? ").lower()
        while opcion not in ['si', 'no']:
            opcion = input("Por favor ingresa 'si' para repetir o 'no' para ir al inicio: ").lower()
        if opcion == 'no':
            print("\n" * 50)
            break

def modo_solitario():
    
    """ Modo solitario donde el jugador elige categoría.
    Se selecciona aleatoriamente una palabra dentro de la categoría."""
    
    while True:
        print("Selecciona una categoría:")
        for i, cat in enumerate(categorias_palabras.keys(), 1):
            print(f"{i}. {cat.capitalize()}")

        while True:
            opcion = input("Ingresa el número de la categoría deseada: ")
            if opcion.isdigit() and 1 <= int(opcion) <= len(categorias_palabras):
                categoria_seleccionada = list(categorias_palabras.keys())[int(opcion) - 1]
                break
            else:
                print("Opción inválida. Ingresa una opcion del 1 al 7.")

        palabra = obtener_palabra(categoria_seleccionada)
        print("\n" * 50)
        print(f"\nHas seleccionado la categoría: {categoria_seleccionada.capitalize()}\n")
        juego_ahorcado(palabra)

        opcion = input("¿Quieres jugar otra vez (si) o volver al inicio (no)? ").lower()
        while opcion not in ['si', 'no']:
            opcion = input("Por favor ingresa 'si' para repetir o 'no' para ir al inicio: ").lower()
        if opcion == 'no':
            print("\n" * 50)
            break

def inicio_juego():
    
    """Menú principal para elegir el modo de juego o salir."""
    
    while True:
        print("¡Bienvenido al juego del Ahorcado!")
        print("Selecciona el modo de juego:")
        print("1. Un solo jugador (palabra aleatoria)")
        print("2. 2 Jugadores (turnos alternados con límite de rondas)")
        print("3. Salir")
        modo = input("Ingresa 1, 2 o 3 según el modo deseado: ")
        
        if modo == "1":
            print("\n" * 50)
            modo_solitario()
            
        elif modo == "2":
            print("\n" * 50)
            modo_multijugador()
        
        elif modo == "3":
            print("\n" * 50)
            print("Gracias por jugar. ¡Hasta pronto!")
            break
        else:
            print("Opción no válida, por favor ingresa 1, 2 o 3.")

if __name__ == "__main__":
    inicio_juego()
