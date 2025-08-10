# Juego-del-Ahorcado
Explicación del Código del Juego del Ahorcado en Python
Este programa es una implementación básica del clásico juego del ahorcado, diseñada para ser sencilla y clara, facilitando su comprensión y extensión futura.

Descripción General
El juego selecciona una palabra secreta al azar de una lista predefinida y el jugador debe adivinar las letras de esa palabra. Tiene un número limitado de intentos para hacerlo antes de perder. El programa muestra el estado actual de la palabra con los aciertos y guiones bajos para las letras aún no descubiertas.

Detalles del Código
Importación de Módulos

import random: Se importa para seleccionar aleatoriamente una palabra de la lista disponible.

Función obtener_palabra()

Define una lista fija de palabras.

Devuelve una palabra aleatoria de la lista para usarla como palabra secreta del juego.

Función mostrar_tablero(palabra_secreta, letras_adivinadas)

Muestra en consola el estado actual de la palabra.

Las letras que el jugador ha adivinado se muestran visibles.

Las letras no adivinadas se representan con guiones bajos _.

Función Principal juego_ahorcado()

Ejecuta la lógica completa del juego.

Inicializa la palabra secreta y el conjunto de letras que el jugador ya ha intentado.

El jugador tiene 6 intentos para adivinar.

En cada turno:

Se muestra el tablero con el estado actual.

Se solicita entrada al usuario y se valida que sea una sola letra alfabética.

Se verifica si la letra ya fue intentada antes.

Si es correcta, se agrega a las letras adivinadas; si es incorrecta, se descuenta un intento.

Se verifica si el jugador ha adivinado toda la palabra o ha agotado los intentos para mostrar el mensaje correspondiente de victoria o derrota.

Control de ejecución con if __name__ == "__main__":

Garantiza que el juego se inicie solo cuando el archivo se ejecute directamente, no cuando se importe como módulo.
