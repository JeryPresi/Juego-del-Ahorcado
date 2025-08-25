# Juego-del-Ahorcado
Explicación del Código del Juego del Ahorcado en Python
Este programa es una implementación básica del clásico juego del ahorcado, diseñada para ser sencilla y clara, facilitando su comprensión y extensión futura.

# Descripción General  
El juego del Ahorcado es un divertido y tradicional juego de adivinanza de palabras donde un jugador debe descubrir una palabra secreta letra por letra, dentro de un número limitado de intentos. Cada intento fallido acerca al jugador a perder la partida, mientras que cada acierto revela letras que componen la palabra. El objetivo es adivinar toda la palabra antes de agotar los intentos.

# !!!Actualizacion 1.10 24/08/2025

# def obtener_palabra(categoria)
Selecciona y devuelve una palabra aleatoria de la categoría dada.

# def modo_Multijudador
Modo multijugador con turnos alternados.
Cada jugador elige palabras para que el otro las adivine.
Se lleva un conteo de victorias y derrotas.
Permite configurar número de rondas antes de iniciar.

# def modo_solitario
Modo solitario donde el jugador elige categoría.
Se selecciona aleatoriamente una palabra dentro de la categoría.

# def inicio_juego
Menú principal para elegir el modo de juego o salir.

# Cambios en el juego
* Modo Multijugador para 2 Players
* Turnos alternados, número de rondas configurable por usuario en el modo multiplayer
* Seleccion de categoria en el modo Solitario
* Menús de selección, limpieza de pantalla simulada, mensajes más claros
* Los usuarios pueden repetir el modo o volver al menú principal
# !!!

# Detalles del Código
Importación de Módulos

import random: Se importa para seleccionar aleatoriamente una palabra de la lista disponible.

# Función obtener_palabra()

Define una lista fija de palabras.

Devuelve una palabra aleatoria de la lista para usarla como palabra secreta del juego.

# Función mostrar_tablero(palabra_secreta, letras_adivinadas)

Muestra en consola el estado actual de la palabra.

Las letras que el jugador ha adivinado se muestran visibles.

Las letras no adivinadas se representan con guiones bajos _.

# Función Principal juego_ahorcado()

Ejecuta la lógica completa del juego.

Inicializa la palabra secreta y el conjunto de letras que el jugador ya ha intentado.

El jugador tiene 6 intentos para adivinar.

En cada turno:

Se muestra el tablero con el estado actual.

Se solicita entrada al usuario y se valida que sea una sola letra alfabética.

Se verifica si la letra ya fue intentada antes.

Si es correcta, se agrega a las letras adivinadas; si es incorrecta, se descuenta un intento.

Se verifica si el jugador ha adivinado toda la palabra o ha agotado los intentos para mostrar el mensaje correspondiente de victoria o derrota.

# Control de ejecución con if __name__ == "__main__":

Garantiza que el juego se inicie solo cuando el archivo se ejecute directamente, no cuando se importe como módulo.

# Recomendaciones
Python 3.11.12
Spyder 6.0.7



